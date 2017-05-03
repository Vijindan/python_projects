import sys

def palindrome(str):
	# return str == str[::1] #Pythonic way of determing palindrome
	strhalf = len(str)//2 #integer division '/' returns float, use '//' for floor div
	for i in range(strhalf):
		if str[i] != str[len(str)-1-i]:
			return False
	return True


while True:
	str = input("Enter a string to be checked if its a palindrome or hit ENTER to quit: ")
	if str=="": sys.exit()
	print(palindrome(str))