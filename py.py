from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
 
app = Flask(__name__)

db_client = MongoClient('localhost', 27017)
db = db_client['tree_database']
tree = db['tree']

#user = ""
#password = ""

@app.route('/index/<name>', methods = ['POST', 'GET'])
def index(name):
		name = name.split('@')
		return render_template("index.html", name = name[0])

@app.route('/add', methods = ['POST', 'GET'])
def add():
		global tree
		global user

		if request.method == 'POST':

				rid = request.form['rid']
				tid = request.form['tid']
				tname = request.form['tname']
				sharea = request.form['sharea']

				tree_info = {}

				tree_info['rid'] = rid
				tree_info['tid'] = tid
				tree_info['tname'] = tname
				tree_info['sharea'] = sharea

				tree.insert_one(tree_info)

		if request.method == 'GET':
				rid = request.args.get('rid')
				tid = request.args.get('tid')
				tname = request.args.get('tname')
				sharea = request.args.get('sharea')

				tree_info = {}

				tree_info['rid'] = rid
				tree_info['tid'] = tid
				tree_info['tname'] = tname
				tree_info['sharea'] = sharea


				tree.insert_one(tree_info)

		return redirect(url_for('index', name = str(user)))

@app.route('/view', methods = ['POST', 'GET'])
def view():
		global tree

		data = [{}]

		for i in tree.find():
			data.append(i)

		return render_template("view.html", data = data);

@app.route('/login', methods = ['POST', 'GET'])
def login():
		global user

		if request.method == 'POST':
				user = request.form['user']

				return redirect(url_for('index', name = str(user)))

@app.route('/', methods = ['POST', 'GET'])
def login_view():
		return render_template("login.html");

if __name__ == '__main__':
    app.run(debug = True)
