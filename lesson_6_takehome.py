"""
Lesson 6
--------

1) With a provided file pointer, check if a file has been properly closed or not (and then close the file if not!)

    Return True for a closed file (is_closed(<file_closed 0x???>) == True).
    Return False for an open file (is_closed(<file_open 0x???>) == False).

2) A magic square (https://en.wikipedia.org/wiki/Magic_square) is a NxN square of unique integers from 1 to N^2, where
each horizontal, vertical, and diagonal row add up to the same number. Given a 2D array representation of a square,
determine if it is a magic square or not.

    [[ 2 2 ]           is not a magic square (is_magic_square(<...>) == False).
     [ 2 2 ]]

    [[  5 15 16  2 ]
     [ 10  8  7 13 ]   is a magic square (is_magic_square(<...>) == True).
     [  6 12 11  9 ]
     [ 17  3  4 14 ]]

    [[  4  7  1 10 ]
     [  3  8  2  9 ]   is not a magic square (is_magic_square(<...>) == False).
     [  9  3  8  2 ]
     [  6  4 11  1 ]]

    [[ 2 7 6 ]
     [ 9 5 1 ]         is a magic square (is_magic_square(<...>) == True).
     [ 4 3 8 ]]

3) Epic Games rolls out new versions of their insanely cool Fortnite program around every month, using X.YY versioning
scheme (https://semver.org/). Basically, the X number refers to the Season number (i.e. Season 10), and the YY number
refers to the patch number, usually for adding some small features/items within the same season.

As a QA Tester, you have gotten 10-year-old customers complaining that the Slurp Juice failed to give that epic gamer
point like it used to a year ago (~ver 8.00). From your testing, you have a running list whether the slurp juice worked
or not for each version since Season 8 started. Given this list, determine the first software version that broke this
function. You are provided the `is_slurp_juice_broken`, which takes in a version string from this list (i.e. "8.60") and
tells you whether this version is broken or not.

4) Given a list of tuples, sort the list using the second element of the tuple in ascending order.

    second_element_sort([(4, 2), (3, 1)]) == [(3, 1), (4, 2)]
    second_element_sort([(6, 9, 4), (9, 6, 4, 2), (13, 12)]) == [(9, 6, 4, 2), (6, 9, 4), (13, 12)]
    second_element_sort([(5, 3, 2, 7, 6, 4, 8), (2, 1), (-1, -2, -3)]) == [(-1, -2, -3), (2, 1), (5, 3, 2, 7, 6, 4, 8)]

5) Using recursion, find the maximum element in a list. Do not use for-loops, while-loops, or the built-in max()
function.


Topics covered: files, lists, search, lambda, recursion

"""

import os
import random

FIRST_BAD_VERSION = random.randrange(26)
FORTNITE_VERSIONS = ["8.00", "8.01", "8.10", "8.11", "8.20", "8.30", "8.40", "8.50", "9.00", "9.01", "9.20", "9.21",
                     "9.30", "9.40", "9.41", "10.10", "10.20", "10.30", "10.31", "10.4", "11.10", "11.20", "11.30",
                     "11.31", "11.40", "11.50"]


def is_slurp_juice_broken(version_string): return float(version_string) >= float(FORTNITE_VERSIONS[FIRST_BAD_VERSION])

# --- DO NOT EDIT ABOVE THIS LINE --- #


def is_closed(file_pointer):
    pass  # TODO: delete this entire line and complete this function


def is_magic_square(square_array):
    pass  # TODO: delete this entire line and complete this function


def when_did_slurp_break(version_list):
    pass  # TODO: delete this entire line and complete this function


def second_element_sort(tuple_list):
    pass  # TODO: delete this entire line and complete this function


def maximum_value(value_list):
    pass  # TODO: delete this entire line and complete this function


# --- DO NOT EDIT BELOW THIS LINE --- #


class TestCase:
    def __init__(self, problem_number, description, function_under_test, testing_function, number_of_test_cases):
        self.num = problem_number
        self.desc = description
        self.func = function_under_test
        self.test = testing_function
        self.cases = number_of_test_cases

    def __str__(self):
        return self.desc

    def run(self):
        res, outcome = True, []
        for case_num in range(self.cases):
            if (vals := self.test(self.func, case_num)) is not True:
                res = False
                in_val, out_val, actual_val = vals
                outcome.append(f"    Your solution:     {self.func.__name__}({in_val}) -> {actual_val}\n"
                               f"    Expected solution: {self.func.__name__}({in_val}) -> {out_val}\n")
        return res, outcome


# Test Cases
def test_1(function_under_test, val_num):
    assert val_num in range(2), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    if val_num == 0:
        in_val, out_val = open("tempfile0.txt", "w"), True
        in_val.close()
        actual_val = function_under_test(in_val)
        os.remove(in_val.name)
        return True if actual_val == out_val else (in_val, out_val, actual_val)
    else:
        in_val, out_val = open("tempfile1.txt", "w"), False
        actual_val = function_under_test(in_val)
        if not in_val.closed:
            in_val.close()
            os.remove(in_val.name)
            return in_val, out_val, actual_val
        return True if actual_val == out_val else (in_val, out_val, actual_val)


def test_2(function_under_test, val_num):
    in_vals = ([[2, 2], [2, 2]],
               [[5, 15, 16, 2], [10, 8, 7, 13], [6, 12, 11, 9], [17, 3, 4, 14]],
               [[4, 7, 1, 10], [3, 8, 2, 9], [9, 3, 8, 2], [6, 4, 11, 1]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    out_vals = (False, True, False, True)
    assert val_num in range(4), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else (in_val, out_val, actual_val)


def test_3(function_under_test, val_num):
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val, out_val = FORTNITE_VERSIONS, FORTNITE_VERSIONS[FIRST_BAD_VERSION]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else ("[FORTNITE_VERSIONS]", out_val, actual_val)


def test_4(function_under_test, val_num):
    in_vals = ([(4, 2), (3, 1)], [(6, 9, 4), (9, 6, 4, 2), (13, 12)], [(5, 3, 2, 7, 6, 4, 8), (2, 1), (-1, -2, -3)])
    out_vals = ([(3, 1), (4, 2)], [(9, 6, 4, 2), (6, 9, 4), (13, 12)], [(-1, -2, -3), (2, 1), (5, 3, 2, 7, 6, 4, 8)])

    assert val_num in range(3), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else (in_val, out_val, actual_val)


def test_5(function_under_test, val_num):
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val = random.choices(range(10), k=random.randint(1, 10))
    out_val, actual_val = max(in_val), function_under_test(in_val)
    return True if actual_val == out_val else (in_val, out_val, actual_val)


tcs = [TestCase(problem_number=1, description="Determine if a file is closed.", function_under_test=is_closed,
                testing_function=test_1, number_of_test_cases=2),
       TestCase(problem_number=2, description="Determine a magic square or not.", function_under_test=is_magic_square,
                testing_function=test_2, number_of_test_cases=4),
       TestCase(problem_number=3, description="Find first version with broken slurp juice.",
                function_under_test=when_did_slurp_break, testing_function=test_3, number_of_test_cases=1),
       TestCase(problem_number=4, description="Sort list of tuples by second element.",
                function_under_test=second_element_sort, testing_function=test_4, number_of_test_cases=3),
       TestCase(problem_number=5, description="Find maximum element using recursion.",
                function_under_test=maximum_value, testing_function=test_5, number_of_test_cases=1)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
