import unittest
import mastermind
import random
from mastermind import create_code
from mastermind import check_correctness
from mastermind import take_turn
from unittest.mock import patch
from io import StringIO
 
def get_answer_input():
    return input('Enter your guess: ') 


class TestFunctions(unittest.TestCase):
    """
    tests if create_code function is creating a code with 4 digits and to see if it lies between the range of 1 and 8
    """
    def test_code(self):
        count = 0
        while count < 100:
            self.assertEqual(len(create_code()), 4)
            for i in range(0, 4):
                create_code()[i]
                self.assertTrue(create_code()[i] >= 1 and create_code()[i] <= 8)
            count += 1
    """
    tests check_correctness function if the its returning the correct True or False value depending on the code
    """  
    def test_correct(self):
        number_true = 4
        number_false = random.randint(0, 3)
        self.assertTrue(check_correctness(10, number_true) == True)
        self.assertTrue(check_correctness(10, number_false) == False)
    """
    checks if the code you entered is 4 digits
    """
    @patch("sys.stdin", StringIO("1234\n12345\n"))
    def test_input(self):
        self.assertEqual(get_answer_input(), "1234")
        self.assertEqual(get_answer_input(), "12345")

    """
    Tests the output of the take turn function to check if it returns the correct outputs
    """
    @patch("sys.stdin", StringIO("7851\n1234\n5647\n8765"))
    def test_take_turn(self):
        self.assertEqual(take_turn([1,2,3,4]), (0,1))
        self.assertEqual(take_turn([4,3,2,1]), (0,4))
        self.assertEqual(take_turn([7,8,5,1]), (0,2))
        self.assertEqual(take_turn([8,7,6,5]), (4,0))

if __name__ == "__main__":
    unittest.main()
