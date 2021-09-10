def add(a, b):
    return a + b


print(__name__)     # if mymath file runs then __name__ becomes __main__
if __name__ == "__main__":
    print(add(10, 16))
# this checks whether mymath file is running then it prints 10+16
