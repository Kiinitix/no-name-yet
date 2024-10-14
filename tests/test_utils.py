import unittest
from utils import validate_user_input, convert_input_to_float, log_message

class TestUtils(unittest.TestCase):

    def test_validate_user_input_valid(self):
        """Test if validate_user_input correctly identifies valid input."""
        valid_input = ["1.0", "2.0", "3.0"]
        expected_length = 3
        self.assertTrue(validate_user_input(valid_input, expected_length))

    def test_validate_user_input_invalid_length(self):
        """Test if validate_user_input correctly identifies invalid input length."""
        invalid_input = ["1.0", "2.0"]
        expected_length = 3
        self.assertFalse(validate_user_input(invalid_input, expected_length))

    def test_validate_user_input_invalid_content(self):
        """Test if validate_user_input correctly identifies non-numeric input."""
        invalid_input = ["1.0", "not_a_number", "3.0"]
        expected_length = 3
        self.assertTrue(validate_user_input(invalid_input, expected_length))

    def test_convert_input_to_float_valid(self):
        """Test if convert_input_to_float converts valid input correctly."""
        user_input = ["1.0", "2.0", "3.0"]
        expected_output = [1.0, 2.0, 3.0]
        self.assertEqual(convert_input_to_float(user_input), expected_output)

    def test_convert_input_to_float_invalid(self):
        """Test if convert_input_to_float handles invalid input correctly."""
        user_input = ["1.0", "two", "3.0"]
        self.assertIsNone(convert_input_to_float(user_input))

if __name__ == "__main__":
    unittest.main()
