"""
Lesson 6
--------

1) With a provided file pointer, check if a file has been properly closed or not (and then close the file if not!)

    Return True for a closed file (is_closed(<file_closed 0x???>) == True).
    Return False for an open file (is_closed(<file_open 0x???>) == False).

Topics covered:

"""

import os

# --- DO NOT EDIT ABOVE THIS LINE --- #


def is_closed(file_pointer):
    pass  # TODO: delete this entire line and complete this function


def list_overlap(first_list, second_list):
    pass  # TODO: delete this entire line and complete this function


def factors(dividend):
    pass  # TODO: delete this entire line and complete this function


def is_prime(number):
    pass  # TODO: delete this entire line and complete this function


def text_at_line(line_number, filename="lesson_5_problem_5.txt"):
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
        for case_num in range(1, self.cases+1):
            if (vals := self.test(self.func, case_num)) is not True:
                res = False
                in_val, out_val, actual_val = vals
                outcome.append(f"    Your solution:     {self.func.__name__}({in_val}) -> {actual_val}\n"
                               f"    Expected solution: {self.func.__name__}({in_val}) -> {out_val}\n")
        return res, outcome


# Test Cases
def test_1(function_under_test, val_num):
    assert val_num in (1, 2), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    if val_num == 1:
        in_val, out_val = open("tempfile1.txt", "w"), True
        in_val.close()
        actual_val = function_under_test(in_val)
        os.remove(in_val.name)
        return True if actual_val == out_val else in_val, out_val, actual_val
    else:
        in_val, out_val = open("tempfile2.txt", "w"), False
        actual_val = function_under_test(in_val)
        if not in_val.closed:
            in_val.close()
            os.remove(in_val.name)
            return in_val, out_val, actual_val
        return True if actual_val == out_val else in_val, out_val, actual_val


tcs = [TestCase(problem_number=1, description="Determine if a file is closed.", function_under_test=is_closed,
                testing_function=test_1, number_of_test_cases=2)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
