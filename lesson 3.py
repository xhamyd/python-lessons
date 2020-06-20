# print "even" if x is even, "odd" if not

x = 29
if x%2 == 0: #conditional
    print("even")
else:
    print("odd")

# print "my favorite" if x is even, "matthew's favorite" if x is negative, "no one's favorite" otherwise
x = -6
if x%2 == 0:
    print("my favorite")
elif x<0:
    print("matthew's favorite")
else:
    print("no one's favorite")
    
if x<0:
    print("matthew's favorite")
elif x%2 == 0:
    print("my favorite")
else:
    print("no one's favorite")

# is_even(6) ==> True# is_even(3) ==> False

input = x
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(6))
print(is_even(3))

    
#def is_even(x): return x % 2 == 0

#except ZeroDivisionError:

#list_name[1,2,3,4,5]

for x in range(1,21):
     print(x)
# for when you know how many times you repeat


x=1
while x<=20:
    print(x)
    x=x+1
# for when you know the ending point

def fizzbuzz(x):
    if x%15==0:
        print("fizzbuzz")
    elif x%3==0:
        print("fizz")
    elif x%5==0:
        print("buzz")
    else:
        print(x)

for x in range(1,101):
    fizzbuzz(x)
