import unittest
from src.example_tests.grid_intersections import compute_intersecting_squares

class TestComputeIntersectingSquares(unittest.TestCase):
    def test_diagonal(self):
        starting_point = (0,0)
        ending_point = (5,5)
        expected_points = [(1,1), (2,2), (3,3), (4,4)]
        self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)

    def test_negative_diagonal(self):
        starting_point = (0,0)
        ending_point = (-5,-5)
        expected_points = [(-1,-1), (-2,-2), (-3,-3), (-4,-4)]
        self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)

    def test_partial_negative_diagonal(self):
        starting_point = (0,0)
        ending_point = (5,-5)
        expected_points = [(1,-1), (2,-2), (3,-3), (4,-4)]
        self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)

    def test_half_slope(self):
        starting_point = (0,0)
        ending_point = (6,3)
        expected_points = [(1,0), (2,1), (3,1), (4,2), (5,2)]
        self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)
    
    def test_slope_less_than_1(self):
        starting_point = (0,0)
        ending_point = (5,3)
        expected_points = [(1,0), (1,1), (2,1), (3,1), (3,2), (4,2)]
        self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)

    def test_slope_greater_than_1(self):
        starting_point = (0,0)
        ending_point = (3,7)
        expected_points = [(0,1), (0,2), (1,2), (1,3), (1,4), (2,4), (2,5), (2,6)]
        self.assertEqual(compute_intersecting_squares(starting_point, ending_point), expected_points)