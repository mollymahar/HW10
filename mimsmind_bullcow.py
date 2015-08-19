def get_bullcow_renold_mahar(guess, rand_num):
    """Takes a guess as a string and a random number string, returns a tuple
    of bulls and cows as integers."""
    guess_s = list(guess)
	nbr_s = list(rand_num)

	# Calc bulls
	bulls = 0
	skip_index = [] 						# this will hold the indexes where the bulls appear
	for index in range(len(guess_s)):
		if guess_s[index] == nbr_s[index]:
			bulls += 1
			skip_index.append(index) 					# record indexes where the bulls are

	# Calc cows
	cows = 0
	for index2, num2 in enumerate(nbr_s): 						# check by nums in the answer
		for index1, num1 in enumerate(guess_s): 				# compare with nums in guess
			if (index1 in skip_index) or (index2 in skip_index): # Avoid counting bulls again
				continue
			if num1 == num2 and index1 != index2:
				cows += 1
				break
	return (bulls, cows)
