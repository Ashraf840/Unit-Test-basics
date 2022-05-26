import unittest
from employee import Employee


##########################
# Class based testcase
# Construct test-case for the "Employee" class.
##########################


class Test_Employee(unittest.TestCase):

    # DRY-ing the testcase code; instantiate the class object in a seperate function
    def setUp(self):
        self.emp_1 = Employee('Riaz', 'Hasan', 5000)
        self.emp_2 = Employee('Nasimul', 'Haque', 10000)

    # Test the email method: assign the first & last name to construct the mail for the employee.
    def test_email(self):
        # Check the equality of the assigning & constructing the email as expected
        self.assertEqual(self.emp_1.email, "riaz.hasan@gmail.com")
        self.assertEqual(self.emp_2.email, "nasimul.haque@gmail.com")
    
        # Change the first name of the emaployee & check if the email gets modified accordingly
        self.emp_1.first = "Ayesha"
        self.emp_2.first = "Nishad"

        self.assertEqual(self.emp_1.email, "ayesha.hasan@gmail.com")
        self.assertEqual(self.emp_2.email, "nishad.haque@gmail.com")

    def test_fullname(self):
        # Check the equality of the assigning & constructing the full name as expected
        self.assertEqual(self.emp_1.fullname, "Riaz Hasan")
        self.assertEqual(self.emp_2.fullname, "Nasimul Haque")
    
        # Change the first name of the emaployee & check if the fullname gets modified accordingly
        self.emp_1.first = "Ayesha"
        self.emp_2.first = "Nishad"

        self.assertEqual(self.emp_1.fullname, "Ayesha Hasan")
        self.assertEqual(self.emp_2.fullname, "Nishad Haque")

    def test_apply_raise(self):
        # Check the equality of the assigning the renumeration
        self.assertEqual(self.emp_1.pay, 5000)
        self.assertEqual(self.emp_2.pay, 10000)
    
        # Invoke the appriasal method to check the correctness of the calculation
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 10500)



if __name__ == "__main__":
    unittest.main()


"""
Method of running a testcase python file
Method-1:  Run the cmd.
    python -m unittest testcaseFileName.py

Method-2:  Run regular cmd to execute the testcase file.
    python testcaseFIleName.py
[ Condition ]:  We need to define the "unittest.main()" method inside the conditional check code-block, to execute the file with this method.
"""