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
    def __init__(self, problem_number, description, test_function, in_vals, out_vals, unsorted=False):
        self.num = problem_number
        self.desc = description
        self.func = test_function
        assert len(in_vals) == len(out_vals)
        self.cases = (in_vals, out_vals)
        self.unsorted = unsorted

    def __str__(self):
        return self.desc

    def unsorted_check(self, a_val, o_val):
        if self.unsorted:
            return isinstance(a_val, list) and isinstance(o_val, list) and sorted(a_val) == sorted(o_val)
        else:
            return True

    def run(self):
        res, outcome = True, []
        for in_val, out_val in zip(*self.cases):
            actual_val = self.func(*in_val) if isinstance(in_val, tuple) else self.func(in_val)
            if isinstance(in_val, tuple):
                in_val_print = f"{in_val}"[1:-1]  # drop the tuple parens when printing to console
            elif isinstance(in_val, str):
                in_val_print = f"\"{in_val}\""
            else:
                in_val_print = f"{in_val}"
            out_val_print = f"\"{out_val}\"" if isinstance(out_val, str) else f"{out_val}"
            actual_val_print = f"\"{actual_val}\"" if isinstance(actual_val, str) else f"{actual_val}"

            if not self.unsorted_check(actual_val, out_val) or actual_val != out_val:
                res = False
                outcome.append(f"    Your solution:     {self.func.__name__}({in_val_print}) -> {actual_val_print}\n"
                               f"    Expected solution: {self.func.__name__}({in_val_print}) -> {out_val_print}\n")
        return res, outcome


# Test Cases
tcs = [TestCase(problem_number=1, description="Determine if a string is a palindrome.", test_function=is_palindrome,
                in_vals=("racecar", "dodo", "rotator", "moomoo"), out_vals=(True, False, True, False)),
       TestCase(problem_number=2, description="Find the overlapping elements in two lists.", test_function=list_overlap,
                in_vals=(([1, 2, 3, 5], [3, 5]), ([0, -5, 16], [37, 12, 16, 5]), ([5, 5, 6, 7], [5, 5, 6, 7])),
                out_vals=(([3, 5]), ([]), ([5, 6, 7])), unsorted=True),
       TestCase(problem_number=3, description="List all of the factors for a given integer", test_function=factors,
                in_vals=(6, 11, 18), out_vals=(([1, 2, 3, 6]), ([1, 11]), ([1, 2, 3, 4, 6, 9, 18]))),
       TestCase(problem_number=4, description="Determine if a number is prime.", test_function=is_prime,
                in_vals=(6, 11, 18), out_vals=(False, True, False)),
       TestCase(problem_number=5, description="Find a line of text within a file.", test_function=text_at_line,
                in_vals=(1146, 1999, 2183),
                out_vals=("I suppose so.", "Curabitur quis pretium mi.", "Primary schools"))]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
