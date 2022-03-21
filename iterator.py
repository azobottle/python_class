List = []
member = input()
for i in member.split(','):
    result = i
    List.append(result)
# 请在此添加代码，将List转换为迭代器的代码
# ********** Begin *********#
IterList = iter(List)
# ********** End **********#
while True:
    try:
        # 请在此添加代码，用next()函数遍历IterList的代码
        # ********** Begin *********#
        num = next(IterList)
        # ********** End **********#
        result = int(num) * 2
        print(result)
    except StopIteration:
        break


