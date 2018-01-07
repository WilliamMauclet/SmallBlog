class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

def init_db(db):
    db.create_all()
    username = input("Admin username: ")
    password = input("Admin password: ")
    email = input("Admin email: ")
    admin = User(username=username, password=password, email=email)
    db.session.add(admin)
    db.session.commit()