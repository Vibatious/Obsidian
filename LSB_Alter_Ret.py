import cv2 as cv

height = 0
width = 0

def last(x):
	"""Return an integer value, the least significant bit of the argument."""
	x = bin(x)
	return x[len(x)-1]

def get_ascii(arr_list):
	"""Return a character, ascii equivalent of a number"""
	deci = 0
	for i in range(len(arr_list)):
		if arr_list[i] == '1':
			deci = deci + pow(2,len(arr_list)-i)

	return str(deci)
		
def getnext(list1,pos):
	"""Returns next character in message"""
	sum = 0
	k = 7
	for i in range(pos,pos+8):
		if list1[i]=='1':
			sum = sum+pow(2,k)
		k = k-1

	#print(chr(sum))
	return chr(sum)

def get_message_size():
	"""Determines the size of message"""
	file_obj = open("Res/user_input.txt","r")
	string = file_obj.readline()
	return len(string)

def write_To_File(message):
	"""Writes the decoded message to a file named Decoded.txt"""
	file_obj = open("Res/decoded.txt","w")
	file_obj.write(message)


def decode():
	"""main decoding logic"""
	steganoImage = cv.imread("Res/steganographed_image.png",1)
	height,width = steganoImage.shape[:2]

	message = ""

	column=0
	row=0
	color=0

	last_bits = []

	for row in range(height):
		for column in range(width):
			last_bits.append(last(steganoImage[row][column][color]))
			if (column+1)%width == 0:
				row = row+1
			column = (column+1)%width
			color = (color+1)%3
	
	message_size = get_message_size()
	i=0
	while True:
		nextChar = getnext(last_bits,i)
		if(nextChar == '`'):
			temp = getnext(last_bits,i)
			i = i+8
			temp2 = getnext(last_bits,i)
			if(temp == '`'):
				if(temp2 == '`'):
					break
			else:
				message+=temp
				message+=temp2
		message+=nextChar
		i = i+8
		
	write_To_File(message)

def main():
	decode()
	
if __name__ == '__main__':
	main()
