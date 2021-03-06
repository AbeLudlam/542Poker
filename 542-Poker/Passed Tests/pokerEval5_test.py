#writer Hezekiah
#Function: This file tests the eval5 function to make sure it properly selects the correct winner and handles ties. eval7 gives back a score for each given community + hand pool. The first 5 cards are the community, the last 2 are the players hand. Lower scores are better hands, with 0 being the best possible with a royal flush. Terminology: T = 10, J = Jack, Q = Queen, K = King, A = Ace, s = Spades, d = Diamonds, h = Hearts, c = clubs.

from poker import *

#This test is to make sure a pair of 10 is greater than a pair of 9
def test_eval5Pairs():
	player1 = ('2h', 'Ts', 'Tc', 'Td', '5h')
	player2 = ('5d', '9h', '9s', '9s', '4s')
	assert eval5(player1) < eval5(player2)

#This test is to make sure a three 9's beat a pair of 10 
def test_eval5Three():
	player1 = ('9h', '9d', '9s', '8c', '6h')
	player2 = ('Th', 'Td', '3s', '2c', '3h')
	assert eval5(player1) < eval5(player2)

#This test is to make sure that a straight beats three 9's
def test_eval5Flush():
	player1 = ('2h', '3h', '4d', '5c', '6s')
	player2 = ('9d', '9h', '9s', '6s', '5c')
	assert eval5(player1) < eval5(player2)
	
#This test is to make sure that a flush of spades beats a straight. 
def test_eval5Straight():
	player1 = ('2h', '3h', '4d', '5c', '6s')
	player2 = ('7s', '5s', '3s', '4s', '2s')
	assert eval5(player1) > eval5(player2)

#This test is to make sure that a royal flush of spades beats a royal straight of 10,J,Q,k,A.
def test_eval5Royal_Straight():
	player1 = ('Ts', 'Jh', 'Qd', 'Kc', 'As')
	player2 = ('As', 'Ks', 'Qs', 'Js', 'Ts')
	assert eval5(player1) > eval5(player2)

#This test is to make sure that A pair of 10 in one set is equal to pair of 10 in other set 
def test_eval5tie1():
	player1 = ('2h', '3s', 'Tc', 'Td', '2h')
	player2 = ('3d', '2h', 'Tc', 'Td', '2s')
	assert eval5(player1) == eval5(player2)

# This test is to make sure that three 9's plus kick is higher three 9's in other set.
def test_eval5tie2():
	player1 = ('2h', '3s', '9c', '9d', '9s')
	player2 = ('2s', '4d', '9c', '9d', '9s')
	assert eval5(player1) > eval5(player2)


#This test is to make sure that straight of hearts is equal to same value of spades.
def test_eval5Straight_tie():
	player1 = ('2h', '3h', '4h', '5h', '6h')
	player2 = ('6s', '2s', '4s', '3s', '5s')
	assert eval5(player1) == eval5(player2)

#This test is to make sure that a royal straight os spades is equal to royal straight of hearts.
def test_eval5royal_tie():
	player1 = ('As', 'Ks', 'Qs', 'Js', 'Ts')
	player2 = ('Ah', 'Kh', 'Qh', 'Jh', 'Th')
	assert eval5(player1) == eval5(player2)

#This test is to make sure that a pair of 9 and pair of T beats a pair of T.
def test_eval5Two_pairs():
	player1 = ('9h', '9c', 'Tc', 'Td', '6s')
	player2 = ('Ts', 'Ts', '3h', '4c', '2d')
	assert eval5(player1) < eval5(player2)
