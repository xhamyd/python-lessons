""" The Final Final to Finally Rule Them All! """

"""
1. Create a list with the first 10 positive integer numbers.
    a. Create it in three different ways
        i. One of the ways should be a one-liner solution
    b. Discuss the benefits/cons to each method
    c. If the original problem asked it in a tuple, does each method still work?
    d. If the original problem had a very large amount of numbers to use, does each method still work?

"""

"""
2. Create a collection to associate days of the week with their number (i.e. 0 <=> Sun, 1 <=> Mon)
    a. Create it in three different ways
        i. You can use whatever data structure you'd like (with as much documentation as needed)
    b. Sort the collection by day number. Is this possible with each creation method?
    c. Sort it by second letter of the day (i.e. sAturday, wEdnesday, etc.).
        i. You can use Python's built-in sort() and/or sorted() functions
    d. Flip the association (i.e. days -> nums into nums -> days)
        i. A documentation update is not good enough, you should actually flip the days with their respective numbers

"""

"""
3. Write a function to open a file
    a. Handle reading text files
        i. Check if the file doesn't exist (return False)
        ii. Check if the file is even a text file (return False)
        iii. Check if the file is empty (return False)
        iv. Check if the file is even encoded correctly (return False)
    b. If file is readable, return the line number associated with the first line that contains a given word to search
        i. The word to search is a input argument, defaulted to "TODO"
        ii. Perform this search in three different ways
        iii. You may assume the given word to search is only letters (i.e. `[a-zA-Z]+`) 
    c. In this same function, handle reading JSON files
        i. Check if the file doesn't exist (return False)
        ii. Check if the file is even a JSON file (return False)
        iii. Check if the file is empty (return False)
    d. If JSON is parsable, return the sum of all the values in the dictionary
        i. You may assume the following structure: { str: i, str: i, ... }
        ii. BONUS! Allow for nested dictionaries: { str: i, str: { str: i, str: i, ... }, str: i, ... }

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
