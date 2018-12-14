from poker import *

#This test is to make sure two pairs beats as single pair. Here, pairs of 2's and 3's beats a pair of Aces
def test_eval5Pairs():
	player1 = ('2h', '3s', 'Ac', '3d', '2h')
	player2 = ('5d', 'Ah', 'As', '6s', 'Ts')
	assert eval5(player1) < eval5(player2)

#This test is to make sure a three of a kind beats a hand with 2 pairs. Here three 5's beats two pairs of 2's and 3's
def test_eval5Three():
	player1 = ('2h', '3s', 'Tc', '3d', '2h')
	player2 = ('5d', '9h', '6s', '5s', '5c')
	assert eval5(player1) > eval5(player2)

#This would be the format you would use to test the eval5 function. (T is 10)
#Tests I suggest doing:
#1. Make sure pair of 10's > pair of 9's
#2. Make sure three 9's > pair of 10's
#3. Make sure a flush of 5 spades > three 9's 
#4. Make sure straight of 2,3,4,5,6 > a flush of spades not in a straight
#5. Make sure a royal straight of spades > a non royal straight of 10, J, Q, K, A
#6-10. Do the tie case scenario of the ones above for the greater side (so tie case of #1 is two pairs on 10's, no highs)
