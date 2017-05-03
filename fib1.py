#Write a program to calculate fibonacci of user proved number

def fib(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fib(num-1) + fib(num-2)

def main():
	number = int(input("Enter a number: "))
	print(fib(number))

if __name__ == '__main__':
	main()