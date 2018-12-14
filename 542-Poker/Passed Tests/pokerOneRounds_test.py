#Writer: Abraham Ludlam
#Function: This test set shows a stubbed out one_round5() so that its logic flow can be automatically tested. This is more of a demonstration of a stubbed out test set than a compelete test set. The complete test set would have stubbed out versions of one_round7 and one_round73, with 3 test cases for the former and 7 for the latter. We decided against doing this as the logic flow graphs already show their logic flow and the tests themselves are somewhat redundant.

from poker import *

#The stub bersion of one_round5. Here, the deck is an input called stubdeck and returns its expected output as exOut.
def stubone_round5(stubdeck):
    # shuffle a deck
    # draw two hands
    hand1 = stubdeck[:5]
    hand2 = stubdeck[5:10]
    # evaluate the hands
    score1 = eval5(hand1)
    score2 = eval5(hand2)
    # display the winning hand
    hand1 = '[%s]' % ' '.join(hand1)
    hand2 = '[%s]' % ' '.join(hand2)
    if score1 < score2:
        exOut = '%s beats %s' % (hand1, hand2)
    elif score1 == score2:
        exOut = '%s ties %s' % (hand1, hand2)
    else:
        exOut = '%s beats %s' % (hand2, hand1)
    return exOut

#This test verifies that the one_round5()'s logic is correct in declaring hand1 the winner.
def test_oneRound5Winner1():
	inp = ('2d', '3h', '5s', '2c', '2h', 'As', 'Tc', '5c', '6h', '9s')
	assert stubone_round5(inp) == '[2d 3h 5s 2c 2h] beats [As Tc 5c 6h 9s]'

#This test verifies that the one_round5()'s logic is correct in declaring hand2 the winner.
def test_oneRound5Winner2():
	inp = ( 'As', 'Tc', '5c', '6h', '9s', '2d', '3h', '5s', '2c', '2h')
	assert stubone_round5(inp) == '[2d 3h 5s 2c 2h] beats [As Tc 5c 6h 9s]'

#This test verifies that the one_round5()'s logic is correct in declaring a tie.
def test_oneRound5Tie():
	inp = ('Ac', 'Ts', '5h', '6c', '9d', 'As', 'Tc', '5c', '6h', '9s')
	assert stubone_round5(inp) == '[Ac Ts 5h 6c 9d] ties [As Tc 5c 6h 9s]'

	
