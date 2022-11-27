from datetime import datetime
from flask import Flask, render_template, request
from . import app
import mysql.connector

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/Register", methods = ['POST','GET'])
def register():
	print("Inside register ")
	conn = mysql.connector.connect(host="project1.c0vqwtm66cva.us-east-1.rds.amazonaws.com",user="admin",password = "Secret55", database="project_db")
	cursor = conn.cursor()
	msg = ''
	msgcolor=''
	if(request.method=='POST'):
		try:
			print("post called")
			id = request.form.get('id')
			name = request.form.get('name')
			address = request.form.get('address')
			dob = request.form.get('dob')
			phone = request.form.get('phone')
			print(id,name,address,dob,phone)
			insert_query = """INSERT INTO employee VALUES(%s,%s,%s,%s,%s)"""  
			recordTuple = (id,name, address, dob, phone)
			cursor.execute(insert_query, recordTuple)
			conn.commit()
			print("1 row inserted!!!")
			msg = 'Data inserted Successfully'
			msgcolor='success'
		except:
			conn.rollback()
			msgcolor='danger'
			msg = 'The Entry is already present!! \n or you have exceeded the data limit in a feild.'
	conn.close()
		
	return render_template('Registeremployee.html',msg = msg,msgcolor=msgcolor)

@app.route("/Update", methods =["POST","GET"])
@app.route("/Update/<string>", methods =["POST","GET"])
def update(string=""):
	msg = ''
	msgcolor=''
	
	conn = mysql.connector.connect(host="project1.c0vqwtm66cva.us-east-1.rds.amazonaws.com",user="admin",password = "Secret55", database="project_db")
	cursor = conn.cursor()
	retrive_query = """SELECT * FROM employee"""  
	cursor.execute(retrive_query)
	result=cursor.fetchall()

	if request.method =="POST" and string=="":
		try:
			id = request.form.get('id')
			name = request.form.get('name')
			address = request.form.get('address')
			dob = request.form.get('dob')
			phone = request.form.get('phone')

			query = """UPDATE employee SET empId=%s,empName =%s, empAddress=%s, empDob=%s,empPhone=%s WHERE empId=%s """	
			recordTuple = (id,name, address, dob, phone,id)
			cursor.execute(query,recordTuple)
			conn.commit()
			msg = 'The Details have been updated'
			msgcolor='success'
	
			print("Value updated!!!")
		except:
			conn.rollback()
			msg = 'Some error occured! Unable to update the details'
			msgcolor='danger'
	
			return render_template('Updateemployee.html',posts = result,msg = 'danger')
	print('Record updated successfully...')  
	return render_template('Updateemployee.html',posts = result,msg =msg, msgcolor=msgcolor)


@app.route("/View", methods=['POST','GET'])
def view():
	msg = ''
	msgcolor=''
	
	print("Inside register ")
	conn = mysql.connector.connect(host="project1.c0vqwtm66cva.us-east-1.rds.amazonaws.com",user="admin",password = "Secret55", database="project_db")
	cursor = conn.cursor()
	retrive_query = """SELECT * FROM employee""" 
	cursor.execute(retrive_query)
	result=cursor.fetchall()
	print("Result :", result)
	result1 = []

	count_query = """SELECT COUNT(empId) FROM employee""" 
	cursor.execute(count_query)
	count=cursor.fetchall()

	
	if request.method == 'POST':	
		val = request.form.get('query')
		category = request.form.get('select')
		print(val)
		print(category)
		if category.lower() == 'id':
			print("in search category id")
			id = val
			tup = (id,)
			query = """ SELECT * FROM employee WHERE empId=%s """  
			cursor.execute(query,tup)
			result1 = cursor.fetchall()
			count_query = """SELECT COUNT(empId) FROM employee""" 
			cursor.execute(count_query)
			count=cursor.fetchall()

			if len(result1)==0:
				msg = 'No Match Found!!!'
				msgcolor='danger'
				

			print("ID found is :",result1)
			return render_template('Viewemployee.html', results = result,count=count,SearchResults =result1, display = True,msg=msg,msgcolor=msgcolor)
		
		elif category.lower() == 'age':
			print("in search category age")
			age = val
			tup = (age,)
			query = """ SELECT * FROM employee WHERE DATEDIFF(CURDATE(), empDob)/365 > %s """  
			cursor.execute(query,tup)
			result1 = cursor.fetchall()
			count_query = """SELECT COUNT(empId) FROM employee""" 
			cursor.execute(count_query)
			count=cursor.fetchall()

			if len(result1)==0:
				msg = 'No Match Found!!!'
				msgcolor='danger'
			
			return render_template('Viewemployee.html',count=count, results = result,SearchResults =result1, display = True,msg=msg,msgcolor=msgcolor)
		
		elif category.lower() == 'letter':
			print("in search category letter")
			name = val+'%'
			print(name)
			tup = (name,)
			query = "SELECT * FROM employee WHERE empName like %s "
			cursor.execute(query,tup)
			result1 = cursor.fetchall()
			count_query = """SELECT COUNT(empId) FROM employee""" 
			cursor.execute(count_query)
			count=cursor.fetchall()

			if len(result1)==0:
				msg = 'No Match Found!!!'
				msgcolor='danger'
			
			print('Result is here :',result1)
			return render_template('Viewemployee.html',count=count, results = result,SearchResults =result1, display = True,msg=msg,msgcolor=msgcolor)
		else:
			msg = 'No match found!!!'
			msgcolor='danger'
			return render_template('Viewemployee.html',count=count, results = result,SearchResults =result1, display = True)
	conn.close()
	return render_template('Viewemployee.html', results = result,SearchResults =result1,count=count, display = False)
	

@app.route("/Delete", methods=['POST','GET'])
def delete():
	conn = mysql.connector.connect(host="project1.c0vqwtm66cva.us-east-1.rds.amazonaws.com",user="admin",password = "Secret55", database="project_db")
	cursor = conn.cursor()
	msg = ''
	msgcolor=''
	if(request.method=='POST'):
		try:
			retrive_query = """SELECT * FROM employee"""  
			cursor.execute(retrive_query)
			result=cursor.fetchall()		
	
			id =int(request.form.get('id'))
			print(id)
			print(result)
			for i in result:
				if id not in i:
					flag = True
				else:
					flag = False
					break
			
			if flag == True:
				msg='No employee Found with such id!!!'
				msgcolor = 'danger'
			else:
				msg = 'Details deleted succesfully'
				msgcolor = 'success'

			tup = (id,)
			query = """ DELETE FROM employee WHERE empId like %s """  
			cursor.execute(query,tup)
			conn.commit()
			
		except:
			conn.rollback()
			msg = 'An Error Occured!!!.'
			msgcolor = 'danger'
		conn.close()
	return render_template('Deleteemployee.html',msg=msg,msgcolor=msgcolor)

