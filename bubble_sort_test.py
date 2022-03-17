import unittest
import bubble_sort
class TestBubbleSortAlgorithm(unittest.TestCase):

    def _test_sort(self, sorting_func, input_list):
        expected_list = sorted(input_list)
        self.assertEqual(sorting_func(input_list), expected_list)

    def test_bubble_sort_with_positive_numbers(self):
        input_list = [5, 5, 7, 8, 2, 4, 1]
        self._test_sort(bubble_sort.bubble_sort_v1, input_list)
        self._test_sort(bubble_sort.bubble_sort_v2, input_list)

    def test_bubble_sort_negative_numbers_only(self):
        input_list = [-1, -3, -5, -7, -9, -5]
        self._test_sort(bubble_sort.bubble_sort_v1, input_list)
        self._test_sort(bubble_sort.bubble_sort_v2, input_list)

    def test_bubble_sort_with_negative_and_positive_numbers(self):
        input_list = [-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]
        self._test_sort(bubble_sort.bubble_sort_v1, input_list)
        self._test_sort(bubble_sort.bubble_sort_v2, input_list)

    def test_bubble_sort_same_numbers(self):
        input_list = [1, 1, 1, 1]
        self._test_sort(bubble_sort.bubble_sort_v1, input_list)
        self._test_sort(bubble_sort.bubble_sort_v2, input_list)

    def test_bubble_sort_empty_list(self):
        input_list = []
        self._test_sort(bubble_sort.bubble_sort_v1, input_list)
        self._test_sort(bubble_sort.bubble_sort_v2, input_list)