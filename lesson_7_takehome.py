"""
Lesson 7
--------

1) In 'lesson_7_problem_1.json' file, you will find several holidays of varying statuses (i.e. Federal, Proposed,
Celebrated). We will be using this JSON file in future assignments, but for this problem:
    - Read the JSON into Python, using any Python object you prefer
    - Return the number of holidays provided that are in the month of June (month == 6)

2) A power set (https://en.wikipedia.org/wiki/Power_set) is defined as the set containing all combinations of the
elements in the original set. For this exercise, BUILD YOUR "sets" USING PYTHON LISTS! For example:

    The power set of [1] is [[], [1]]
    The power set of [2, 3] is [[], [2], [3], [2, 3]]
    The power set of [4, 5, 6] is [[], [4], [5], [6], [4, 5], [5, 6], [4, 6], [4, 5, 6]]

3) Use OOP principles to create two classes: a general FileReader class, and a specific JSONReader class. Your classes
must support the following functions:

    FileReader must have a constructor method that takes the variable `filename` and `type_of_file`
    FileReader must have a read() function, that reads the file as a binary string and returns the result
    JSONReader should inherit FileReader's constructor method, but should also create the instance variable `json_dict`
    JSONReader must have a read() function, that loads the file as a dictionary and saves the result into the
    `json_dict` instance variable. Return True if the load was successful.
        - HINT: a simple try-except block is sufficient here

Your function `create_reader_classes` will take in `binary_filename`, `binary_type_of_file`, `json_filename`, and
`json_type_of_file`. It should return a tuple containing the two classes references.

Topics covered: Dictionaries, JSON, sets, recursion, OOP, file handling

"""

import os

JSON_FILE = "lesson_7_problem_1.json"

# --- DO NOT EDIT ABOVE THIS LINE --- #
import json
import re


def june_holidays(JSON_FILE):
    pass
"""
   with open (JSON_FILE) as f:
        holidays = json.load(f)
        for i in range(0):
            count = 0
            if holidays.value(i) == 6:
                    count = count + 1
                    
        return count
        f.close


I couldn't figure out how to specifically look for the month in the dictionary. What I wanted to do in this,
was to first load in the JSON file as the variable, "Holidays", then iterate through the dictionary to find
and count how many times 'month' = 6. I was expecting months to be a key, but I think i messed that up
by assigning it to a variable.

"""


def power_set(original_set):
    length = len(original_set)
    for i in range(1 << length):
        for j in range(length):
            if (i & (1 << j)):
                return [original_set[j]]

"""
    length = len(original_set)
    print([])
    for i in range(0, length):
        print([original_set[i]])

    if length>1:
        for i in range(0, length-1):
            for j in range (0, length-1):
                print([i, j+1])
            
    elif length>2:
        print(original_set)

Here's what I had originally. It was close, though I messed around with it too many times and it fell apart.
The other "solution" is from https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset.

What I was trying to do was first, find out how many elements there are, print out the none element,
then print each element separately, followed by the permutations, and then the whole set as one list by itself.

For some reason, returns stop the function short, and prints don't work for passing the test,
so it still is unsolved.

"""
    
def create_reader_classes(binary_filename, binary_type_of_file, json_filename, json_type_of_file):
    class FileReader:
        def __init__ (self, filename, type_of_file):
            self.name = filename
            self.type = type_of_file

        def read(self):
            return self.name.read()

    class JSONReader(FileReader):
        def __init__ (self, json_dict):
            self.dict = json_dict

        def read(self):
            try:
                json_dict = dict(self.dict)
                return json_dict
            except:
                print("Failure to load")
            
"""
Don't even know

"""


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
    in_vals = ([1], [2, 3], [4, 5, 6])
    out_vals = ([[], [1]], [[], [2], [3], [2, 3]], [[], [4], [5], [6], [4, 5], [4, 6], [5, 6], [4, 5, 6]])
    assert val_num in range(3), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else in_val, out_val, actual_val


def test_3(function_under_test, val_num):
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_val = ("binary_file.b", "binary", "lesson_7_problem_3.json", "JSON")
    actual_val = function_under_test(*in_val)
    if not isinstance(actual_val, tuple) or len(actual_val) != 2:
        return in_val, ("<class FileReader>", "<class JSONReader>"), actual_val
    fr_class, jr_class = actual_val
    fread, jread = fr_class(), jr_class()
    binary_output = fread.read()
    if type(binary_output) == bytes:
        binary_output = binary_output.decode('utf-8')
    if binary_output != "Foo © bar":
        return "FileReader.read()", "Foo © bar", binary_output
    if not hasattr(jread, "json_dict"):
        return in_val, "JSONReader.json_dict exists", "JSONReader.json_dict does not exists"
    json_res = jread.read()
    if json_res is not True:
        return "JSONReader.read()", "True", json_res
    json_output = jread.json_dict
    json_dict = {
        "main": {
            "fibonacci": [1, 2, 3, 5, 8],
            "fav_numbers": "6, 29",
            "secret": {
                "favorite_brother": None
            }
        }
    }
    if json_output != json_dict:
        return "JSONReader.read()", json_dict, json_output
    os.remove("lesson_7_problem_1.json")
    json_res = jread.read()
    if json_res is not False:
        return "JSONReader.read()", "False", json_res


tcs = [TestCase(problem_number=1, description="Read JSON file to count number of holidays in June.",
                function_under_test=june_holidays, testing_function=test_1, number_of_test_cases=1),
       TestCase(problem_number=2, description="Return the power set of the provided set.",
                function_under_test=power_set, testing_function=test_2, number_of_test_cases=3),
       TestCase(problem_number=3, description="Create FileReader and JSONReader classes.",
                function_under_test=create_reader_classes, testing_function=test_3, number_of_test_cases=1)]

for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")
    r, o = tc.run()
    if r:
        print(f"PASSED")
    else:
        print(f"FAILED")
        for out_text in o:
            print(f"{out_text}")
