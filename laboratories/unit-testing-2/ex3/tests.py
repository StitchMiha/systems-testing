import unittest
from unittest.mock import patch
import ex3


class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        with patch('ex3.read') as mock_read:
            mock_read.return_value = [1.0, 2.0, 3.0]

            result = ex3.calculate_total("fake_file.txt")

            self.assertEqual(result, 6.0)
            mock_read.assert_called_once_with("fake_file.txt")


if __name__ == '__main__':
    unittest.main()