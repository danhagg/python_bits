import unittest
from name_function import get_formatted_name


# following class inherits from class unittest.TestCase
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

# method to verify names with 1st and last formatted correctly
# method must start with "test"
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgnag Amadeus Mozart' work"""
        formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
