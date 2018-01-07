import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\sqlitedbs\\smallblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        from init_db import init_db
        init_db(db)
    else:            
        print("The found users are: ")
        for user in User.query.all():
            print(user.username + " - " + user.email + "\n")
        # app.run(port=8000)

