# imports

# body

def seventeen():
	"""This function plays the marble game. It takes no arguments and calls two functions.
	It passes a string."""
	print "\nLet's play the game of Seventeen."
	marbles = 17
	turn = 1 										# designate turns to track winner easily
	result = None
	while marbles >= 1:
		print "Number of marbles left in the jar:", marbles
		if turn % 2 == 1:
			marbles -= human_turn(marbles) 			# iterate # marbles here to minimize repetition
		else:
			marbles -= computer_turn(marbles) 		# ditto as above
		turn += 1
	if marbles == 0:
		if turn % 2 == 0: 							# last player to play loses
			result = "\nThere are no marbles left. Computer wins!\n"
		else:
			result = "\nThere are no marbles left. You win!\n"
	print result

def human_turn(marbles):
	"""This function takes one integer argument and returns another integer."""
	while marbles >= 1:
		human = raw_input("\nYour turn. How many marbles will you remove (1-3)? ")
		try:
			human = int(human)
		except Exception:
			print "Invalid input. Try again."
			continue
		else:
			if human > marbles or human < 1 or human > 3:
				print "Sorry, that is not a valid option. Try again!"
				print "Number of marbles left in the jar:", marbles
				continue
			print "You removed", human, "marbles."
			return human

def computer_turn(marbles):
	"""This function takes one integer as an argument and returns an integer."""
	print "\nComputer's turn..."
	computer = 0
	if marbles > 3:
		computer = 3
	else:
		computer = 1
	print "Computer removed", computer, "marbles."
	return computer


# call main function
def main():
	seventeen()

if __name__ == '__main__':
	main()