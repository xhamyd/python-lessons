"""
Lesson 8
--------

1) Tetris Line Clear

2) Detect if a string contains a footnote marker

3) Find the mean, median, and range of 2020 holidays using the days within the year as your key metric. BONUS: Plot it!

4) Suppose you have a unsorted stream of note pitch values, all in A minor. Due to a bad programming bug, there can
sometimes be one note in the stream that will randomly be altered out of the scale (i.e. turn into a black key). You
must find this offending note using the following formula:
    - If note_stream is empty, there was no offending note in the stream
        - find_bad_note([]) => None
    - If note_stream has only one note, check if the remaining note is still in the key or not
        - find_bad_note(["A"]) => None
        - find_bad_note(["A#"]) => "A#
    - Else, split the stream in half and run both halves through this function, `or`ing the result together
        - find_bad_note(["E" "F" "G"]) => None
        - find_bad_note(["A" "B" "C" "D#" "E"]) => "D#"

NOTE: You do not need to provide a function docstring for this problem

5) Concatenate list of strings

Topics covered: 2D lists, RegEx, numpy, statistics, recursion, search, optimization, list comprehensions

"""

import datetime

YEAR = 2020
A_MIN_SCALE = "ABCDEFG"


def convert_date_to_number(month, day, year=YEAR):
    holiday_date = datetime.datetime(month=month, day=day, year=year)
    start_date = datetime.datetime(month=1, day=1, year=year)
    return (holiday_date - start_date).days


def convert_number_to_date(day_num, year=YEAR):
    start_date = datetime.datetime(month=1, day=1, year=year)
    days = datetime.timedelta(days=int(day_num))
    return start_date + days

# --- DO NOT EDIT ABOVE THIS LINE --- #


def tetris_line_clear(board):
    pass  # TODO: delete this entire line and complete this function


def footnote_detector(text):
    raise NotImplementedError  # TODO: delete this entire line and complete the function


def holiday_stats(holiday_json="lesson_7_problem_1.json"):
    pass  # TODO: delete this entire line and complete this function


def find_bad_note(note_stream):
    """
    No docstring needed for this problem.

    HINT 1: "E" in A_MIN_SCALE ==> True
            "Db" in A_MIN_SCALE ==> False
    HINT 2: Since you can't manually split the stream into two parts, use the following function for help:
            left_stream, right_stream = note_stream.split_stream()

    """
    raise NotImplementedError  # TODO: delete this entire line and complete the function


def combined_string(str_list):
    pass  # TODO: delete this entire line and complete the function


# --- DO NOT EDIT BELOW THIS LINE --- #
import random


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
    in_vals = ([['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-']],
               [['x', '-', '-', '-', '-', '-', '-', '-'],
                ['x', '-', '-', '-', '-', '-', 'x', 'x'],
                ['x', '-', '-', '-', '-', '-', 'x', '-'],
                ['x', '-', '-', '-', '-', '-', 'x', 'x'],
                ['x', '-', '-', '-', '-', '-', '-', 'x'],
                ['x', '-', '-', '-', '-', '-', '-', 'x'],
                ['x', '-', 'x', 'x', '-', '-', '-', 'x'],
                ['x', '-', 'x', 'x', '-', 'x', 'x', 'x']],
               [['-', '-', '-', 'x', '-', '-', '-', '-'],
                ['-', '-', '-', 'x', '-', '-', '-', '-'],
                ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', '-', '-', '-', 'x', 'x', 'x'],
                ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],
                ['-', '-', '-', 'x', 'x', '-', '-', '-'],
                ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']])
    out_vals = False, False, True

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    actual_val = function_under_test(in_val)
    return True if actual_val == out_val else (f"<board_1{chr(ord('a') + val_num)}>", out_val, actual_val)


def test_2(function_under_test, val_num):
    assert val_num in range(9), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    in_vals = ("Richard Paul Astley (born 6 February 1966) is an English singer, songwriter and radio personality.",
               "He rose to fame through his association with the production trio Stock Aitken Waterman.",
               "His 1987 recording of their song \"Never Gonna Give You Up\" was a number 1 hit single in 25 countries",
               " winning the 1988 Brit Award for Best British Single.[12]",
               "By the time of his retirement in 1993, Astley had sold approximately 40 million records worldwide.[34]",
               "Astley made a comeback in 2007, becoming an Internet phenomenon when the music video for ",
               "\"Never Gonna Give You Up\" became integral to the meme known as \"rickrolling\".[6]",
               "Astley was voted \"Best Act Ever\" by Internet users at the MTV Europe Music Awards 2008,[7] and his ",
               "2016 album 50 debuted in the UK at No. 1.[8]")
    out_vals = (None, None, None, 12, 34, None, 6, 7, 8)

    in_val, out_val = in_vals[val_num], out_vals[val_num]
    try:
        actual_val = function_under_test(in_val)
    except NotImplementedError:
        return in_val, out_val, ""
    return True if actual_val == out_val else (in_val, out_val, actual_val)


def test_3(function_under_test, val_num):
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")

    if (actual_vals := function_under_test("lesson_7_problem_1.json")) is None:
        return "<holiday_json>", "tuple(<mean>, <median>, <range>)", actual_vals
    else:
        actual_mean, actual_median, actual_range = actual_vals

    if isinstance(actual_mean, datetime.datetime):
        out_mean = datetime.datetime(year=2020, month=6, day=18).strftime("%m/%d/%Y")
    else:
        out_mean = 169.5
    if isinstance(actual_median, datetime.datetime):
        out_median = datetime.datetime(year=2020, month=6, day=4).strftime("%m/%d/%Y")
    else:
        out_median = 155
    out_range = 359
    actual_val = actual_mean, actual_median, actual_range
    out_val = out_mean, out_median, out_range
    return True if actual_val != out_val else ("<holiday JSON>", out_val, actual_val)


def test_4(function_under_test, val_num):
    import inspect
    assert val_num in range(1), ValueError(f"TESTING ERROR: Improper test case number provided: {val_num}")
    class NoteStream:

        CAN_SHARP = "ACDFG"
        CAN_FLAT = "ABDEG"
        ACCIDENTALS = dict(flat="b", sharp="#")

        def __init__(self, notes, scale=A_MIN_SCALE, wrong_ind=None):
            if isinstance(notes, int):
                num_of_notes = notes  # variable name manipulation for code clarity
                self.__stream = random.choices(scale, k=num_of_notes)
                if wrong_ind is not None:
                    if self.__stream[wrong_ind] in self._can_only_flat():
                        self.__stream[wrong_ind] += self.ACCIDENTALS["flat"]
                    elif self.__stream[wrong_ind] in self._can_only_sharp():
                        self.__stream[wrong_ind] += self.ACCIDENTALS["sharp"]
                    else:
                        self.__stream[wrong_ind] += random.choice(tuple(self.ACCIDENTALS.values()))
            else:
                self.__stream = notes

        def __getitem__(self, item):
            if inspect.stack()[1].function != "test_4":
                raise ValueError("You are not allowed to inspect the note stream from user code!")
            return self.__stream[item]

        def __len__(self):
            return len(self.__stream)

        def __str__(self):
            return f"<NoteStream: {len(self.__stream)} notes>"

        @classmethod
        def _can_only_sharp(cls):
            return set(cls.CAN_SHARP) - set(cls.CAN_FLAT)

        @classmethod
        def _can_only_flat(cls):
            return set(cls.CAN_FLAT) - set(cls.CAN_SHARP)

        def split_stream(self):
            mid = len(self.__stream) // 2
            left_stream, right_stream = self.__stream[:mid], self.__stream[mid:]
            if len(left_stream) > 1:
                left_stream = NoteStream(left_stream)
            if len(right_stream) > 1:
                right_stream = NoteStream(right_stream)
            return left_stream, right_stream

    note_num = 20
    answer_ind = random.randrange(note_num) if random.randint(0, 10) else None
    stream = NoteStream(note_num, A_MIN_SCALE, answer_ind)
    in_val = stream
    out_val = stream[answer_ind] if answer_ind is not None else None
    try:
        actual_val = function_under_test(stream)
    except NotImplementedError:
        return in_val, out_val, "NotImplementedError"
    return True if actual_val == out_val else (in_val, out_val, actual_val)


def test_5(function_under_test, val_num):
    import string
    import time
    time_threshold = 2.5

    def is_iterable(x):
        try:
            iter(x)
        except TypeError:
            return False
        else:
            return True

    in_val = random.choices(string.hexdigits.replace("abcdef", "-:-x"), k=10_000_000)
    start_time = time.time()
    out_val = function_under_test(in_val)
    end_time = time.time()

    if not is_iterable(out_val) or len(out_val) != 10_000_000:
        return "[<random_characters>]", "'random_characters'", out_val
    elif end_time - start_time >= time_threshold:
        return "[<random_characters>]", "execution_time < 5 sec", f"execution_time = {time_threshold} sec"
    else:
        return True if "".join(in_val[:10]) == out_val[:10] else (f'{in_val[:10]}...'.replace("]...", " ...]"),
                                                                  f"{''.join(in_val[:10])}...",
                                                                  f"{out_val[:10]}")


tcs = [TestCase(problem_number=1, description="Detect a horizontal line in a Tetris board",
                function_under_test=tetris_line_clear, testing_function=test_1, number_of_test_cases=3),
       TestCase(problem_number=2, description="Detect the footnote marker in a text string from Wikipedia",
                function_under_test=footnote_detector, testing_function=test_2, number_of_test_cases=9),
       TestCase(problem_number=3, description="Calculate basic stats on 2020 Holidays",
                function_under_test=holiday_stats, testing_function=test_3, number_of_test_cases=1),
       TestCase(problem_number=4, description="Find the offkey note in a stream of notes",
                function_under_test=find_bad_note, testing_function=test_4, number_of_test_cases=1,
                docstring_check=False),
       TestCase(problem_number=5, description="Efficiently combine a list of characters into one string",
                function_under_test=combined_string, testing_function=test_5, number_of_test_cases=1)]


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
