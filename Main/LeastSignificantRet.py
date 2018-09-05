import cv2 as cv

height = 0
width = 0

def last(x):
	x = bin(x)
	return x[len(x)-1]

def get_ascii(arr_list):
	
	deci = 0
	for i in range(len(arr_list)):
		if arr_list[i] == '1':
			deci = deci + pow(2,len(arr_list)-i)

	return str(deci)

def end_check(image,i,j,k,width):
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

	if list1 == list2: 
		if ch1==';':
			if ch1 == ch2:
				return 1
	return 0
		

def get_char(image,i,j,k,width):
	
	list = []

	for c in range(8):
		list.append(last(image[i][j][k]))
		if (j+1)%width == 0:
			i = i+1
		j = (j+1)%width
		k = (k+1)%3

		ch = get_ascii(list)
		return ch,i,j,k


def getnext(list1,pos):
	sum = 0
	k = 7
	for i in range(pos,pos+8):
		if list1[i]=='1':
			sum = sum+pow(2,k)
		k = k-1

	return chr(sum)


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

	'''while end_check(steganoImage,i,j,k,width)!=1:
		ch,i,j,k = (get_char(steganoImage,i,j,k,width))
		message = message+ch
	'''

	list = []

	for i in range(height):
		for j in range(width):
			list.append(last(steganoImage[i][j][k]))
			if (j+1)%width == 0:
				i = i+1
			j = (j+1)%width
			k = (k+1)%3

	i=0
	file_obj = open("lett","r")
	string = file_obj.readline()
	ran = int(string)
	mark = 0
	#print(mark)
	while mark!=ran:
		if getnext(list,i) == ';':
			if getnext(list,i+8) == ';':
				return
		else:
			message+=getnext(list,i)
			i = i+8

		mark = mark+1


	print("decoded message is = {}".format(message))

if __name__ == '__main__':
	main()
