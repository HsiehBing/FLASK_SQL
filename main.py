#main.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

#MySql database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:your.password@localhost:3306/testdb"
db = SQLAlchemy(app)

class Product(db.Model):
	__tablename__='linebot_test'
	pid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True, nullable=False)
	description = db.Column(db.String(255), nullable=False)
	insert_time = db.Column(db.DateTime, default=datetime.now)
	update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
	
	def __init__(self, name, description):
		self.name = name
		self.description = description



@app.route("/")
def index():
	#Create data
	db.create_all()
	return 'OK'

@app.route("/test")
def test():
	test1 = Product("MAX", "He is the bestdriver in the world")
	db.session.add(test1)
	db.session.commit()
	return "success"

@app.route("/test2")
def test2():
	test2 = Product("HAM", "He is the driver in the world")
	test3 = Product("LEC", "He is the saddest driver in the world")
	p =[test2, test3]
	db.session.add_all(p)
	db.session.commit()
	return "success"
@app.route("/showresult")
def test3():
	values = Product.query.all()
	printout = f''
	for item in values:
		printout =printout +(f"{item.pid} {item.name} {item.description} \n ")
	return (f"123\n 456 \n 789")
	#return printout
	


if __name__=="__main__":
	app.run(debug=True)
