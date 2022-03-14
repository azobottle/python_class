# def fact(N,M):

# def is_prime(N):

# 加提示
# 在下方填充代码，注释掉pass
# pass
import math


def fact(inputmap):
    for i in range(len(inputmap)):
        for j in range(len(inputmap[i])):
            if (i > 0) & (j > 0):
                if inputmap[i - 1][j] > inputmap[i][j - 1]:
                    inputmap[i][j] += inputmap[i][j - 1]
                else:
                    inputmap[i][j] += inputmap[i - 1][j]
            elif i > 0:
                inputmap[i][j] += inputmap[i - 1][j]
            elif j > 0:
                inputmap[i][j] += inputmap[i][j - 1]
    return inputmap[len(inputmap) - 1][len(inputmap[0]) - 1]


'''
def isprime(n):
    flag = True
    if n == 2:
        return flag
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                flag = False
                break
    return flag
'''

if __name__ == '__main__':
    map = [[1, 3, 4], [2, 1, 2], [4, 3, 1]]
    print(fact(map))
