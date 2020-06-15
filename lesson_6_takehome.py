"""
Lesson 6
--------

1)

Topics covered:

"""

# --- DO NOT EDIT ABOVE THIS LINE --- #


def is_palindrome(string_to_check):
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
        for case_num in range(self.cases):
            if (vals := self.test(self.func, case_num)) is not True:
                res = False
                in_val, out_val, actual_val = vals
                outcome.append(f"    Your solution:     {self.func.__name__}({in_val}) -> {actual_val}\n"
                               f"    Expected solution: {self.func.__name__}({in_val}) -> {out_val}\n")
        return res, outcome


# Test Cases
def test_1(function_under_test, val_num):
    in_vals = [1, 2, 3]
    out_vals = [1, 4, 9]

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if out_val == actual_val else in_val, out_val, actual_val


tcs = [TestCase(problem_number=1, description="Determine if a string is a palindrome.",
                function_under_test=is_palindrome, testing_function=test_1, number_of_test_cases=3)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
