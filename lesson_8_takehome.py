"""
Lesson 8
--------

1) Tic Tac Toe

2) RegEx over text files

3) Holiday Stats

4) prep for NumPy/MatPlotLib

5) prep for Music21

6) Optimization / Big O

Topics covered: graphics, algorithms, file handling, text parsing

"""


# --- DO NOT EDIT ABOVE THIS LINE --- #


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
    return True

def test_2(function_under_test, val_num):
    return True


tcs = [TestCase(problem_number=1, description="blank",
                function_under_test=None, testing_function=test_1, number_of_test_cases=1),
       TestCase(problem_number=2, description="blank",
                function_under_test=None, testing_function=test_2, number_of_test_cases=3)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
