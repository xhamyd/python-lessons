"""
1) Define a function `nth_fibonacci` that takes in a single int argument, and returns the Fibonacci number at that
spot in the sequence. Assuming the following sequence for Fibonacci:

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

The 1st Fibonacci Number would be 1 (nth_fibonacci(1) == 1)
The 2nd Fibonacci Number would be 1 (nth_fibonacci(2) == 1)
The 3rd Fibonacci Number would be 1 (nth_fibonacci(3) == 2)
The 4th Fibonacci Number would be 1 (nth_fibonacci(4) == 3)

Topics covered: functions, lists, for/while loops, arithmetic operations, variables

"""

# --- DO NOT EDIT ABOVE THIS LINE --- #


def nth_fibonacci(x):
    pass  # TODO: complete this function

# --- DO NOT EDIT BELOW THIS LINE --- #


class TestCase:
    def __init__(self, problem_number, description, test_function, expected_values):
        self.num = problem_number
        self.desc = description
        self.func = test_function
        self.cases = expected_values

    def __str__(self):
        return self.desc

    def run(self):
        res, outcome = True, []
        for in_val, out_val in self.cases.items():
            if self.func(in_val) != out_val:
                res = False
                outcome.append(f"    Your solution:     {self.func.__name__}({in_val}) -> {self.func(in_val)}\n"
                               f"    Expected solution: {self.func.__name__}({in_val}) -> {out_val}\n")
        return res, outcome


# Test Cases
tcs = [TestCase(problem_number=1, description="Find the nth Fibonacci number in the sequence.",
                test_function=nth_fibonacci, expected_values={1: 1, 2: 1, 3: 2, 4: 3})]
for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
