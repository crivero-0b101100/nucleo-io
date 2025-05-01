import unittest
from list_utils import reverse_list

class TestListUtils(unittest.TestCase):
    def test_reverse_list_empty(self):
        """Test reversing an empty list"""
        self.assertEqual(reverse_list([]), [])
    
    def test_reverse_list_numbers(self):
        """Test reversing a list of numbers"""
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    
    def test_reverse_list_strings(self):
        """Test reversing a list of strings"""
        self.assertEqual(reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
    
    def test_reverse_list_mixed(self):
        """Test reversing a list with mixed types"""
        self.assertEqual(reverse_list([1, 'a', 2, 'b']), ['b', 2, 'a', 1])
    
    def test_reverse_list_invalid_input(self):
        """Test that non-list input raises TypeError"""
        with self.assertRaises(TypeError):
            reverse_list("not a list")
        with self.assertRaises(TypeError):
            reverse_list(123)
        with self.assertRaises(TypeError):
            reverse_list(None)

if __name__ == '__main__':
    unittest.main() 