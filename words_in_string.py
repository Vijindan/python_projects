import sys
import string

def countwords(textfile):
	#empty word dictionary
	word_dict = {}

	#open and read file contents
	with open(textfile, 'r') as f:
		contents = f.read()

	#trim spaces and punctuation and put into list
	words = [word.strip(string.punctuation) for word in contents.split()]

	#populate word dictionary
	for word in words:
		if word not in word_dict: 
			word_dict[word] = 1
		else: 
			word_dict[word] += 1

	for key in word_dict:
		print("The word", key, "appears", word_dict[key], "time(s)")

def main():
	countwords(sys.argv[1])


if __name__ == '__main__':
	main()