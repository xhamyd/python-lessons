""" The Final Final to Finally Rule Them All! """

"""
1. Create a list with the first 10 positive integer numbers.
    a. Create it in three different ways
        i. Create a one-liner solution
    b. Discuss the benefits/cons to each method
    c. Switch the container into a tuple, does each method work?
    d. What if we have unlimited amount of elements?

"""

print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
res = []
for i in range(1, 11):
    res.append(i)
print(res)
print([x+1 for x in range(10)])

print(tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
res = []
for i in range(1, 11):
    res.append(i)
print(tuple(res))
print(tuple(x+1 for x in range(10)))

"""
2. Create a collection to associate days of the week with their number (i.e. 0 <=> Sun, 1 <=> Mon)
    a. Create it in three different ways
    b. Sort it by day number
    c. Sort it by second letter of the day (i.e. sAturday, wEdnesday, etc.)
    d. Flip the association (i.e. days -> nums into nums -> days)

"""

print(dict(Sun=0, Mon=1, Tues=2, Wed=3, Thurs=4, Fri=5, Sat=6))
days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
nums = [0, 1, 2, 3, 4, 5, 6]
print({day: num for (day, num) in zip(days, nums)})
res = []
for i in range(len(days)):
    day, num = days[i], nums[i]
    t = (day, num)
    res.append(t)
print(res)

# Dictionaries cannot be sorted... unless using OrderedDicts (out-of-scope)
res.sort(key=lambda e: e[1])
print(res)

res.sort(key=lambda e: e[0][1])
print(res)

# cannot use integer keys with dict constructor
print({num: day for (day, num) in zip(days, nums)})
res = []
for i in range(len(days)):
    day, num = days[i], nums[i]
    t = (num, day)
    res.append(t)
print(res)

"""
3. Write a function to open a file
    a. Handle reading text files
    b. Find the first line that has the given word in three different ways
        i. Default word to search: "TODO"
    c. Check if the file doesn't exists, is empty, is a text file, and if encoded correctly
    d. Handle reading JSON files

"""
import json


def open_any_file(fp, search_word="TODO"):
    lines = json_dict = None
    try:
        with open(fp, "r", encoding="utf-8") as f:
            if fp.endswith(".txt"):
                lines = f.readlines()
            elif fp.endswith(".json"):
                json_dict = json.load(f)
            else:
                print("Unacceptable file extension")
                return False
    except FileExistsError:
        print("File doesn't exist")
        return False
    except UnicodeError:
        print("File couldn't be read")
        return False
    if lines is not None:
        if lines:
            return lines
        else:
            print("File is empty")
            return False
    elif json_dict:
        return json_dict


def dict_sum(d):
    if isinstance(d, int):
        return d
    else:
        return sum(dict_sum(val) for val in d.values())

# with open("test.txt", "wb") as f:
#     f.write(bytes((0xB3, 0xA5, 0x07, 0x1F)))
a = dict(boo=6, nah=dict(a=12, b=5), whoops=-1)
print(a, dict_sum(a))

"""
4. Provide a callback function to halve the gain of each sample when processing

"""
# [round(x, 2) for x in numpy.sin(range(20))*20]
input_samples = [0.0, 16.83, 18.19, 2.82, -15.14, -19.18, -5.59, 13.14, 19.79,
                 8.24, -10.88, -20.0, -10.73, 8.4, 19.81, 13.01, -5.76, -19.23,
                 -15.02, 3.0]


def audio_pump(samples, process_fn):
    return process_fn(samples)


print(audio_pump(input_samples, lambda sample_list: [0.5*sample for sample in sample_list]))


"""
5. Write a tic-tac-toe class

"""


class TicTacToe:

    def __init__(self):
        self.board = self._create_initial_board()

    def __str__(self):
        rows = [" - - - "]
        for row in self.board:
            rows.append(f"|{'|'.join(row)}|")
            rows.append(f" - - - ")
        return "\n".join(rows)

    def is_won(self):
        hori_rows = [row for row in self.board]
        vert_rows = [[self.board[c][r] for c in range(len(self.board[r]))] for r in range(len(self.board))]
        # assuming square board
        diag_rows = [[self.board[r][r] for r in range(len(self.board))],
                     [self.board[r][len(self.board)-1-r] for r in range(len(self.board))]]

        for rows in (hori_rows, vert_rows, diag_rows):
            for row in rows:
                if all(p == "x" for p in row):
                    return "x wins!"
                elif all(p == "o" for p in row):
                    return "o wins!"
        return "No winner yet..."

    @staticmethod
    def _create_initial_board():
        return [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

    def __add__(self, other):
        if not isinstance(other, tuple) or len(other) != 3:
            raise ValueError

        r, c, t = other
        assert(self.board[r][c] == " "), f"Not an empty space, cannot add \"{t}\" to the board"
        self.board[r][c] = t
        return self

    def __sub__(self, other):
        if not isinstance(other, tuple) or len(other) != 2:
            raise ValueError

        r, c = other
        assert(self.board[r][c] != " "), f"Space is empty, nothing to remove from the board"
        self.board[r][c] = " "
        return self


board = TicTacToe()
board += (1, 1, "x")
board += (2, 2, "o")
board += (0, 1, "x")
board += (0, 0, "o")
board -= (0, 0)
board += (2, 1, "o")
board += (0, 0, "x")
board += (0, 2, "x")
print(board.is_won())

"""
6. String formatting
    a. Print out multiplication equations in 3 ways
        i. Initially, assume two input arguments
        ii. Then accept any number of arguments
    b. Print out the rounded digits of a float in 2 ways
        i. Rounding is a keyword argument only. If not provided, do not have trailing zeros (i.e. "6.")
    c. Write docstring for both functions
    d. Write test cases for both functions

"""


def spelled_out_multiplication(*args):
    from math import prod
    product = prod(arg for arg in args)
    str_args = (str(arg) for arg in args)
    return f"{' * '.join(str_args)} = {product}"


def rounded_digits(f_num, **kwargs):
    if "rounding" in kwargs:
        return f"{f_num:.{kwargs['rounding']}f}"
    else:
        return f"{f_num:d}."


assert(spelled_out_multiplication(6, 4) == "6 * 4 = 24")
assert(rounded_digits(3.1415, rounding=3) == "3.142")

"""
7. Sets
    a. Create sets from a list of elements
    b. Remove an element from the set in 2 ways (pros/cons)
    c. Find the elements in both sets
    d. Find the elements in only one of the sets

"""
elements = ["apple", "banana", "tomato", "orange", "carrot", "kiwi", "bread", "peanut butter", "lettuce"]
fruits = {"apple", "banana", "tomato", "orange", "kiwi"}
sandwich = set()
sandwich.add("tomato")
sandwich.add("bread")
sandwich.add("lettuce")
sandwich.add("peanut")
sandwich.add("banana")
fruit = fruits.pop()
fruits.discard("tomato")
sandwich.add(fruit)  # for demonstration
fruits.add(fruit)
print(sandwich & fruits)  # sandwich.intersection(fruits)
print(sandwich ^ fruits)  # sandwich.symmetric_difference(fruits)

"""
8. How can I tell python to run a given function in my file automatically?
    - ex. `python my_test.py`

"""

if __name__ == "__main__":
    abc()
