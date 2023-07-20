from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/' , method=['GET', 'POST' ])  # '/' for the default page
def login():
	if request.method=='GET':
  	return render_template('login.html')
	 else :
  	name = request.form('username')
  	thepassword = request.form('password')

	  if name==username and password==thepassword:
	  	return render_template(url_for('home'))
	  else:
	  	return render_template('login.html')


@app.route('/home')
def home():
	return render_template('home.html', fff=facebook_friends)
	def fe(name):
		if name in facebook_friends:
			return render_template('friend_exists.html' , n=name , b=true)
		else:
			return render_template('friend_exists.html' , n=name , b=false)











@app.route('/friend_exists/>string:name' method=['GET', 'POST' ])













if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
