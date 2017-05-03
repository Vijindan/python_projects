import sys

def pigLatin(str):
	return str[1:] + '-' + str[0] + "ay"

while True:
	str = input("Enter a word you'd like to conver to pig latin or ENTER to quit: ")
	if str=="": sys.exit()
	print(pigLatin(str))