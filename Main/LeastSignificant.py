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

def main():
	
	#raw image by user
	raw_image = cv.imread('../Res/input_image.png',1)

	#Getting image height and width
	height,width = raw_image.shape[:2]

	#User-message
	user_message = "vasu tomar"
	
	#encoding the message to get bytes
	covertmsg = user_message.encode()

	i=0
	j=0

	#Traversing through the byte array
	for k in range(len(covertmsg)):
		list = []
		list = conv_to_bin(covertmsg[k])
		for z in list:
			if z == 1:
				if last(raw_image[i][j][2]) == 0:
					raw_image[i][j][2] = raw_image[i][j][2] + 1
			else:
				if last(raw_image[i][j][2]) == 1:
					raw_image[i][j][2] = raw_image[i][j][2] - 1
			j = j+1
			if j == width:
				j = 0
				i = i+1

	#saving the changed image
	cv.imwrite('../Res/stegnographed_image.png',raw_image)
		
if __name__ == '__main__':
	main()