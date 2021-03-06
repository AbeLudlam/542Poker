#Writer: Abraham Ludlam
#Function: This file tests the eval7 function to make sure it properly selects the correct winner and handles ties. eval7 gives back a score for each given community + hand pool. The first 5 cards are the community, the last 2 are the players hand. Lower scores are better hands, with 0 being the best possible with a royal flush. Terminology: T = 10, J = Jack, Q = Queen, K = King, A = Ace, s = Spades, d = Diamonds, h = Hearts, c = Clubs.
#Version: Uses Pytest 3.10.1

from poker import *

#All these tests are to make sure the hand rankings are working correctly. Most will test the next ranking from the winner of the last test, giving a clear hierarchy due to the scoring nature of the eval function.

#Test to make sure the ranking of the cards is evaluated correctly (Ex. 10 > 7) Here Ace should beat Queen
def test_eval7Rank():
	player1 = ('2d', '3h', '5s', '6c', '9h', 'As', 'Tc')
	player2 = ('2d', '3h', '5s', '6c', '9h', 'Qd', 'Jc')
	assert eval7(player1) < eval7(player2) 

#Test to make sure more pairs beat less pairs. Here a pair of 2's and 3's should beat a pair of Aces
def test_eval7Pairs():
	player1 = ('2d', '3h', '8s', '9c', 'Ah', '2s', '3c')
	player2 = ('2d', '3h', '8s', '9c', 'Ah', 'Qd', 'Ac')
	assert eval7(player1) < eval7(player2)

#Test to make sure a straight beats a 3 of a kind. Here a straight of 2,3,4,5,6 should beat 3 Aces
def test_eval7Straight():
	player1 = ('5d', '4h', '6s', '9c', 'Ah', '2s', '3c')
	player2 = ('5d', '4h', '6s', '9c', 'Ah', 'Ad', 'Ac')
	assert eval7(player1) < eval7(player2)

#Test to make sure flush beats straight. Here a flush of spades should beat a straight of 2,3,4,5,6
def test_eval7Flush():
	player1 = ('5s', '4s', '6s', '9c', 'Ah', '2h', '3c')
	player2 = ('5s', '4s', '6s', '9c', 'Ah', 'Js', 'Ts')
	assert eval7(player1) > eval7(player2)

#Test to make sure a full house beats a flush. Here a 3 of a kind of 4's and a pair of 2's should beat flush of clubs
def test_eval7Full():
	player1 = ('2c', '4c', '6s', '9c', '4h', '2h', '4c')
	player2 = ('2c', '4c', '6c', '9c', '4h', 'Jc', 'Tc')
	assert eval7(player1) < eval7(player2)

#Test to make sure a 4 of a kind beats a full house. Here a 4 of a kind of 7's should beat a full house.
def test_eval7Four():
	player1 = ('As', '4s', 'Ad', '9c', 'Ah', '2h', 'Ac')
	player2 = ('As', '4s', 'Ad', '9c', 'Ah', 'Jc', '9s')
	assert eval7(player1) < eval7(player2)

#Test to make sure a straight flush beats a 4 of a kind. Here a striaght flush of spades beats a 4 of a kind
def test_eval7StraightFlush():
	player1 = ('7s', '8s', 'Ts', 'Ks', 'Kh', 'Kd', 'Kc')
	player2 = ('7s', '8s', 'Ts', 'Ks', 'Kh', 'Js', '9s')
	assert eval7(player1) > eval7(player2)

#Test to make sure a royal flush beats a straight flush. 
def test_eval7Royal():
	player1 = ('7s', '2s', 'Td', 'Jd', 'Qd', 'Ad', 'Kd')
	player2 = ('7s', '2s', 'Td', 'Jd', 'Qd', '9d', '8d')
	assert eval7(player1) < eval7(player2)


#These tests are here to make sure eval7 is able to handle ties correctly.

#This test is here to make sure both players having a pair of aces is evaluated as a tie. 
def test_eval7PairTie():
	player1 = ('Ts', '8d', '7h', '5c', 'Ah', '2d', 'Ac')
	player2 = ('Ts', '8d', '7h', '5c', 'Ah', '3s', 'As')
	assert eval7(player1) == eval7(player2)


#Test to make sure a tie of 3 of a kind is decided by a Kicker. Here King beats Queen.
def test_eval7Kicker():
	player1 = ('9s', '4d', '6h', '6c', '7h', '6d', 'Kc')
	player2 = ('9s', '4d', '6h', '6c', '7h', '6s', 'Qs')
	assert eval7(player1) < eval7(player2)

#Test to make sure a flush of hearts tie, with  kicker interactions. Ace beats King
def test_eval7FlushTie():
	player1 = ('2h', '4h', '7h', '5c', 'Qc', 'Th', 'Ah')
	player2 = ('2h', '4h', '7h', '5c', 'Qc', '3h', 'Kh')
	assert eval7(player1) < eval7(player2)

#Test to make sure straight with same ending card is tied correctly, regardless of highest card. Here Ace does not beat King and the score is tied.
def test_eval7StraightTie():
	player1 = ('2s', '6d', '7h', '8c', '9h', 'Ad', 'Tc')
	player2 = ('2s', '6d', '7h', '8c', '9h', 'Ks', 'Ts')
	assert eval7(player1) == eval7(player2)



