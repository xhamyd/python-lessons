def nth_fibonacci(x):
    start = 1
    end = x
    
    a = 0
    b = 1
    c = a + b
    while start < end:
        a = b
        b = c
        c = a + b
        start += 1
        
    return c


# fib(x) = fib(x-1) + fib(x-2)
assert nth_fibonacci(4) == 3

for x in range(10):
    print(x)
    
x = 0
while x < 10:
    print(x)
    x = x + 1
