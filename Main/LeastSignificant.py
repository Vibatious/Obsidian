import cv2 as cv

def conv_to_bin(number):
	bytes = bin(number)
	list = []
	for i in range(2,len(bytes)):
		list.append(bytes[i])
	return list

def last(x):
	x = bin(x)
	return x[len(x)-1]

def make_even(list):
	i = len(list)
	while i!=8:
		list.append('0')
		i = i+1
	return list

def main():
	
	#raw image by user
	raw_image = cv.imread('../Res/input_image.png',1)

	#Getting image height and width
	height,width = raw_image.shape[:2]

	#User-message
	user_message = "I may not be superstitious but i am a little-stitious"
	#encoding the message to get bytes
	covertmsg = user_message.encode()
	end_marker = " ;;"

	user_message = user_message + end_marker
	i = 0
	j = 0
	k = 0

	for byteMessage in covertmsg:
		list = []
		list = conv_to_bin(byteMessage)
		list = make_even(list)
		
		for z in list:
			if z == '1':
				if last(raw_image[i][j][k]) == '0':
					raw_image[i][j][k] = raw_image[i][j][k] + 1
			else:
				if last(raw_image[i][j][k]) == '1':
					raw_image[i][j][k] = raw_image[i][j][k] - 1

			if (j+1)%width == 0:
				i = i+1
			j = (j+1)%width
			k = (k+1)%3

	#saving the changed image
	cv.imwrite('../Res/steganographed_image.png',raw_image)
		
if __name__ == '__main__':
	main()