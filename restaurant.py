from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QLabel
import sqlite3
from collections import defaultdict

# support of list of ingredients along with dish
# spaghetti ~ tomatoes, sauce, 

# Create a database or connect to one
conn = sqlite3.connect('dishes.db')

# Create a cursor
c = conn.cursor()
# Create a table
c.execute("""CREATE TABLE if not exists dishes_list
        (dish_name text,
        ingredients text)
    """)
c.execute('PRAGMA table_info(dishes_list);')
records = c.fetchall()
# Commit the changes
conn.commit()
# Close our connection
conn.close()
print(records)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        buttons_x = 10
        buttons_y = 50
        padding = 50

        box_size_x = 140
        box_size_y = 35

        # size of displayed window
        MainWindow.setWindowIcon(QtGui.QIcon('wolf.jpg'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(buttons_x+3*box_size_x+padding, buttons_y + box_size_y*10)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QLabel(self.centralwidget)
        pixmap = QPixmap("wolf.jpg")
        pixmap = pixmap.scaled(padding*4, padding*4, QtCore.Qt.KeepAspectRatio)
        self.photo.setPixmap(pixmap)
        self.photo.move(100, 300)

        # Let user type in their dish for an entry
        self.additem_blankbox = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_blankbox.setGeometry(QtCore.QRect(buttons_x, buttons_y/5, buttons_x+3*box_size_x, box_size_y))
        self.additem_blankbox.setObjectName("additem_blankbox")
        self.additem_blankbox.setPlaceholderText("Dish Name") 

        # Let user add dish 
        self.add_dish_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add())
        self.add_dish_pushButton.setGeometry(QtCore.QRect(buttons_x, buttons_y, box_size_x, box_size_y))
        self.add_dish_pushButton.setObjectName("add_dish_pushButton")

        # Let user delete dish 
        self.delete_dish_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete())
        self.delete_dish_pushButton.setGeometry(QtCore.QRect(buttons_x+box_size_x, buttons_y, box_size_x, box_size_y))
        self.delete_dish_pushButton.setObjectName("delete_dish_pushButton")

        # Let user view dish using pop up window
        self.view_list = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.view())
        self.view_list.setGeometry(QtCore.QRect(buttons_x+2*box_size_x, buttons_y, box_size_x, box_size_y))
        self.view_list.setObjectName("view_list")

        # Let user view dish using pop up window
        self.searching_dish = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.searching())
        self.searching_dish.setGeometry(QtCore.QRect(buttons_x+box_size_x, buttons_y*3, box_size_x, box_size_y))
        self.searching_dish.setObjectName("searching")

        # Let user type in their dish for an entry
        self.searching_blankbox = QtWidgets.QLineEdit(self.centralwidget)
        self.searching_blankbox.setGeometry(QtCore.QRect(buttons_x, buttons_y*4, buttons_x+3*box_size_x, box_size_y))
        self.searching_blankbox.setObjectName("searching_blankbox")
        self.searching_blankbox.setPlaceholderText("Search Dish based on Ingredients") 


        # Let user type in their ingredients for an entry
        self.add_ing_blankbox = QtWidgets.QLineEdit(self.centralwidget)
        self.add_ing_blankbox.setGeometry(QtCore.QRect(buttons_x, buttons_y*2, buttons_x+3*box_size_x, box_size_y))
        self.add_ing_blankbox.setObjectName("add_ing_blankbox")
        self.add_ing_blankbox.setPlaceholderText("Dish Ingredients") 

        # Let user clear all dishes
        self.clearall_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clear_all())
        self.clearall_pushButton.setGeometry(QtCore.QRect(buttons_x+3*box_size_x, buttons_y, box_size_x, box_size_y))
        self.clearall_pushButton.setObjectName("clearall_pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # # Let user save dishes to database
        # self.savedb_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.save())
        # self.savedb_pushButton.setGeometry(QtCore.QRect(buttons_x+4*box_size_x, buttons_y, box_size_x, box_size_y))
        # self.savedb_pushButton.setObjectName("savedb_pushButton")



        # Appear on main screen
        # bigbox_size = buttons_x+4*box_size_x + box_size_x
        # self.mylist = QtWidgets.QListWidget(self.centralwidget)
        # self.mylist.setGeometry(QtCore.QRect(bigbox_size/4, buttons_y*2, bigbox_size/2, box_size_y*8))
        # self.mylist.setObjectName("mylist")

        # Grab all dishes from db
        # self.grab_all()

    def add(self):
        '''
        Add Dish To List
        '''
        # Grab the item from the list box
        item = self.additem_blankbox.text()
        ing = self.add_ing_blankbox.text()

        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor

        cur = conn.cursor()
        add_query = 'INSERT INTO dishes_list (dish_name, ingredients) VALUES (?, ?)'
        cur.execute(add_query, (item, ing))
        # Commit the changes & close connection
        conn.commit()
        conn.close()

        # Add item to list
        # self.mylist.addItem(item)

        # Clear the item box after adding dish to list
        self.additem_blankbox.setText("")
        self.add_ing_blankbox.setText("")


    def delete(self):
        '''
        Delete Item From List
        '''

        # Grab the item from the list box
        item = self.additem_blankbox.text()

        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor

        cur = conn.cursor()
        del_query = 'DELETE FROM dishes_list WHERE dish_name=?'
        cur.execute(del_query, (item,))
        # Commit the changes & close connection
        conn.commit()
        conn.close()

        # Add item to list
        # self.mylist.addItem(item)

        # Clear the item box after adding dish to list
        self.additem_blankbox.setText("")

    def view(self):
        '''
        Observe Dishes
        '''
        # Warning box or Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Viewing Dishes")
        msg.setStyleSheet("QLabel{min-width: 200px;}");

        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM dishes_list")
        records = c.fetchall()

        # Commit the changes & close connection
        conn.commit()
        conn.close()

        # Blank dish list to hold dishes' names
        dish_lst = []
        ing_lst = []
        # Loop through the records and pull out each dish
        # records contains a list of tuples
        print(records)
        for record in records:
            dish_lst.append(record[0])
            ing_lst.append(record[1])
        
        dishes = [dish_lst[i] + ' - ' + ing_lst[i] for i in range(len(dish_lst))]
        print(dishes)
        dishes = '\n'.join(dishes)
        msg.setText(dishes)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def searching(self):
        '''
        Search dishes based on ingredients
        '''
        
        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM dishes_list")
        records = c.fetchall()

        # Commit the changes & close connection
        conn.commit()
        conn.close()

        # Blank dish list to hold dishes' names
        dish_lst = []
        ing_lst = []
        # Loop through the records and pull out each dish
        # records contains a list of tuples
        # print(records)
        for record in records:
            dish_lst.append(record[0])
            ing_lst.append(record[1])
        # key is ingredient, values a list of dish_names
        dct = defaultdict(list)

        ingredients = []
        for i, ing in enumerate(ing_lst):
            lst_ing = ing.split(',')
            for item in lst_ing:
                dct[item.lstrip().rstrip()].append(dish_lst[i])
        print(dct)
        ingredients = self.searching_blankbox.text()
        search_ing = ingredients.split(',')

        wanted_dish = set()
        # print(search_ing)
        for s_ing in search_ing:
            if s_ing in dct:
                # print(set(dct[s_ing]))
                wanted_dish = wanted_dish.union(set(dct[s_ing]))
                # print(wanted_dish)

            
        print(wanted_dish)


    def grab_all(self):
        '''
        Grab items from database        
        '''
        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT DISTINCT * FROM dishes_list")
        records = c.fetchall()

        # Commit the changes & close connection
        conn.commit()
        conn.close()

        # Iterate records and add to screen
        for record in records:
            self.mylist.addItem(str(record[0]))
    def clear_all(self):
        '''
        Clear All Dishes From List
        '''
        # self.mylist.clear()

        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("DELETE FROM dishes_list")
        records = c.fetchall()

        # Commit the changes & close connection
        conn.commit()
        conn.close()
    def save(self):
        '''
        Save To The Database
        '''
        # Create a database or connect to one
        conn = sqlite3.connect('dishes.db')
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the db table
        c.execute('DELETE FROM dishes_list;',)   
        
        # blank list to hold dishes
        dishes = []
        # Loop through the listWidget and pull out each item
        for idx in range(self.mylist.count()):
            dishes.append(self.mylist.item(idx))

        for item in dishes:
            # Add dish to the table
            c.execute("INSERT INTO dishes_list (dish_name) VALUES (:item)",
                {
                    'item': item.text(),
                })

        # Commit the changes & close connection
        conn.commit()
        conn.close() 

        # Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Database saved!!")
        msg.setText("Your Dishes Has Been Saved!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


    def retranslateUi(self, MainWindow):
        '''
        Set textboxes
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chef Cuisine Journey"))
        self.add_dish_pushButton.setText(_translate("MainWindow", "Add Dish To List"))
        self.view_list.setText(_translate("MainWindow", "View List"))
        self.delete_dish_pushButton.setText(_translate("MainWindow", "Delete Dish From List"))
        self.searching_dish.setText(_translate("MainWindow", "Search Dish From List"))
        self.clearall_pushButton.setText(_translate("MainWindow", "Clear Dishes"))
        
        # self.savedb_pushButton.setText(_translate("MainWindow", "Save To Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())