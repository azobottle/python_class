class Solution():
    def get_lcm(self, x):
        #请在此添加代码，实现求出给定的所有正整数的最小公倍数，并将其返回
        #********** Begin *********#
        def gcd(x,y):
            return x if y==0 else gcd(y,x%y)
        def lcm(x,y):
            return int(x*y/gcd(x,y))
        for i in range(len(x)-1):
            x[i+1]=lcm(x[i],x[i+1])
        return x[len(x)-1]
        #********** End **********#
        pass