from flask import Flask
from flask import request
from flask import render_template
from base64 import decodestring
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World, i am vasu and this is the obsidian server'

@app.route('/post_message',methods=['POST'])
def message():
	message = request.form['message']
	BaseString = request.form['image']
	save_path = 'Res/'

	imgdata = base64.b64decode(BaseString)
	image_filename = 'input_image.png'
	image_filename = save_path + image_filename
	with open(image_filename,'wb') as f:
		f.write(imgdata)
	
	message_filename = 'user_input.txt'
	message_filename = save_path + message_filename
	with open(message_filename,'w') as f:
		f.write(message)

	return 'OK'


if __name__ == '__main__':
   app.debug = False
   app.run(host= '0.0.0.0', port="5000")