'''
输入y继续，n结束
输入方程个数n
循环n次
输入n+1个数
'''
import numpy as np
import sys


def xiaoqu(arr, n, eps):
    for i in range(n):
        mymax = sys.float_info.min
        mymax_index = 0
        if i != 0:
            for j in range(i, n):  # 从第i行开始，对第i列元素做减法
                arr[j, i] -= sum(arr[j, 0:i] * arr[0:i, i].T)

        for j in range(i, n):
            if abs(arr[j, i]) > abs(mymax):
                mymax_index = j
                mymax = arr[j, i]
        if abs(mymax) < eps:
            return False
        else:  # 已得到最大值的下标
            arr[[i, mymax_index], :] = arr[[mymax_index, i], :]
            for k in range(i + 1, n):  # 对第i列的元素做除法（L）
                arr[k, i] /= mymax
            if i != 0:
                for k in range(i + 1, n + 1):  # 对第i行的元素做减法（U)
                    arr[i, k] -= sum(arr[i, 0:i] * arr[0:i, k].T)
    return True


def huidai(arr, n):
    ans = np.zeros((1, n))
    for i in range(n - 1, -1, -1):
        ans[0, i] = (arr[i, n] - sum(sum(ans * arr[i, 0:n]))) / arr[i, i]
    return ans


def main():
    print('使用列主元消去法解方程组')
    while True:
        print('输入(y/n)以决定是否计算')
        f = input()
        if f == 'y' or f == 'Y':
            print('输入方程组中方程的个数', end='')
            n = int(input())
            arr = np.zeros((n, n + 1))
            for i in range(n):
                print('输入第' + str(i + 1) + '个方程(数字之间用空格隔开)')
                arr[i] = list(map(float, input().split(' ')))
            print('原方程组为:')
            print(arr)
            print('输入eps')
            eps = float(input())
            if xiaoqu(arr, n, eps):
                print('解为:')
                print(huidai(arr, n)[0, :])
            else:
                print('该方程组不存在唯一解')
        elif f == 'n' or f == 'N':
            break
        else:
            print(f + '为非法输入')
            continue
    print('计算结束')


if __name__ == '__main__':
    main()
