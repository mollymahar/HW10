# imports

# body
def seventeen():
	with open('seventeen2_output.txt', 'w') as fout:
		p1_plays = retrieve_p1_plays()
		play_sequence = {}
		p1_wins = 0 				# store values for number of wins per player
		p2_wins = 0
		# each game from p1 POV is saved as one key in the dictionary of p1 _plays
		for game, plays in p1_plays.items():
			play_sequence[game] = []
			marbles = 17 	# each game will start with 17 marbles
			p1 = 0
			p2 = 0
			winner = None
			# in each game, iterate among each play that p1 makes
			while marbles >= 1:
				for turn in plays:
					p1 = p1_turn(turn, marbles)
					play_sequence[game].append(str(p1))	
					marbles -= p1
					if marbles == 0:
						winner = "P2"
						p2_wins += 1
						break
					p2 = p2_turn(marbles)
					play_sequence[game].append(str(p2))
					marbles -= p2				
					if marbles == 0:
						winner = "P1"
						p1_wins += 1
						break
			fout.write("Game #" + str(game) + ". Play sequence: " + 
					'-'.join(play_sequence[game]) + ". Winner: "  + winner + "\n")
		fout.write("Player 1 won " + str(p1_wins) + " times. Player 2 won " +  str(p2_wins) + " times.")

def p1_turn(turn, marbles):
	p1 = 0
	if marbles < turn:
		p1 = marbles
	else:
		p1 = turn
	return p1

def p2_turn(marbles):
	p2 = 0
	if marbles > 3:
		p2 = 3
	elif marbles >= 1:
		p2 = 1
	return p2

def retrieve_p1_plays():
	p1_plays = {}
	with open('i206_placein_input_0.txt') as f:
		for index, game in enumerate(f):
			p1_plays[index + 1] = game.strip().split(",")
		for idx, val in p1_plays.items():
			p1_plays[idx] = [int(val) for val in p1_plays[idx]]
	return p1_plays


# call main function
def main():
	seventeen()

if __name__ == '__main__':
	main()