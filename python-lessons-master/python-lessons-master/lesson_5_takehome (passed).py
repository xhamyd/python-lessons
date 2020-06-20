"""
Lesson 5
--------

1) Given a single string input argument, return True if this string is a palindrome (False otherwise). A string is a
palindrome is it is the spelled the same backwards and forwards.

    "racecar" is a palindrome (is_palindrome("racecar") == True)
    "dodo" is not a palindrome (is_palindrome("doom") == False)
    "rotator" is a palindrome (is_palindrome("rotator") == True)
    "moomoo" is not a palindrome (is_palindrome("moomoo") == False)

2) Given two lists of varying lengths, return a list of the common elements between both lists.

    [1, 2, 3, 5] and [3, 4, 5] returns [3, 5]
    [0, -5, 16] and [37, 12, 16, 5] returns [16]
    [5, 5, 7, 6] and [5, 5, 7, 6] returns [5, 7, 6]

3) Given a single integer argument, return a list of its integer factors/divisors. Bonus points if you use list
comprehension.

    [1, 2, 3, 6] are all of the factors for 6 (factors(6) == [1, 2, 3, 6])
    [1, 11] are all of the factors for 11 (factors(11) == [1, 11])
    [1, 2, 3, 6, 9, 18] are all of the factors for 18 (factors(18) == [1, 2, 3, 6, 9, 18])

4) Using your answer in Question 3, determine if a given integer is prime or not. You should call the `factors` function
inside of your `is_prime` function.

    is_prime(6) ==> False
    is_prime(11) ==> True
    is_prime(18) ==> False

5) Using the provided text file, return the string of text at a given line number. Don't forget to strip newlines ('\n')
from the returned text!

    text_at_line(1146) ==> "I suppose so."
    text_at_line(1999) ==> "Curabitur quis pretium mi."
    text_at_line(2183) ==> "Primary schools"

Topics covered: strings, indexing, functions, lists, sets, arithmetic, helper functions

"""

# --- DO NOT EDIT ABOVE THIS LINE --- #

import re


def is_palindrome(x):
    reverse = x[len(x)::-1]
    check = re.match(x, reverse)
    return bool(check)


def list_overlap(first_list, second_list):
    first_set = set(first_list)
    second_set = set(second_list)
    return list(first_set & second_set)


def factors(dividend):
    value = set()
    for x in range(1, dividend + 1):
        if dividend % x == 0:
            value.add(x)
    return list(value)


def is_prime(number):
    for x in range(2, number + 1):
        if number % x == 0:
            return False
        else:
            return True


def text_at_line(line_number, filename="lesson_5_problem_5.txt"):
    file = open(filename)
    all_lines = file.readlines()
    line = str(all_lines[line_number - 1])

    return line.rstrip("\n")
            

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
                out_vals=(([3, 5]), ([16]), ([5, 6, 7])), unsorted=True),
                   #the second out_vals should have a 16
       TestCase(problem_number=3, description="List all of the factors for a given integer", test_function=factors,
                in_vals=(6, 11, 18), out_vals=(([1, 2, 3, 6]), ([1, 11]), ([1, 2, 3, 6, 9, 18]))),
                   #the third out_vals should'nt have a 4 as a factor of 18
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
