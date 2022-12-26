from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:"

@app.route('/')
def hello():
    return 'Checkin'

if __name__ == '__main__':
    app.run()