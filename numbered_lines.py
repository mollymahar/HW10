def num_lines():
	with open('small.txt') as f:
		with open('new.txt', 'w') as f2:
			for index, line in enumerate(f):
				f2.write(str(index + 1) + " " + line.strip() + "\n")

def main():
	num_lines()

if __name__ == '__main__':
	main()