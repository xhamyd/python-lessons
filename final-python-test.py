""" The Final Final to Finally Rule Them All! """

"""
1. Create a list with the first 10 positive integer numbers.
    a. Create it in three different ways
        i. Create a one-liner solution
    b. Discuss the benefits/cons to each method
    c. Switch the container into a tuple, does each method work?
    d. What if we have unlimited amount of elements?

"""

"""
2. Create a collection to associate days of the week with their number (i.e. 0 <=> Sun, 1 <=> Mon)
    a. Create it in three different ways
    b. Sort it by day number
    c. Sort it by second letter of the day (i.e. sAturday, wEdnesday, etc.)
    d. Flip the association (i.e. days -> nums into nums -> days)

"""

"""
3. Write a function to open a file
    a. Handle reading text files
    b. Find the first line that has the given word in three different ways
        i. Default word to search: "TODO"
    c. Check if the file doesn't exists, is empty, is a text file, and if encoded correctly
    d. Handle reading JSON files

"""

"""
4. Provide a callback function to halve the gain of each sample when processing.
    a. Write test cases to check your function

"""
# [round(x, 2) for x in numpy.sin(range(20))*20]
input_samples = [0.0, 16.83, 18.19, 2.82, -15.14, -19.18, -5.59, 13.14, 19.79,
                 8.24, -10.88, -20.0, -10.73, 8.4, 19.81, 13.01, -5.76, -19.23,
                 -15.02, 3.0]


def audio_pump(samples, process_fn):
    return process_fn(samples)


print(audio_pump(input_samples, FILL_ME_IN))


"""
5. Write a tic-tac-toe class

"""


class TicTacToe: pass


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


# spelled_out_multiplication(6, 4) ==> "6 * 4 = 24"
# spelled_out_multiplication(6, 2, 5) ==> "6 * 2 * 5 = 60"
def spelled_out_multiplication(*args):
    pass


# rounded_digits(3.1415, rounding=3) ==> "3.142"
# rounded_digits(6.28) ==> "6."
def rounded_digits(f_num, **kwargs):
    pass


"""
7. Sets
    a. Create sets from a list of elements
    b. Remove an element from the set in 2 ways (pros/cons)
    c. Find the elements in both sets
    d. Find the elements in only one of the sets

"""

elements = ["apple", "banana", "tomato", "orange", "carrot", "kiwi", "bread", "peanut butter", "lettuce"]

"""
8. How can I tell python to run a given function in my file automatically?
    - ex. `python my_test.py`
    
"""
# my_test.py


def abc():
    print("ABC!")
