#new_test_pyfile
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Main import my_input, info_player, info_team, my_quit

#Test the inputs code
class TestMain(unittest.TestCase):


    # smoke test: valid inputs
    def test_correct_A(self):
        # select some valid inputs, for which the output is known
        self.assertEqual(info_player(), print("You chose to have more info about the volleyball player.\n"))
        
        # smoke test: valid inputs
    def test_correct_B(self):
        # select some valid inputs, for which the output is known
        self.assertEqual(info_team(), print("You chose to have more info about the volleyball team.\n"))
        
        # smoke test: valid inputs
    def test_correct_Q(self):
        # select some valid inputs, for which the output is known
        self.assertEqual(my_input(), print("You chose to quit the program.\n"))


# invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(info_player("C"), None)
        self.assertEqual(info_team("C"), None)
        self.assertEqual(my_quit("C"), None)
        self.assertEqual(info_player(7), None)
        self.assertEqual(info_team(7), None)
        self.assertEqual(my_quit(7), None)

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(<def_name>([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(info_player(""), None)
        self.assertEqual(info_team(""), None)
        self.assertEqual(my_quit(""), None)



if __name__ == '__main__':
    
    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)


