Project done by: Abraham Ludlam and Hezekiah Pilli
Contact: LudlamAbraham@csu.fullerton.edu
	 HezekiahPilli@csu.fullerton.edu

Software Used: Python 2.7.6
	       Pytest 3.10.1
               Python's unittest Framework

Github: https://github.com/AbeLudlam/542Poker

The original program was found here: (https://github.com/fogleman/Poker). This is a Python Implementation of Cactus Kev's Poker Hand Evaluator (http://www.suffecool.net/poker/evaluator.html). It does evaluations for 5 and 7 card poker hands, where it provides a score for the hand. The lower the score, the better hand, with a Royal Flush with the lowest score of '0'. It has functions to display which of the two randomly generated hands won. We expanded it to have a three player evaluation of 7 card texas hold'em style poker and an interactive interface for the user to run any of the evaluations as much as he wants. 

To run the program (poker.py), Python 2.7.6 was used in a Linux Ubuntu system and this command was used to run it from the command line: "python ./poker.py". poker.py requires poker_data.py to perform the evaluations needed

For the tests, we used Pytest 3.10.1 to perform the tests. For the evaluations, we used equivalence class testing to categorize the ranking of the different types of hands and to limit the number of tests. If we were to test every single hand combination for both evaluations functions, there would be over a trillion test cases. By utilizing equivalence class partioning and testing, we limited the number of tests for both functions to just above 20 test cases. These files are 'pokerEval5_test.py' and 'pokerEval7_test.py'

We also had quality tests to make sure the evaluation functions are not handing scores for invalid hands that have two or more of the same card. Currently these tests fail, as this functionality is not implemented for the eval5() and eval7(). This is 'pokerHandCheck_test.py'.

For the functions that display the result of the random evaluations, we had to use a stubbed out version of the functions. Because of this, we decided to only show one of these stubbed versions as these tests felt very redundant at testing logic flow. In return, we made logic flow graphs for all three of the display functions (one_round() functions). This is file is 'pokerOneRounds_test.py'

We also wanted to automatically test the input of the use_eval function, but found out that the way we handled input was not easy to test. We decided to show a mock file to show how we would handle doing mock inputs if we changed the original code. This uses parts of Python's unittest framework for its mock behavior. This is 'MOCK_pokerInput_MOCKTEST.py'

To run all tests, simply go to the directory in command line where the project is stored, usually the 'Poker' directory. Then simply type "pytest" and it will run all tests in directory and subdirectories.

To run all passed tests, type "pytest Passed\ Tests"

To run all failed tests, type "pytest Failed\ Tests"

If you want to run an individual test, such as 'pokerEval7_test.py', you would type in the format as "pytest Passed\ Tests/pokerEval7_test.py"
