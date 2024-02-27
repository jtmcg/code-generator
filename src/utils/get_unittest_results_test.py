import unittest
from get_unittest_results import get_unittest_results

class TestGetUnittestResults(unittest.TestCase):
    results_string = ".F..FF\n======================================================================\nFAIL: test_half_slope (src.example_tests.grid_intersections_test.TestComputeIntersectingSquares.test_half_slope)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/Users/jtmcgoffin/Documents/projects/semanticAI/semanticai/src/example_tests/grid_intersections_test.py\", line 27, in test_half_slope\n    self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)\nAssertionError: Lists differ: [(1, 0), (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 2), (4, 3), (5, 2), (5, 3)] != [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2)]\n\nFirst differing element 1:\n(1, 1)\n(2, 1)\n\nFirst list contains 5 additional elements.\nFirst extra element 5:\n(3, 2)\n\n- [(1, 0), (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 2), (4, 3), (5, 2), (5, 3)]\n+ [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2)]\n\n======================================================================\nFAIL: test_slope_greater_than_1 (src.example_tests.grid_intersections_test.TestComputeIntersectingSquares.test_slope_greater_than_1)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/Users/jtmcgoffin/Documents/projects/semanticAI/semanticai/src/example_tests/grid_intersections_test.py\", line 39, in test_slope_greater_than_1\n    self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)\nAssertionError: Lists differ: [(0, 1), (1, 1), (0, 2), (1, 2), (1, 3), (2, 3), (1[40 chars], 6)] != [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (2, 6)]\n\nFirst differing element 1:\n(1, 1)\n(0, 2)\n\nFirst list contains 4 additional elements.\nFirst extra element 8:\n(2, 5)\n\n+ [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (2, 6)]\n- [(0, 1),\n-  (1, 1),\n-  (0, 2),\n-  (1, 2),\n-  (1, 3),\n-  (2, 3),\n-  (1, 4),\n-  (2, 4),\n-  (2, 5),\n-  (3, 5),\n-  (2, 6),\n-  (3, 6)]\n\n======================================================================\nFAIL: test_slope_less_than_1 (src.example_tests.grid_intersections_test.TestComputeIntersectingSquares.test_slope_less_than_1)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/Users/jtmcgoffin/Documents/projects/semanticAI/semanticai/src/example_tests/grid_intersections_test.py\", line 33, in test_slope_less_than_1\n    self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)\nAssertionError: Lists differ: [(1, 0), (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 2), (4, 3)] != [(1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2)]\n\nFirst differing element 3:\n(2, 2)\n(3, 1)\n\nFirst list contains 2 additional elements.\nFirst extra element 6:\n(4, 2)\n\n- [(1, 0), (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 2), (4, 3)]\n+ [(1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2)]\n\n----------------------------------------------------------------------\nRan 6 tests in 0.002s\n\nFAILED (failures=3)\n"
    
    def test_test_count(self):
        self.assertEqual(get_unittest_results(self.results_string)["total_count"], 6)

    def test_fail_count(self):
        self.assertEqual(get_unittest_results(self.results_string)["failed_count"], 3)
    
    def test_failed_names(self):
        self.assertEqual(get_unittest_results(self.results_string)["failed_names"], ["test_half_slope", "test_slope_greater_than_1", "test_slope_less_than_1"])

    def test_success_count(self):
        self.assertEqual(get_unittest_results(self.results_string)["success_count"], 3)

if __name__ == 'main':
    unittest.main()