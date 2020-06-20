def fluff(x):
    for i in range(1,x+1): #range is iterable
        print(i)

fluff(5)

print(list(range(1,5)))

integers = [1, 2]
boolean = [False]

print(integers + boolean)

print(len([3, 4, 5]))

poof = [3, 4, 5]

print((poof[1]))

print(poof.index(5))

print(poof[-5%3])

#key-value pairs
brickionary = {1:25, "Jason":-99,}
brickionary["Jason"] = abs(brickionary["Jason"])
del brickionary["Jason"]
brickionary ["jason"] = -99 #adding new key and value
            
print(brickionary)

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def nth_fibonacci(x):
    return fib[x-1]

print(nth_fibonacci(4))

#brackets for element in list and brickionary, paranthesse for everything else. How does one spell parentheses?? There are exceptions to this rule.
assert nth_fibonacci(4) == 3
assert nth_fibonacci(5) == 5
assert nth_fibonacci(6) == 8
assert nth_fibonacci(7) == 13
assert nth_fibonacci(8) == 21
assert nth_fibonacci(9) == 34

print(nth_fibonacci(4))

    
