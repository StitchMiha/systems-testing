import unittest
import datetime
from unittest.mock import patch, Mock


def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)


import datetime
import unittest
from unittest.mock import patch, Mock


def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)


class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        fake_date = Mock()
        fake_date.year = 2024

        with patch('ex1.datetime.datetime') as mock_datetime:
            mock_datetime.today.return_value = fake_date
            self.assertTrue(is_leap_year())

    def test_not_leap_year(self):
        fake_date = Mock()
        fake_date.year = 2023

        with patch('ex1.datetime.datetime') as mock_datetime:
            mock_datetime.today.return_value = fake_date
            self.assertFalse(is_leap_year())


if __name__ == '__main__':
    unittest.main()