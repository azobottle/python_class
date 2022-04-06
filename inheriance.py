class Demo:
    pass


t = Demo()


def mytest(self, v):
    self.value = v


t.test = mytest
print(t.test)
