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
        self.assertEqual(my_quit(), print("You chose to quit the program.\n"))

        # false values
    def test_false_values(self):
        self.assertFalse(info_player(), None)
        self.assertFalse(info_team(), None)
        self.assertFalse(my_quit(), None)
        self.assertFalse(info_player(), print("Your choice is not correct!!\n"))
        self.assertFalse(info_team(), print("Your choice is not correct!!\n"))
        self.assertFalse(my_quit(), print("Your choice is not correct!!\n"))
        self.assertFalse(info_player(), 7)
        self.assertFalse(info_team(), 7)
        self.assertFalse(my_quit(), 7)
        self.assertFalse(info_player(), "")
        self.assertFalse(info_team(), "")
        self.assertFalse(my_quit(), "")

        # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(my_input("C"), "Your choice is not correct!!\n")
        self.assertEqual(my_input(7), "Your choice is not correct!!\n")

        # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(my_input(""), print("Your choice is not correct!!\n"))


        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(<def_name>([]), None)




if __name__ == '__main__':
    
    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)


