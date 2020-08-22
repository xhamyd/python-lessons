# greeting = "Hello World"
# print(greeting)
#
# print(80 / 5.)


def foo():
    # start=1, end=20, step=1
    # 1:1:20 -> [1,2,3,4,5,...,20]
    res = []
    for counter in range(1, 20, 1):  # python will start from 0 if default
        res.append(counter)
    return res


if __name__ == "__main__":
    print(__name__, type(__name__))
    print(foo())

foo()
