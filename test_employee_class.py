from employee_class import Employee
import unittest
from unittest.mock import patch


class test_employee(unittest.TestCase):
    """the print statements are used to display how this code works"""

    @classmethod
    def setUpClass(cls):
        # print("this is setUp class method")
        pass

    @classmethod
    def tearDownClass(cls):
        # print("this is tearDown class method")
        pass

    def setUp(self):
        # print("setup")
        self.emp1 = Employee("Srinivas", "Koda", 50000)
        self.emp2 = Employee("Pavan", "Koda", 60000)

    def tearDown(self) -> None:
        # print("tear down")
        pass

    def test_full_name(self):
        # print("full name")
        self.assertEqual(self.emp1.full_name, "Srinivas Koda")
        self.assertEqual(self.emp2.full_name, "Pavan Koda")

        self.emp1.first_name = "Sasuke"
        self.emp2.first_name = "Naruto"

        self.assertEqual(self.emp1.full_name, "Sasuke Koda")
        self.assertEqual(self.emp2.full_name, "Naruto Koda")

    def test_email(self):
        # print("test email")
        self.assertEqual(self.emp1.email, "srinivaskoda@youwecan.com")
        self.assertEqual(self.emp2.email, "pavankoda@youwecan.com")

        self.emp1.last_name = "Uchiha"
        self.emp2.last_name = "Uzumaki"

        self.assertEqual(self.emp1.email, "srinivasuchiha@youwecan.com")
        self.assertEqual(self.emp2.email, "pavanuzumaki@youwecan.com")

    def test_apply_raise(self):
        # print("apply raise")
        self.emp1.raise_amount = 1.10
        self.assertEqual(self.emp1.apply_raise(), 55000)
        self.assertEqual(self.emp2.apply_raise(), 63000)

    def test_monthly_schedule(self):
        with patch("employee_class.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule("june")
            mocked_get.assert_called_with("http://youwecan.com/Koda/june")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule("may")
            mocked_get.assert_called_with("http://youwecan.com/Koda/may")
            self.assertEqual(schedule, "Bad response")








