import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello(name1=None):
	if request.method == 'POST':
		if request.form['name1']:	
			name1 = request.form['name1']
		return render_template('hello.html', name1=name1)
	else:
		return render_template('form.html')