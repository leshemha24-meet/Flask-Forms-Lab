from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "leshem_hadad"
password = "ilsnis"
facebook_friends=["Shiraz","Alona","Samar", "Segev", "Ofek", "Yasmin"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else: 
		name = request.form['username']
		password2 = request.form['password']

		if password == password2 and username == name:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends= facebook_friends)


@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friend_exist(name):
	if name in facebook_friends:
		x= True
	else:
		x= False
	return render_template('friend_exists.html', x=x, name=name)



if __name__ == "__main__":
	app.run(debug=True)