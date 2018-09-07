import cv2 as cv

height = 0
width = 0

def last(x):
	x = bin(x)
	return x[len(x)-1]

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
	steganoImage = cv.imread("../../Res/steganographed_image.png",1)

	#getting height and width of image
	height,width = steganoImage.shape[:2]

	#Decoded message
	message = ""

	i=0
	j=0
	k=0

	list = []
	
	for i in range(height):
		for j in range(width):
			list.append(last(steganoImage[i][j][k]))
			if (j+1)%width == 0:
				i = i+1
				if i == height:
					i = 0
					k = k+1
			j = (j+1)%width

	i=0
	file_obj = open("lett","r")
	string = file_obj.readline()
	ran = int(string)
	mark = 0
	#print(mark)
	while mark!=ran:
		message+=getnext(list,i)
		i = i+8
		mark = mark+1

	print("decoded message is = {}".format(message))

if __name__ == '__main__':
	main()
