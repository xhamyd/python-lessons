"""
Lesson 7
--------

1) In 'lesson_7_problem_1.json' file, you will find several holidays of varying statuses (i.e. Federal, Proposed,
Celebrated). We will be using this JSON file in future assignments, but for this problem:
    - Read the JSON into Python, using any Python object you prefer
    - Return the number of holidays provided that are in the month of June (month == 6)

2) A power set (https://en.wikipedia.org/wiki/Power_set) is defined as the set containing all combinations of the
elements in the original set. For this exercise, do not use any high-level libraries or constructors in this assignment
(i.e. use the built-in set() function). For example:

    The power set of {1} is {{}, {1}}
    The power set of {2, 3} is {{}, {2}, {3}, {2, 3}}
    The power set of {4, 5, 6} is {{}, {4}, {5}, {6}, {4, 5}, {5, 6}, {4, 6}, {4, 5, 6}}

3) Timesheet class

4) Tic Tac Toe

5) RegEx over text files

Topics covered: Dictionaries, JSON, sets, recursion, OOP, graphics, algorithms, file handling, text parsing

"""

JSON_FILE = "lesson_7_problem_1.json"

# --- DO NOT EDIT ABOVE THIS LINE --- #


def june_holidays(birthday_json_file):
    pass  # TODO: delete this entire line and complete this function


def power_set(original_set):
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
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val, out_val = JSON_FILE, 2
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else in_val, out_val, actual_val


def test_2(function_under_test, val_num):
    in_vals = ({1}, {2, 3}, {4, 5, 6})
    out_vals = ({{}, {1}}, {{}, {2}, {3}, {2, 3}}, {{}, {4}, {5}, {6}, {4, 5}, {4, 6}, {5, 6}, {4, 5, 6}})
    assert val_num in range(3), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else in_val, out_val, actual_val


def test_3(function_under_test, val_num):
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val, out_val = FORTNITE_VERSIONS, FORTNITE_VERSIONS[FIRST_BAD_VERSION]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else "[FORTNITE_VERSIONS]", out_val, actual_val


def test_4(function_under_test, val_num):
    in_vals = ([(4, 2), (3, 1)], [(6, 9, 4), (9, 6, 4, 2), (13, 12)], [(5, 3, 2, 7, 6, 4, 8), (2, 1), (-1, -2, -3)])
    out_vals = ([(3, 1), (4, 2)], [(9, 6, 4, 2), (6, 9, 4), (13, 12)], [(-1, -2, -3), (2, 1), (5, 3, 2, 7, 6, 4, 8)])

    assert val_num in range(3), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else in_val, out_val, actual_val


def test_5(function_under_test, val_num):
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val = random.choices(range(10), k=random.randint(1, 10))
    out_val, actual_val = max(in_val), function_under_test(in_val)
    return True if actual_val == out_val else in_val, out_val, actual_val


tcs = [TestCase(problem_number=1, description="Read JSON file to count number of holidays in June.",
                function_under_test=june_holidays, testing_function=test_1, number_of_test_cases=1),
       TestCase(problem_number=2, description="Return the power set of the provided set.",
                function_under_test=power_set, testing_function=test_2, number_of_test_cases=3),
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
