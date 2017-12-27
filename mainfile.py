from flask import Flask,request,render_template,sessions
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'logintest'
app.config['MONGO_URI'] = 'mongodb://localhost/logintest'
mongo = PyMongo(app)
@app.route('/')
def a():
    return render_template("index.html")

@app.route('/disp',methods=['GET','POST'])
def b():
    if request.method=="POST":
       name = request.form['name']
       age  = request.form['pasw']
    user = mongo.db.users
    user.insert({'username':name,'password':age})

    return 'welcome ' + request.form['name']

if __name__ =="__main__":
    app.run(debug=True)