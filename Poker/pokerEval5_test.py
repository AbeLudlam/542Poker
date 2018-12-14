from poker import *

def test_answer():
	usef = ('Kh', 'Qh', 'Ah', 'Ah', 'Th')
	useg = ('Ks', 'Qs', 'As', 'As', 'Ts')
	# First call eval5()
	user_1 = eval5(usef)
	user_2 = eval5(useg) 
	#assert eval5(usef) == eval5(useg)
	if  "Royal Straight Spades" in user_1 or "Royal Straight Spades" in user_2:
		if "Royal Straight Spades" in user_1 and "Royal Straight Spades" in user_2:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		if "Royal Straight Spades" in user_1:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Player 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif "Straight" in user_1 or "Straight" in user_2:
		if "Straight" in user_1 and "Straight" in user_2:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		if "Straight" in user_1:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif "Flush" in user_1 or "Flush" in user_2:
		if "Flush" in user_1 and "Flush" in user_2:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif "Flush" in user_1:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif  "3" in user_1 or "3" in user_2:
		if "3" in user_1 and "3" in user_2:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif "3" in user_1:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif  "2" in user_1 or "2" in user_2:
		if "2" in user_1 and "2" in user_2:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif "2" in user_1:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif user[-3] == "A" or user[-3] == "A":
		if  user[-3] == "A" and user[-3] == "A":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif user[-3] == "A":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif user[-3] == "K" or user[-3] == "K":
		if  user[-3] == "K" and user[-3] == "K":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif user[-3] == "K":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif user[-3] == "Q" or user[-3] == "Q":
		if  user[-3] == "Q" and user[-3] == "Q":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif user[-3] == "Q":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif user[-3] == "J" or user[-3] == "J":
		if  user[-3] == "J" and user[-3] == "J":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif user[-3] == "J":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	elif user[-3] == "T" or user[-3] == "T":
		if  user[-3] == "T" and user[-3] == "T":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"Tie")
		elif user[-3] == "T":
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 1")
		else:
			return ("Player 1 have: {}".format(user_1),
					"Player 1 have: {}".format(user_2),
					"The winner is Palyer 2")
	else:
		return "Tie"

#This would be the format you would use to test the eval5 function. (T is 10)
#Tests I suggest doing:
#1. Make sure pair of 10's > pair of 9's
#2. Make sure three 9's > pair of 10's
#3. Make sure a flush of 5 spades > three 9's 
#4. Make sure straight of 2,3,4,5,6 > a flush of spades not in a straight
#5. Make sure a royal straight of spades > a non royal straight of 10, J, Q, K, A
#6-10. Do the tie case scenario of the ones above for the greater side (so tie case of #1 is two pairs on 10's, no highs)

def get_face_card(cards):
	'''
		Return list of Face value of user cards
	'''
	cards_with_face_vale = []
	card1 = cards[0][0]
	card2 = cards[0][0]
	card3 = cards[0][0]
	card4 = cards[0][0]
	card5 = cards[0][0]
	cards_with_face_vale.extend([card1])
	cards_with_face_vale.extend([card2])
	cards_with_face_vale.extend([card3])
	cards_with_face_vale.extend([card4])
	cards_with_face_vale.extend([card5])
	return cards_with_face_vale

def get_suit_card(cards):
	'''
		Return list cards suit of user cards
	'''
	cards_with_suit_vale = []
	card1 = cards[0][1]
	card2 = cards[0][1]
	card3 = cards[0][1]
	card4 = cards[0][1]
	card5 = cards[0][1]
	cards_with_suit_vale.extend([card1])
	cards_with_suit_vale.extend([card2])
	cards_with_suit_vale.extend([card3])
	cards_with_suit_vale.extend([card4])
	cards_with_suit_vale.extend([card5])
	return cards_with_suit_vale

def convert_all_to_int(cards):
	for index,single_card in enumerate(cards):
		if single_card == 'A':
			cards[index] = 14
		if single_card == 'K':
			cards[index] = 13
		if single_card == 'Q':
			cards[index] = 12
		if single_card == 'J':
			cards[index] = 11
		if (single_card != 'A' and 
			single_card != 'K' and 
			single_card != 'J' and
			single_card != 'Q'):
			cards[index] = int(single_card)
	return cards

def check_sequnce(cards_value):
	'''
		Will return wheather cards are in sequnce or not
	'''
	cards_value.sort()
	if cards_value[0] - cards_value[-1] == 4:
		return cards_value
	else:
		return False

def check_pair(cards):
	'''
		This Function will return paired cards
	'''
	cards.sort() 
	new_list = sorted(set(cards))
	dup_list =[]
	for i in range(len(new_list)):
			if (cards.count(new_list[i]) > 1 ):
				dup_list.append(new_list[i])
	return dup_list

def royal_straight(cards):
	'''
		This cards will return cards are Royal Straight or not
	'''
	if cards[-1] == 14:
		return True

def eval5(user_cards):
	'''
		This function will return high priority cards
	'''
	cards_with_face_vale = get_face_card(user_cards)
	cards_values_int = convert_all_to_int(cards_with_face_vale)
	cards_in_sequnce = check_sequnce(cards_values_int)
	paired_cards = check_pair(cards_values_int)
	if cards_in_sequnce:
		if check_royal_staight(cards_in_sequnce):
			suit_value = list(set(get_suit_card(user_cards)))
			if len(suit_value) == 1:
				if suit_value[0] == 's':			
					return ("Royal Straight Spades")
				if suit_value[0] == 'h':			
					return ("Royal Straight Hearts")
				if suit_value[0] == 'd':			
					return ("Royal Straight Diamonds")
				if suit_value[0] == 'c':			
					return ("Royal Straight Clubs")
			else:
				return ("A non royal straight")
		else:
			return "Straight"
	elif not cards_in_sequnce:
		suit_value = list(set(get_suit_card(user_cards)))
		if len(suit_value) == 1:
			if suit_value[0] == 's':			
				return ("Flush of Spades")
			if suit_value[0] == 'h':			
				return ("Flush of Hearts")
			if suit_value[0] == 'd':			
				return ("Flush of Diamonds")
			if suit_value[0] == 'c':			
				return ("Flush of Clubs")
	
		elif paired_cards:
			no_repeated = len(paired_cards)
			card = paired_cards[0]
			if card == 14:
				return ("{} A's".format(no_repeated))
			elif card == 13:
				return ("{} K's".format(no_repeated))
			elif card == 12:
				return ("{} Q's".format(no_repeated))
			elif card == 11:
				return ("{} J's".format(no_repeated))
			else:
				return ("{} {}'s".format(no_repeated,card))
		else:
			cards_with_face_vale.sort()
			return cards_with_face_vale[-1]
		

			

