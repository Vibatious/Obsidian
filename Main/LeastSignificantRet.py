import cv2 as cv

height = 0
width = 0

def last(x):
	x = bin(x)
	return x[len(x)-1]

def get_ascii(arr_list):
	
	deci = 0
	for i in len(arr_list):
		deci = deci+pow(2,len(arr_list)-i)

	return str(deci)

def end_check(image,i,j,k):
	list1 = []
	list2 = []

	for c in range(8):
		list1.append(last(image[i][j][k]))
		if (j+1)%width == 0:
			i = i+1
		j = (j+1)%width
		k = (k+1)%3
	for c in range(8):
		list2.append(last(image[i][j][k]))
		if (j+1)%width == 0:
			i = i+1
		j = (j+1)%width
		k = (k+1)%3
	
	ch1 = get_ascii(list1)
	ch2 = get_ascii(list2)

	if cmp(list1,list2): 
		if ch1==';':
			if ch1 == ch2:
				return 1
	return 0
		

def get_ascii(image,i,j,k):
	
	list = []

	for c in range(8):
		list.append(last(image[i][j][k]))
		if (j+1)%width == 0:
			i = i+1
		j = (j+1)%width
		k = (k+1)%3

		ch = get_ascii(list)
		return ch,i,j,k


def main():
	#generated Steganographed image
	steganoImage = cv.imread("../Res/steganographed_image.png",1)

	#getting height and width of image
	height,width = steganoImage.shape[:2]

	#Decoded message
	message = ""

	i=0
	j=0
	k=0

	while end_check(steganoImage,i,j,k)!=1:
		ch,i,j,k = message.append(get_char(steganoImage,i,j,k))
		message.append(ch)

	print(message)

if __name__ == '__name__':
	main()