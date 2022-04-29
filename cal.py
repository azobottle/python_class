import math


def sigmoid(x):
    return 1/(1+math.exp(-x))

def dao(x):
    return x*(1-x)

if __name__ == '__main__':
    while True:
        print("1 for sigmoid 2 for dao")
        n=int(input())
        if n==1:
            print("sigmoid")
            print(sigmoid(float(input())))
        else:
            print("dao")
            print(dao(float(input())))