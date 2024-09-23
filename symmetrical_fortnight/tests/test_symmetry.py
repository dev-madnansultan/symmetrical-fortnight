import unittest
from symmetrical_fortnight import generate_symmetry

class TestSymmetry(unittest.TestCase):
    def test_generate_symmetry(self):
        self.assertEqual(generate_symmetry("fortnight"), "fortnight|thginrof")
        self.assertEqual(generate_symmetry("symmetry"), "symmetry|yrtemmys")
        self.assertEqual(generate_symmetry(""), "|")  # Test for empty string

if __name__ == "__main__":
    unittest.main()
