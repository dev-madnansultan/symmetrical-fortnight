import unittest
from symmetrical_fortnight import generate_symmetry, generate_vertical_symmetry, generate_random_symmetry

class TestSymmetry(unittest.TestCase):
    def test_generate_symmetry(self):
        self.assertEqual(generate_symmetry("fortnight"), "fortnight|thginrof")
        self.assertEqual(generate_symmetry("symmetry"), "symmetry|yrtemmys")
        self.assertEqual(generate_symmetry(""), "Input cannot be empty.")  # Test for empty string
    
    def test_vertical_symmetry(self):
        result = generate_vertical_symmetry("fort")
        expected = "f f\no o\nr r\nt t"
        self.assertEqual(result, expected)
    
    def test_random_symmetry(self):
        result = generate_random_symmetry("fortnight")
        self.assertIn(result, ["fortnight|" + ''.join(p) for p in random.sample("fortnight", len("fortnight"))])

    def test_vertical_empty(self):
        self.assertEqual(generate_vertical_symmetry(""), "Input cannot be empty.")

    def test_random_empty(self):
        self.assertEqual(generate_random_symmetry(""), "Input cannot be empty.")

if __name__ == "__main__":
    unittest.main()
