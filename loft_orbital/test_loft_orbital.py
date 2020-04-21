import pytest
import loft_orbital as lo


class TestLoft:

    # Verifying the number of created arrays
    def test_array_number(self):
        assert (len(lo.ten_random_arrays)) == 10, "The number of created arrays != 10"

    # Verifying the length of each array
    def test_array_len(self):
        for x in range(0, len(lo.ten_random_arrays)-1):
            assert (len(lo.ten_random_arrays[x])) == 10000, "The number of values != 10000"

    # Verifying the range of numbers in each array
    def test_verify_numbers_range_in_array(self):
        for x in range(0, len(lo.ten_random_arrays)-1):
            for i in lo.ten_random_arrays[x]:
                assert 0 <= i <= 9, "Not all values are between 0 and 9"

    # Testing Bubble sort function
    def test_bubble_sort(self):
        lst = [3, 1, 2, 4]  # positive values
        neg_lst = [3, 3, -1, 4]  # with negative values
        lo.bubble_sort(lst)
        lo.bubble_sort(neg_lst)
        assert lst == [1, 2, 3, 4], "The sorting was not correct"
        assert neg_lst == [-1, 3, 3, 4], "The sorting was not correct"

    # Testing the function that counts the number of occurrences
    def test_count_number_of_occurrences(self):
        lst = [2, 3, 3]  # positive values
        neg_lst = [-3, -4, -4]  # negative values
        number = lo.count_number_of_occurrences(lst)
        number2 = lo.count_number_of_occurrences(neg_lst)
        assert number == {2: 1, 3: 2}, "The number of occurrences is not correct"
        assert number2 == {-4: 2, -3: 1}, "The number of occurrences is not correct"
