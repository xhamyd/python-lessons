def nth_fibonacci():
    nth_term = int(input("What term? "))
    n1, n2 = 0, 1
    count = 0
    if nth_term > 0:
        while count < nth_term:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
    
        print(n1)
        
    else:
        print("Start from 1st term")

while True:
    nth_fibonacci()

