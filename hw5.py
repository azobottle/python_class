# 最小栈类
class fact:
    total = 0 # 记录构造实例的个数
    # 初始化
    def __init__(self):
        fact.total += 1
        self.stack = [] # 存储栈中的元素
        self.min = None # 栈中最小的值

    # 压栈
    def push(self, num):
        return self.stack.append(num)

    # 弹栈
    def pop(self):
        return self.stack.pop()

    # 取栈顶的值
    def top(self):
        return self.stack[len(self.stack)-1]

    # 返回栈中最小的值
    def getMin(self):
        return min(self.stack)

    # 定义类方法getClassTotal(minStack),返回total的值
    @classmethod
    def getClassTotal(cls):
        return cls.total
    # 定义静态方法getStaticTotal(), 返回total的值
    @staticmethod
    def getStaticTotal():
        return fact.total

