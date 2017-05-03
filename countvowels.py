import sys

def countVowels(str):
	vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
	for c in str:
		if c in vowels:
			vowels[c] +=1
	return vowels

while True:
	str = input("Enter the string to count its vowels or hit ENTER to quit: ")
	if str=="": sys.exit()
	vowels = countVowels(str)
	print("Count of a: ", vowels['a'])
	print("Count of e: ", vowels['e'])
	print("Count of i: ", vowels['i'])
	print("Count of o: ", vowels['o'])
	print("Count of u: ", vowels['u'])
	print ("Total sum of vowels is: ",  vowels['a']+
		vowels['e']+vowels['i']+vowels['o']+vowels['u'])