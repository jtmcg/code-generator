import unittest
from utils import strip_unittest_path

class TestStripUnittestPath(unittest.TestCase):
    def test_unit_test_name(self):
        unittest_path = "test_path/unit_test.py"
        test_name, _ = strip_unittest_path(unittest_path)
        self.assertEqual(test_name, "unit")

    def test_unit_test_path(self):
        unittest_path = "test_path/unit_test.py"
        _, path = strip_unittest_path(unittest_path)
        self.assertEqual(path, "test_path/")

    def test_unit_test_complex_path(self):
        unittest_path = "test_path/complex/unit_test.py"
        _, path = strip_unittest_path(unittest_path)
        self.assertEqual(path, "test_path/complex/")

if __name__ == 'main':
    unittest.main()