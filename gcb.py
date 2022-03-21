# coding=utf-8

# 输入两个正整数a,b
a = int(input())
b = int(input())


# 请在此添加代码，求两个正整数的最大公约数
########## Begin ##########
def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    while x % y != 0:
        t = y
        y = x % y
        x = t
    return y


########## End ##########

# 调用函数，并输出最大公约数
if __name__ == '__main__':
    print(gcd(a, b))
