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
		list.insert(0,'0')
		i = i+1
	return list

def main():
	
	#raw image by user
	raw_image = cv.imread('../../Res/input_image.png',1)

	#Getting image height and width
	height,width = raw_image.shape[:2]

	#User-message
	user_message = "That concludes the Neural Logic Project. Some notes, the projects weights has been made manually for the sake of introducing the basic function of a perceptron, although optimization would be the best answer to find the correct weights for this problem, so that the neural network could correctly answer the problem if the inputs becomes larger.";
	covertmsg = user_message.encode()

	#user_message = user_message + end_marker
	print("The message is = {}".format(user_message))
	file_obj = open("lett","w")
	file_obj.write(str(len(user_message)))
	
	i = 0
	j = 0
	k = 0
	iterations = 0

	for byteMessage in covertmsg:
		#print(byteMessage)
		list = []
		list = conv_to_bin(byteMessage)
		list = make_even(list)
		#print(list,end=" ")
		#print("")
		
		for z in list:
			if z == '1':
				if last(raw_image[i][j][k]) == '0':
					raw_image[i][j][k] = raw_image[i][j][k] + 1
			else:
				if last(raw_image[i][j][k]) == '1':
					raw_image[i][j][k] = raw_image[i][j][k] - 1

			j = (j+1)%width
			k = (k+1)%3

			if j == 0:
				i = i+1
				if i == height:
					i = 0
					j = 0
					iteration = iteration+1
					k = iteration

	#saving the changed image
	cv.imwrite('../../Res/steganographed_image.png',raw_image)
		
if __name__ == '__main__':
	main()