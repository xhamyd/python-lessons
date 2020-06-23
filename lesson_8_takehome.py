"""
Lesson 8
--------

1) Tetris Line Clear

2) Detect if a string contains a footnote marker

3) Find the mean, median, and range of 2020 holidays using the days within the year as your key metric. BONUS: Plot it!

4) prep for Music21

5) Concatenate list of strings

Topics covered:

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
# TODO: Check for docstrings in every test
def test_1(function_under_test, val_num):
    return True
    # TODO: Provide JPGs for each test case
    in_val, out_val = [['-'] * 8] * 10, False
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else ("<blank_board>", out_val, actual_val)


def test_2(function_under_test, val_num):
    return True


def test_5(function_under_test, val_num):
    in_val = random.choices(string.hexdigits.replace("abcdef", "-:-x"), k=10_000_000)
    # ATOMIC_START
    start_time = time.time()
    out_val = function_under_test(in_val)
    end_time = time.time()
    # ATOMIC_END
    assert "".join(in_val[:10]) == out_val[:10]  # TODO
    time_threshold = 2.5
    return True if end_time - start_time < time_threshold else ("[<random_characters>]", "execution_time < 5 sec",
                                                                f"execution_time = {time_threshold} sec")


tcs = [TestCase(problem_number=1, description="blank",
                function_under_test=tetris_line_clear, testing_function=test_1, number_of_test_cases=1),
       TestCase(problem_number=2, description="blank",
                function_under_test=None, testing_function=test_2, number_of_test_cases=3),
       TestCase(problem_number=5, description="blank",
                function_under_test=combined_string, testing_function=test_5, number_of_test_cases=1)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
