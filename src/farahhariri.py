from collections import defaultdict
import os

def foo(x):
    return x +5

def main():
    print("This statement should always be covered")
    res = foo(9)

    if res > 3:
        res = foo(res)
    else:
        res = foo(res + 8)
    print("THis should also be always printed: " + str(res))
    print(os.path.join("source", "/dest/ina/tion"))
    if res > 3:      
        res = foo(res)
    else:
        res = foo(res + 8)

if __name__ == "__main__":
    main()
