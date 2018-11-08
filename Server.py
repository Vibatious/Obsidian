from flask import Flask
from flask import request
from flask import render_template
import base64
import cv2 as cv

app = Flask(__name__)


def conv_to_bin(number):
	"""Returns a list, binary equivalent of a number."""
	bytes = bin(number)
	list = []
	for i in range(2,len(bytes)):
		list.append(bytes[i])
	i = len(list)
	while i!=8:
		list.insert(0,'0')
		i = i+1
	return list

save_path = 'Res/'

@app.route('/')
def hello_world():
   return 'This is the obsidian server'

@app.route('/post_message',methods=['POST'])
def upload():
	print("POST Request recieved")

	message = request.form['message']
	BaseString = request.form['image']
	StegnoChoice = request.form['choice']

	imgdata = base64.b64decode(BaseString)
	image_filename = 'input_image.png'
	image_filename = save_path + image_filename
	with open(image_filename,'wb') as f:
		f.write(imgdata)

	message_filename = 'user_input.txt'
	message_filename = save_path + message_filename
	with open(message_filename,'w') as f:
		f.write(message)

	if(StegnoChoice == 'LSB-Linear'):
		import LSB_Linear
		LSB_Linear.main()
	if(StegnoChoice == 'LSB-Alternating'):
		import LSB_Linear_Ret
		LSB_Linear_Ret.main()

	return 'OK'

@app.route('/Return_Steg',methods=['GET'])
def Ret_Steg():
	sending_filename = 'steganographed_image.png'
	sending_filename = save_path + sending_filename
	im = open(sending_filename,'rb')
	str = base64.b64encode(im.read())
	return str 

@app.route('/Decode_Image',methods=['POST','GET'])
def decode_download():
	if request.method == 'POST':
		print('Evaluating POST request')
		BaseString = request.form['image']
		save_path = 'Res/'

		imgdata = base64.b64decode(BaseString)
		image_filename = 'steganographed_image.png'
		image_filename = save_path + image_filename
		with open(image_filename,'wb') as f:
			f.write(imgdata)
	else:
		print('Evaluating GET Request')
		userImage = cv.imread('Res/steganographed_image.png',1)
		pixel = userImage[0][0][0]
		to_bin = conv_to_bin(pixel)
		if(to_bin[len(to_bin)-2]=='0'):
			import LSB_Linear_Ret
			LSB_Linear_Ret.main()
		else:
			import LSB_Alter_Ret
			LSB_Alter_Ret.main()

		decoded = open("Res/decoded.txt","r")
		send = decoded.read()
		return send

	return 'OK'

if __name__ == '__main__':
   app.debug = False
   app.run(host= '0.0.0.0', port="5000")