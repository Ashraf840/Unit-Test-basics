import unittest
import calc


#############################
# Function Based testcase
#############################


class Test_calc(unittest.TestCase):
    # ** Testcase: Basic Arithmetic Calculation **

    def test_add(self):
        # use the func to get the sum of params
        self.assertEqual(calc.add(10,5), 15)
        # adding multiple checks, making the testcase better
        self.assertEqual(calc.add(1,-1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
        self.assertEqual(calc.add(-1,1), 0)
    
    def test_sub(self):
        self.assertEqual(calc.sub(10,5), 5)
        self.assertEqual(calc.sub(1,-1), 2)
        self.assertEqual(calc.sub(-1,-1), 0)
        self.assertEqual(calc.sub(-1,1), -2)
        # self.assertEqual(calc.sub(-1,1), -3) # it'll make the testcase throw an error
    
    def test_mul(self):
        self.assertEqual(calc.mul(5,5), 25)
        self.assertEqual(calc.mul(10,-2), -20)
        self.assertEqual(calc.mul(-10,-10), 100)
        self.assertEqual(calc.mul(-3,5), -15)
    
    def test_div(self):
        self.assertEqual(calc.div(10,5), 2)
        self.assertEqual(calc.div(9,-3), -3)
        self.assertEqual(calc.div(-42,-7), 6)
        self.assertEqual(calc.div(-40,10), -4)
        
        # Test: valueError
        
        # Method-1
        # self.assertRaises(ValueError, calc.div, 10, 0)

        # Method-2
        with self.assertRaises(ValueError):
            calc.div(10, 0)
