from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine


app = Flask(__name__, template_folder = 'templates/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/pythonassignment4'
db = SQLAlchemy(app)


engine = create_engine('postgresql://postgres:hashirama@localhost/pythonassignment4')


'''class Usser(db.Model):
    __tablename__ = 'usser'
    usserid = db.Column('usserid', db.Integer, primary_key=True)
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)


    def __init__(self,usserid,login,password):
        self.usserid = usserid
        self.login = login
        self.password = password


    loginn = ''
    passwordd = ''

    def tablefunc(id):
        with engine.connect() as connection:
            result = connection.execute(text("select login, password from usser where usser.usserid = "+str(id)))
            for row in result:
                global loginn, passwordd
                loginn = row['login']
                passwordd = row['password']
        connection.close()'''


class News(db.Model):
    __tablename__ = 'news'
    idcoin = db.Column('coin_id', db.Integer, primary_key=True)
    coin_name = db.Column('coin_name', db.Unicode)
    news1 = db.Column('news1', db.Unicode)
    news2 = db.Column('news2', db.Unicode)
    news3 = db.Column('news3', db.Unicode)
    news4 = db.Column('news4', db.Unicode)
    news5 = db.Column('news5', db.Unicode)
    news6 = db.Column('news6', db.Unicode)
    news7 = db.Column('news7', db.Unicode)
    news8 = db.Column('news8', db.Unicode)
    news9 = db.Column('news9', db.Unicode)
    news10 = db.Column('news10', db.Unicode)
    news11 = db.Column('news11', db.Unicode)
    news12 = db.Column('news12', db.Unicode)
    news13 = db.Column('news13', db.Unicode)
    news14 = db.Column('news14', db.Unicode)
    news15 = db.Column('news15', db.Unicode)
    news16 = db.Column('news16', db.Unicode)
    news17 = db.Column('news17', db.Unicode)
    news18 = db.Column('news18', db.Unicode)
    news19 = db.Column('news19', db.Unicode)
    news20 = db.Column('news20', db.Unicode)


    def __init__(self, idcoin, coin_name, news1, news2, news3,news4,news5,news6,news7,news8,news9,news10,news11,news12,news13,news14,news15,news16,news17,news18,news19,news20):
        self.idcoin = idcoin
        self.coin_name = coin_name
        self.news1 = news1
        self.news2 = news2
        self.news3 = news3
        self.news4 = news4
        self.news5 = news5
        self.news6 = news6
        self.news6 = news7
        self.news8 = news8
        self.news9 = news9
        self.news10 = news10
        self.news11 = news11
        self.news12 = news12
        self.news13 = news13
        self.news14 = news14
        self.news15 = news15
        self.news16 = news16
        self.news17 = news17
        self.news18 = news18
        self.news19 = news19
        self.news20 = news20


#db.create_all()

#new_inf = Usser(1,'harakiriboy','mypassword') 
#db.session.add(new_inf)
#db.session.commit()