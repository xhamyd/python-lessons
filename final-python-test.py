""" The Final Final to Finally Rule Them All! """

"""
1. Create a list with the first 10 positive integer numbers.
    a. Create it in three different ways
        i. One of the ways should be a one-liner solution
    b. Discuss the benefits/cons to each method
    c. If the original problem asked it in a tuple, does each method still work?
    d. If the original problem had a very large amount of numbers to use, does each method still work?

"""

#tuples are immutable (non-modifiable)

def foo():
    num = []
    for i in range(1,11):
        num.append(i)

    return num
        
print(list(i for i in range(1,11) if i % 2 == 0))

# list()
# []
print({1,2,3,4,5,6,7,8,9,10})


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

#each element of a set is unique===

def snek():
    week = dict(Sun=0, Mon=1, Tue=2, Wed=3, Thu=4, Fri=5, Sat=6)

def kurb():
    week_two_baby = {'Sun':0, 'Mon':1, 'Tue':2, 'Wed':3, 'Thu':4, 'Fri':5, 'Sat':6}

def blob():
    week_three = [('Sun', 0), ('Mon', 1), ('Tues', 2), ('Wed', 3), ('Thurs', 4), ('Fri', 5), ('Sat', 6)]
    week_three.sort(key=lambda e: e[0][1])
    sorted(week_three)


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

def hecking_heck(x):
    if x.endswith('.txt'): 
        try:
            with open(x, 'r', encoding='UTF-8') as f:
                falco = f.readlines()

                if len(f.readlines()) == 0:
                    raise EOFError

            return falco

        except FileNotFoundError:
            raise NameError

        except UnicodeError:
            raise ValueError
        
    else:
        print("I hate you, you are the worst")
        print("Would you steal a car?")
        raise ValueError


"""
4. Below is a generated list of input audio samples provided. Your sound card uses their own "audio pumping" function
that takes input audio samples, applies some function to each of them, and outputs the processed samples (in an audio
stack, this output would then be routed to your speakers' drivers). In order to manipulate the audio samples, you must
provide a callback function to this audio pump function, which will apply your function to each of the input samples.
    a. Provide a reference to a function that halves the gain of each sample in a lis.
        - NOTE: In order to provide your function, delete FILL_ME_IN and replace with the syntax-appropriate code
    b. BONUS! Write test cases to check your code

"""
# ---- DO NOT EDIT THIS SECTION (start) ---- #
# [round(x, 2) for x in numpy.sin(range(20))*20]
input_samples = [0.0, 16.83, 18.19, 2.82, -15.14, -19.18, -5.59, 13.14, 19.79,
                 8.24, -10.88, -20.0, -10.73, 8.4, 19.81, 13.01, -5.76, -19.23,
                 -15.02, 3.0]


def audio_pump(samples, process_fn):
    return process_fn(samples)
# ---- DO NOT EDIT THIS SECTION (end) ---- #

def audio_process(input_samples):
    for i in range(0,len(input_samples)):
        halve = input_samples(i)/2
        input_samples.replace(i, halve)

    return input_samples

if audio_process([16.83, 18.19, 2.82]) == [8.415, 9.095, 1.41]:
    print("Good job! You actually did something right for once, numnuts!")
else:
    print("Good job! And by that, I mean, horrible job!")

lambda input_samples: [input_samples[i]/2 for i in range(0,len(input_samples))]

print(audio_pump(input_samples, lambda input_samples: [input_samples[i]/2 for i in range(0,len(input_samples))]))  # TODO: delete FILL_ME_IN and replace with your function pointer


"""
5. Create a tic-tac-toe class that allows for the following code to run successfully.
    a. An instantiation of your class should create an empty game board
        i. A starter __str__ method is provided for you so that you can print out the game board for debugging.
    b. Adding a 3-element tuple (row, col, piece) to your game board should add one player's move to the game board
    c. Subtracting a 2-element tuple (row, col) should remove any game piece at the specified spot from the game board
    d. Create a `is_won()` method that outputs the winner of the game board, if one exists

"""


class TicTacToe:
    def __init__(self, board):
        self.board = board
        board = [" - - - "]

    def __str__(self):
        rows = [" - - - "]
        for row in self.board:
            rows.append(f"|{'|'.join(row)}|")
            rows.append(f" - - - ")
        return "\n".join(rows)

    def add(self):
        self.board = [" - - - ", " - - - ", " - - - "]
        for i in range(0, len(board)):
            for j in range(1, len(board)):
            if i == 0 or i%3 == 0:
                row = board(i)
                if j == 1 or (j-1)%3 == 0:
                    col = board(j)
            

    def subtract(self):
        

    def is_won(self):
        if board.is_won(True):
            print(self.piece + "wins!")

#I'm getting confused just thinking about this one.

board = TicTacToe()
board += (1, 1, "x")
board += (2, 2, "o")
board += (0, 1, "x")
board += (0, 0, "o")
board -= (0, 0)
board += (2, 1, "o")
board += (0, 0, "x")
assert(board.is_won() == "no winners yet")
board += (0, 2, "x")
assert(board.is_won() == "x wins!")
# BONUS!
# board -= (0, 2, "x")
# board -= (1, 1, "x")
# board += (1, 1, "o")
# assert(board.is_won() == "o wins!")

"""
6. Complete the two functions below using best Python practices
    a. The first function asks you to take the input arguments and multiply them together. Return a string with the full
    equation (i.e. "6 * 4 = 24").
        i. Find 3 different ways to create the string to return
        ii. Initially, assume only two input arguments
        iii. Then, accept any number of arguments
    b. The second function asks you to round a floating-point number and return the resulting number as a string.
        i. Rounding is a keyword argument only
            - If not provided, return the number without trailing zeros (i.e. "6.")
        ii. Find 2 different ways to round the number for the resulting string
    c. Write docstrings for both functions
    d. Write test cases for both functions

"""


# spelled_out_multiplication(6, 4) ==> "6 * 4 = 24"
# spelled_out_multiplication(6, 2, 5) ==> "6 * 2 * 5 = 60"
def spelled_out_multiplication(*args):
    """
    This function takes any amount of integers, and will print those integers in spelled out multiplication as one string.

    Args:
        args (tuple): collection of varying number of integers to be multiplied

    Returns:
        str: The string representing the multiplication equation.

    """
    temp = []
    product = 1
    for i in range(len(args)):
        product *= args[i]
        temp.append(args[i])
        temp.append(' * ')
    temp.append(' = ')
    temp.append(str(product))

    return ''.join(temp)

    return str(args[0]) + ' * ' + str(args[1]) + ' = ' + str(args[0]*args[1])
    return f'{args[0]} * {args[1]} = {args[0] * args[1]}'

# rounded_digits(3.1415, rounding=3) ==> "3.142"
# rounded_digits(6.28) ==> "6."
def rounded_digits(f_num, **kwargs):
    pass


"""
7. Given a provided list of common foods, perform set manipulations on the elements
    a. Create at least two unique sets from the provided list. Example set classifications:
        i. `fruits` set, `belongs_in_sandwich` set
        ii. `red` set, `round` set
        iii. `sweet` set, `seeded` set
    b. Use two different ways to remove an element from one of your sets
        i. Discuss the differences between the two methods
    c. Use a built-in set function to find the common elements between both sets
        ex. If A = red_set and B = round_set, then the answer would be {"apple", "tomato"}            
    d. Use a built-in set function to find the elements found uniquely in only one set
        ex. If A = red_set and B = round_set, then the answer would be {"orange", "kiwi", "strawberry"}

"""
class Groups(elements):
    def __init__(self, fruits, belongs_in_sandwich)
    self.fruits = fruits
    self.belongs_in_sandwich = sandwich

    def fruits(self):
        for i in range(0, len(elements)):
            if elements[i] = "apple", "banana", "tomato", "orange", "kiwi" or "strawberry"
                fruits += elements[i]
        str(fruits)
        fruits.join(", ")
        print("These are fruits: " + fruits)

    def belongs_in_sandwich(self);
        for i in range (0, len(elements)):
            if elements[i] = "banana", "tomato", "peanut butter", or "lettuce"
                sandwich += elements[i]
        str(sandwich)
        sandwich.join(", ")
        print("These belong in a sandwich: " + sandwich)

    def remove(self):
        self.remove(element)

    # This way is simpler, but also requires an additional line if something would need to take its place.
        
    def remove_two(self):
        self.replace("i", "j")

    # This way is cooler, and really a pro gamer move.
        
elements = ["apple", "banana", "tomato", "orange", "carrot", "kiwi", "bread", "peanut butter", "lettuce", "strawberry"]

"""
8. In lesson_2.py, you created the `foo()` function that prints integers from 1 to a given input argument. Edit that
Python file to run that function from the command line automatically.
    - ex. `python my_test.py` should run `foo()`
    # if name == main
"""
