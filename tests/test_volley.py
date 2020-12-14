#new_test_pyfile
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Main import my_input

'''
class TestAnswer(unittest.TestCase):
    def testA(self):
        original_raw_input = __builtins__.input
        __builtins__.input = lambda _: 'A'
        self.assertEqual(my_input(), 'You chose to have more info about the volleyball player.')
        __builtins__.input = original_raw_input

    def testB(self):
        original_raw_input = __builtins__.input
        __builtins__.input = lambda _: 'B'
        self.assertEqual(my_input(), 'You chose to have more info about the volleyball team.')
        __builtins__.input = original_raw_input

'''



class TestMain(unittest.TestCase):


    # smoke test: valid inputs
    def test_correct_A(self):
        # select some valid inputs, for which the output is known
        self.assertEqual(my_input("A"), "You chose to have more info about the volleyball player.")
        
        # smoke test: valid inputs
    def test_correct_B(self):
        # select some valid inputs, for which the output is known
        self.assertEqual(my_input("B"), "You chose to have more info about the volleyball team.")
        
        # smoke test: valid inputs
    def test_correct_Q(self):
        # select some valid inputs, for which the output is known
        self.assertEqual(my_input("Q"), "You chose to quit the program.")



# invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(my_input("C"), None)
        self.assertEqual(my_input(7), None)

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(<def_name>([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(my_input(""), None)


'''
    # add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Functions import fun_name


class TestFunctions(unittest.TestCase):

    def setUp(self):
        """Set the environment:
           create the dataframe output for test.
        """
        test_row_0 = df[0]

    # smoke test: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(fun_name("SALA CHIARA"), test_row_0)

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(fun_name("SALA CHIARA"), None)
        self.assertEqual(fun_name(7), None)

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(<def_name>([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(fun_name(""), None)
'''

if __name__ == '__main__':
    
    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)


