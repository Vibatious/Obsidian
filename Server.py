from flask import Flask
from flask import request
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World, i am vasu and this is the obsidian server yo'

@app.route('/post_message',methods=['POST'])
def message():
	print (request.form['message'])
	return 'OK'


if __name__ == '__main__':
   app.debug = False
   app.run(host= '0.0.0.0', port="5000")