# coding=utf-8

# 输入一个整数n
import math

n =  int(input())

# 请在此添加代码，对输入的整数进行判断，如果是素数则输出为True，不是素数则输出为False
########## Begin ##########
def prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

########## End ##########
print(prime(n))

