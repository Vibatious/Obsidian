import cv2 as cv 
import numpy

def str_to_bin(num):
	b = bin(num)
	list = [];
	for i in range(2,len(b)):
		list.append(b[i])
	return list
def img_to_bin(i):
	i = bin(i)
	return i[-1]


def main():
	input_img = input("Enter the file name: ")
	img = cv.imread(input_img)
	user_msg = input("Enter cover message:- \t")
	encode_msg = user_msg.encode()

	i = 0
	j = 0
	k = 0 
	for msg in encode_msg:
		lst = []
		lst = str_to_bin(msg)
		print(lst)
		for z in lst :
			print("Before")
			print(z,i,j,k,img_to_bin(img[i][j][k]))
			if(z == "1"):
				if(img_to_bin(img[i][j][k]) == "0"):
					img[i][j][k] = img[i][j][k] + 1
			else:
				if(img_to_bin(img[i][j][k]) == "1"):
					img[i][j][k] = img[i][j][k] - 1
			print("After")
			print(z,i,j,k,img_to_bin(img[i][j][k]))
		
			j=j+1
			k=k%3

	out_img = input("Enter the output file name: ")
	cv.imwrite(out_img,img)
if __name__ == '__main__':
	main()

