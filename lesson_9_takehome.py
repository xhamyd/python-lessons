"""
Lesson 9
--------

1) blah.

    - blah

2) blah.

    - blah

3) blah

    - blah

4) blah

    - blah

5) blah

Topics covered:

"""

# --- DO NOT EDIT ABOVE THIS LINE --- #


def blah1():
    pass  # TODO: delete this entire line and complete this function


def blah2():
    raise NotImplementedError  # TODO: delete this entire line and complete the function


def blah3():
    pass  # TODO: delete this entire line and complete this function


def blah4():
    raise NotImplementedError  # TODO: delete this entire line and complete the function


def blah5():
    pass  # TODO: delete this entire line and complete the function


# --- DO NOT EDIT BELOW THIS LINE --- #

class TestCase:
    def __init__(self, problem_number, description, function_under_test, testing_function, number_of_test_cases,
                 docstring_check=True):
        self.num = problem_number
        self.desc = description
        self.func = function_under_test
        self.test = testing_function
        self.cases = number_of_test_cases
        self.doc = docstring_check

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
    # in_vals = ([['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-'],
    #             ['-', '-', '-', '-', '-', '-', '-', '-']],
    #            [['x', '-', '-', '-', '-', '-', '-', '-'],
    #             ['x', '-', '-', '-', '-', '-', 'x', 'x'],
    #             ['x', '-', '-', '-', '-', '-', 'x', '-'],
    #             ['x', '-', '-', '-', '-', '-', 'x', 'x'],
    #             ['x', '-', '-', '-', '-', '-', '-', 'x'],
    #             ['x', '-', '-', '-', '-', '-', '-', 'x'],
    #             ['x', '-', 'x', 'x', '-', '-', '-', 'x'],
    #             ['x', '-', 'x', 'x', '-', 'x', 'x', 'x']],
    #            [['-', '-', '-', 'x', '-', '-', '-', '-'],
    #             ['-', '-', '-', 'x', '-', '-', '-', '-'],
    #             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    #             ['x', 'x', '-', '-', '-', 'x', 'x', 'x'],
    #             ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    #             ['x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],
    #             ['-', '-', '-', 'x', 'x', '-', '-', '-'],
    #             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']])
    # out_vals = False, False, True
    #
    # in_val, out_val = in_vals[val_num], out_vals[val_num]
    # actual_val = function_under_test(in_val)
    # return True if actual_val == out_val else (f"<board_1{chr(ord('a') + val_num)}>", out_val, actual_val)
    return True


def test_2(function_under_test, val_num):
    # assert val_num in range(9), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    # in_vals = ("Richard Paul Astley (born 6 February 1966) is an English singer, songwriter and radio personality.",
    #            "He rose to fame through his association with the production trio Stock Aitken Waterman.",
    #            " winning the 1988 Brit Award for Best British Single.[12]",
    #            "Astley made a comeback in 2007, becoming an Internet phenomenon when the music video for ",
    #            "\"Never Gonna Give You Up\" became integral to the meme known as \"rickrolling\".[6]",
    #            "2016 album 50 debuted in the UK at No. 1.[8]")
    # out_vals = (None, None, None, 12, 34, None, 6, 7, 8)
    #
    # in_val, out_val = in_vals[val_num], out_vals[val_num]
    # try:
    #     actual_val = function_under_test(in_val)
    # except NotImplementedError:
    #     return in_val, out_val, ""
    # return True if actual_val == out_val else (in_val, out_val, actual_val)
    return True


def test_3(function_under_test, val_num):
    # assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    #
    # if (actual_vals := function_under_test("lesson_7_problem_1.json")) is None:
    #     return "<holiday_json>", "tuple(<mean>, <median>, <range>)", actual_vals
    # else:
    #     actual_mean, actual_median, actual_range = actual_vals
    #
    # if isinstance(actual_mean, datetime.datetime):
    #     out_mean = datetime.datetime(year=2020, month=6, day=18).strftime("%m/%d/%Y")
    # else:
    #     out_mean = 169.5
    # if isinstance(actual_median, datetime.datetime):
    #     out_median = datetime.datetime(year=2020, month=6, day=4).strftime("%m/%d/%Y")
    # else:
    #     out_median = 155
    # out_range = 359
    # actual_val = actual_mean, actual_median, actual_range
    # out_val = out_mean, out_median, out_range
    # return True if actual_val != out_val else ("<holiday JSON>", out_val, actual_val)
    return True


def test_4(function_under_test, val_num):
    # import inspect
    # assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    # class NoteStream:
    #
    #     CAN_SHARP = "ACDFG"
    #     CAN_FLAT = "ABDEG"
    #     ACCIDENTALS = dict(flat="b", sharp="#")
    #
    #     def __init__(self, notes, scale=A_MIN_SCALE, wrong_ind=None):
    #         if isinstance(notes, int):
    #             num_of_notes = notes  # variable name manipulation for code clarity
    #             self.__stream = random.choices(scale, k=num_of_notes)
    #             if wrong_ind is not None:
    #                 if self.__stream[wrong_ind] in self._can_only_flat():
    #                     self.__stream[wrong_ind] += self.ACCIDENTALS["flat"]
    #                 elif self.__stream[wrong_ind] in self._can_only_sharp():
    #                     self.__stream[wrong_ind] += self.ACCIDENTALS["sharp"]
    #                 else:
    #                     self.__stream[wrong_ind] += random.choice(tuple(self.ACCIDENTALS.values()))
    #         else:
    #             self.__stream = notes
    #
    #     def __getitem__(self, item):
    #         if inspect.stack()[1].function != "test_4":
    #             raise ValueError("You are not allowed to inspect the note stream from user code!")
    #         return self.__stream[item]
    #
    #     def __len__(self):
    #         return len(self.__stream)
    #
    #     def __str__(self):
    #         return f"<NoteStream: {len(self.__stream)} notes>"
    #
    #     @classmethod
    #     def _can_only_sharp(cls):
    #         return set(cls.CAN_SHARP) - set(cls.CAN_FLAT)
    #
    #     @classmethod
    #     def _can_only_flat(cls):
    #         return set(cls.CAN_FLAT) - set(cls.CAN_SHARP)
    #
    #     def split_stream(self):
    #         mid = len(self.__stream) // 2
    #         left_stream, right_stream = self.__stream[:mid], self.__stream[mid:]
    #         if len(left_stream) > 1:
    #             left_stream = NoteStream(left_stream)
    #         if len(right_stream) > 1:
    #             right_stream = NoteStream(right_stream)
    #         return left_stream, right_stream
    #
    # note_num = 20
    # answer_ind = random.randrange(note_num) if random.randint(0, 10) else None
    # stream = NoteStream(note_num, A_MIN_SCALE, answer_ind)
    # in_val = stream
    # out_val = stream[answer_ind] if answer_ind is not None else None
    # try:
    #     actual_val = function_under_test(stream)
    # except NotImplementedError:
    #     return in_val, out_val, "NotImplementedError"
    # return True if actual_val == out_val else (in_val, out_val, actual_val)
    return True


def test_5(function_under_test, val_num):
    # import string
    # import time
    # time_threshold = 2.5
    #
    # def is_iterable(x):
    #     try:
    #         iter(x)
    #     except TypeError:
    #         return False
    #     else:
    #         return True
    #
    # in_val = random.choices(string.hexdigits.replace("abcdef", "-:-x"), k=10_000_000)
    # start_time = time.time()
    # out_val = function_under_test(in_val)
    # end_time = time.time()
    #
    # if not is_iterable(out_val) or len(out_val) != 10_000_000:
    #     return "[<random_characters>]", "'random_characters'", out_val
    # elif end_time - start_time >= time_threshold:
    #     return "[<random_characters>]", "execution_time < 5 sec", f"execution_time = {time_threshold} sec"
    # else:
    #     return True if "".join(in_val[:10]) == out_val[:10] else (f'{in_val[:10]}...'.replace("]...", " ...]"),
    #                                                               f"{''.join(in_val[:10])}...",
    #                                                               f"{out_val[:10]}")
    return True


tcs = [TestCase(problem_number=1, description="Detect a horizontal line in a Tetris board",
                function_under_test=None, testing_function=test_1, number_of_test_cases=3),
       TestCase(problem_number=2, description="Detect the footnote marker in a text string from Wikipedia",
                function_under_test=None, testing_function=test_2, number_of_test_cases=9),
       TestCase(problem_number=3, description="Calculate basic stats on 2020 Holidays",
                function_under_test=None, testing_function=test_3, number_of_test_cases=1),
       TestCase(problem_number=4, description="Find the offkey note in a stream of notes",
                function_under_test=None, testing_function=test_4, number_of_test_cases=1,
                docstring_check=False),
       TestCase(problem_number=5, description="Efficiently combine a list of characters into one string",
                function_under_test=None, testing_function=test_5, number_of_test_cases=1)]


for tc in tcs:
    print(f"Problem {tc.num}: {tc!s}")

    r, o = tc.run()
    if not r:
        print("FAILED")
        for out_text in o:
            print(f"{out_text}")
    elif tc.doc and not tc.func.__doc__:
        print("FAILED: needs a function docstring")
    else:
        print("PASSED")
