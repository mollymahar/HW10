import random

def get_randomdigit_mahar_renold(length):
	"""takes an integer of the length, returns a string with the number right-justified
	if it is less than the length"""
    # seed random with current time
    random.seed()
    range_end = 10 ** rand_len
    rand_n = random.randrange(0, range_end)
    return ljust(str(rand_n),length,"0") # right justify if number is < length