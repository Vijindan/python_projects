import sys

def reverse(str):
	if len(str) <= 1:
		return str
	return reverse(str[1:]) + str[0]

while True:
	str = input("Enter a string to reverse or hit ENTER to exit: ")
	if str == "": sys.exit()
	print(reverse(str))