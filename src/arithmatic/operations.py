import re


def add(a , b):
    return a + b 

def subtract(a , b):
    return a - b 

if __name__ == '__main__':
    assert add(3, 4) == 7
    assert subtract(3, 4) == -1 
    print("Done")