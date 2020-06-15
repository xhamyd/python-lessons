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

Topics covered: files, lists

"""

import os

# --- DO NOT EDIT ABOVE THIS LINE --- #


def is_closed(file_pointer):
    pass  # TODO: delete this entire line and complete this function


def is_magic_square(square_array):
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
        return True if actual_val == out_val else in_val, out_val, actual_val
    else:
        in_val, out_val = open("tempfile1.txt", "w"), False
        actual_val = function_under_test(in_val)
        if not in_val.closed:
            in_val.close()
            os.remove(in_val.name)
            return in_val, out_val, actual_val
        return True if actual_val == out_val else in_val, out_val, actual_val


def test_2(function_under_test, val_num):
    in_vals = ([[2, 2], [2, 2]],
               [[5, 15, 16, 2], [10, 8, 7, 13], [6, 12, 11, 9], [17, 3, 4, 14]],
               [[4, 7, 1, 10], [3, 8, 2, 9], [9, 3, 8, 2], [6, 4, 11, 1]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    out_vals = (False, True, False, True)
    assert val_num in range(4), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else in_val, out_val, actual_val


tcs = [TestCase(problem_number=1, description="Determine if a file is closed.", function_under_test=is_closed,
                testing_function=test_1, number_of_test_cases=2),
       TestCase(problem_number=2, description="Determine a magic square or not.", function_under_test=is_magic_square,
                testing_function=test_2, number_of_test_cases=4)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
