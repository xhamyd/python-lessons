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
    def __init__(self, problem_number, description, function_under_test, testing_function):
        self.num = problem_number
        self.desc = description
        self.func = function_under_test
        self.test = testing_function

    def __str__(self):
        return self.desc

    def run(self):
        return self.test(self.func)


def test_1(function_under_test):
    res, outcome = True, []
    in_vals = [1, 2, 3]
    out_vals = [1, 4, 9]
    for in_val, out_val in zip(in_vals, out_vals):
        actual_val = function_under_test(in_val)
        if actual_val != out_val:
            res = False
            outcome.append(f"    Your solution:     {function_under_test.__name__}({in_val}) -> {actual_val}\n"
                           f"    Expected solution: {function_under_test.__name__}({in_val}) -> {out_val}\n")
    return res, outcome


# Test Cases
tcs = [TestCase(problem_number=1, description="Determine if a string is a palindrome.",
                function_under_test=is_palindrome, testing_function=test_1)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
