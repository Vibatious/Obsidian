from flask import Flask
from flask import render_template
from flask import jsonify

#Application instace
app = Flask(__name__)

#a small memory databasse
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/',methods=['GET'])
def home():
   return render_template('Home.HTML')

@app.route('/all_Tasks',methods=['GET'])
def all():
	return jsonify(tasks)

if __name__ == '__main__':
   app.run(debug = True)