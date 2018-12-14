#Originally project from here https://github.com/fogleman/Poker
#New authors: Abraham Ludlam and Hezekiah Pilli
#This code evaluates poker hands for 5 and 7 card poker. We added the functionality of 3 player 7 card poker and providing a UI for the user to interact with to run the evaluation functions as much as they want.
#Old code written: Global variables, hash function, eval5, eval7, one_round5, one_round7.
#New code written: one_round73, use_eval()

from poker_data import *
import itertools
import random

#Set up the deck for use for the program. Also set up primes for use in the evaluation process.
_SUITS = [1 << (i + 12) for i in range(4)]
_RANKS = [(1 << (i + 16)) | (i << 8) for i in range(13)]
_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
_DECK = [_RANKS[rank] | _SUITS[suit] | _PRIMES[rank] for rank, suit in 
    itertools.product(range(13), range(4))]

SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = [''.join(s) for s in itertools.product(RANKS, SUITS)]
LOOKUP = dict(zip(DECK, _DECK))


#Original code, I only know it helps with the eval(5) function in returning a score. 
def hash_function(x):
    x += 0xe91aaa35
    x ^= x >> 16
    x += x << 8
    x &= 0xffffffff
    x ^= x >> 4
    b = (x >> 8) & 0x1ff
    a = (x + (x << 2)) >> 19
    r = (a ^ HASH_ADJUST[b]) & 0x1fff
    return HASH_VALUES[r]

#This function evaluates a 5 card poker hand. Original code, can't comment more on.
def eval5(hand):
    c1, c2, c3, c4, c5 = (LOOKUP[x] for x in hand)
    q = (c1 | c2 | c3 | c4 | c5) >> 16
    if (0xf000 & c1 & c2 & c3 & c4 & c5):
        return FLUSHES[q]
    s = UNIQUE_5[q]
    if s:
        return s
    p = (c1 & 0xff) * (c2 & 0xff) * (c3 & 0xff) * (c4 & 0xff) * (c5 & 0xff)
    return hash_function(p)


#Original code. Uses the eval5 function on all 5 card combinations of the inputted 7 cards. 
def eval7(hand):
    return min(eval5(x) for x in itertools.combinations(hand, 5))

#Demonstrates the use of the eval5 function by comparing 2 randomly generated hands. Shows that either hand 1 wins,hand 2 wins, or the hands are tied.
def one_round5():
    # shuffle a deck
    deck = list(DECK)
    random.shuffle(deck)
    # draw two hands
    hand1 = deck[:5]
    hand2 = deck[5:10]
    # evaluate the hands
    score1 = eval5(hand1)
    score2 = eval5(hand2)
    # display the winning hand
    hand1 = '[%s]' % ' '.join(hand1)
    hand2 = '[%s]' % ' '.join(hand2)
    if score1 < score2:
        print '%s beats %s' % (hand1, hand2)
    elif score1 == score2:
        print '%s ties %s' % (hand1, hand2)
    else:
        print '%s beats %s' % (hand2, hand1)

#Shows the evaluation of two randomly generated 7 card hands (5 from the community pool and 2 for each player). Will display if hand 1 wins, hand 2 wins, or the two hands are tied.
def one_round7():
    # shuffle a deck
    deck = list(DECK)
    random.shuffle(deck)
    # draw community and two hands
    community = deck[:5]
    hand1 = deck[5:7]
    hand2 = deck[7:9]
    
    # evaluate the hands
    score1 = eval7(community + hand1)
    score2 = eval7(community + hand2)
    # display the winning hand
    community = '[%s]' % ' '.join(community)
    hand1 = '[%s]' % ' '.join(hand1)
    hand2 = '[%s]' % ' '.join(hand2)
    print community
    if score1 < score2:
        print '%s beats %s' % (hand1, hand2)
    elif score1 == score2:
        print '%s ties %s' % (hand1, hand2)
    else:
        print '%s beats %s' % (hand2, hand1)
    print

#Shows the evaluation of three randomly generated 7 card poker hands (5 from the community pool and 2 for each players' hand). Will display that hand 1 wins, hand 2 wins, hand 3 wins, all hands are tied, hand 1 and hand 2 tied, hand 1 and hand 3 tied, or hand 2 and hand 3 tied.
def one_round73():
	# shuffle a deck
    deck = list(DECK)
    random.shuffle(deck)
    # draw community and two hands
    community = deck[:5]
    hand1 = deck[5:7]
    hand2 = deck[7:9]
    hand3 = deck[9:11]
  
   
   # print ina[1]
   
    # evaluate the hands
    score1 = eval7(community + hand1)
    score2 = eval7(community + hand2)
    score3 = eval7(community + hand3)
    # display the winning hand
    community = '[%s]' % ' '.join(community)
    hand1 = '[%s]' % ' '.join(hand1)
    hand2 = '[%s]' % ' '.join(hand2)
    hand3 = '[%s]' % ' '.join(hand3)
    print community
    # more if statements necessary to determine winner
    if (score1 < score2) & (score1 < score3):
        print '%s beats %s and %s' % (hand1, hand2, hand3)
    elif (score2 < score1) & (score2 < score3):
	 print '%s beats %s and %s' % (hand2, hand1, hand3)
    elif (score3 < score1) & (score3 < score2):
	 print '%s beats %s and %s' % (hand3, hand1, hand2)
    elif (score1 == score2) & (score1 == score3):
        print '%s ties %s and %s' % (hand1, hand2, hand3)
    elif score1 == score2:
        print '%s ties %s' % (hand1, hand2)
    elif score1 == score3:
        print '%s ties %s' % (hand1, hand3)
    elif score3 == score2:
        print '%s ties %s' % (hand3, hand2)
		
   
#This function allows the user to choose which evaluation comparison they want to run, all while looping till the user wants to exit.
def use_eval():
	#run is to make sure the program loops, loop_7 performs the same function for 7 card evaluations.
	run = 1
	
	print '\nThis program performs evaluations on poker hands for 5 card or texas holdem poker games'
	while run:
		#get the input of the user into inp. 
		print '\nPress 1 for a five card evaluation, 2 for a seven card evaluation, and 3 to quit'
		inp = raw_input()
		#5 card eval for 2 players
		if inp == '1':
			one_round5()
		#7 card eval loop begins, user must choose whether to evaluate hands for 2 or 3 players.
		elif inp == '2':
			loop_7 = 1
			while loop_7:
				#second input into in7 for 7 card hands
				print '\nPress 1 for two players or 2 for three players'
				in7 = raw_input()
				#7 card eval for 2 players
				if in7 == '1':
					one_round7()
					loop_7 = 0
				#7 card eval for 3 players
				elif in7 == '2':	
					one_round73()
					loop_7 = 0
				#Loop to beginning if input is not valid
				else:
					print '\nInvalid input, try again'
		#Quit the program
		elif inp == '3':
			run = 0
		#loop to beginning if input not valid
		else:
			print '\nInvalid input, try again'
	

if __name__ == '__main__':
     #run the program
	use_eval()
	
