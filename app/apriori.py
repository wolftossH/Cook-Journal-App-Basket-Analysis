import sqlite3
from collections import defaultdict

from apyori import apriori
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import json
import ast

df = pd.read_csv("RAW_recipes.csv.zip")
dish_ing = df[['name','ingredients']].copy()
dish_ing.loc[:,'ingredients'] = dish_ing['ingredients'].apply(lambda lst: set(ast.literal_eval(lst)))


# Fetch dataset from user input & add to list
conn = sqlite3.connect('dishes.db')
# Create a cursor
c = conn.cursor()
c.execute("SELECT DISTINCT * FROM dishes_list")
user_records = c.fetchall()

# Commit the changes & close connection
conn.commit()
conn.close()

# Create df for user inputs
user_records_dct = []
for dish, items in user_records:
    items_set = set([i.lstrip().rstrip() for i in items.split(',')])
    dictionary_data = {'name': dish, 'ingredients':items_set}
    user_records_dct.append(dictionary_data)
user_df= pd.DataFrame.from_dict(user_records_dct)
user_df.head()

# concat with Kaggle dataset
dish_ing = pd.concat([dish_ing, user_df], ignore_index=True)

# Create a list of sets of ingredients for searching & the apyori library
ing_series = dish_ing['ingredients']
ingredients_lsts = ing_series.to_list()

# Create dict for searching
ing_dct = defaultdict(set)
for n, ings in zip(dish_ing['name'],dish_ing['ingredients']):
    for item in ings:
        ing_dct[item].add(n)


def searching_dish(search_ings):
    '''
    Give out dish name by searching for ingredients
    '''
    wanted_dishes = set()
    for s_ing in search_ings:
        if s_ing in ing_dct and wanted_dishes:
            wanted_dishes = wanted_dishes.intersection(ing_dct[s_ing])
        else:
            wanted_dishes = wanted_dishes.union(ing_dct[s_ing])
            
    return wanted_dishes

# Use Apriori algo
association_rules = apriori(ingredients_lsts, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)


# Create a dataframe with Support, Confidence & Lift scores for each items set
scores_df = pd.DataFrame(columns = ['Ingredients','Items_Base', 'Items_Added', 'Support', 'Confidence','Lift'])
for relation in association_results:
    ing = set(relation.items)
    support = relation.support
    for ord_stat in relation.ordered_statistics:
        scores_df = scores_df.append(
            {'Ingredients' : ing, 'Items_Base' : set(ord_stat.items_base), 'Items_Added' : set(ord_stat.items_add),
             'Support' : support, 'Confidence' : ord_stat.confidence, 'Lift' : ord_stat.lift},
            ignore_index = True
        )
score_sorted_df = scores_df.sort_values(by=['Support', 'Confidence','Lift'], ascending=False)
# Create recommended dishes based on items base
score_sorted_df['recommend_dishes'] = score_sorted_df['Ingredients'].apply(lambda lst: searching_dish(lst))


def recommend(ings_set, df, top_k = 5):
    '''
    Recommend Dishes & Ingredient based on Support, Confidence & Lift scores
    '''
    ings_set = set(ings_set)
    found_records = (
        df[df['Items_Base']==ings_set]
        .sort_values(by=['Support', 'Confidence','Lift'], ascending=False,ignore_index=True)
    )
    wanted_dishes = set()
    # if there exit something in base then slowly start to pull out recommended dishes
    if found_records['Items_Base']:        
#         top k dishes using series indexing so no need to change top_k
        for dishes_set in found_records['recommend_dishes'][:top_k]:         
            if wanted_dishes:
                wanted_dishes = wanted_dishes.intersection(dishes_set)
            else:
                wanted_dishes = wanted_dishes.union(dishes_set)
    # start to search in Ingredients to see if there exists any sets
    #     get top_k recommended food
    else:
        new_found_ing = (
        df[df['Ingredients']==ings_set]
        .sort_values(by=['Support', 'Confidence','Lift'], ascending=False,ignore_index=True)
        ).loc[:top_k,:]
        for dishes_set in new_found_ing['recommend_dishes']:         
            if wanted_dishes:
                wanted_dishes = wanted_dishes.intersection(dishes_set)
            else:
                wanted_dishes = wanted_dishes.union(dishes_set)
        
    return wanted_dishes
    