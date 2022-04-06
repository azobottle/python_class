import os
import re

mydict = {}


def fact(path):
    # 在下方填充代码，注释掉pass
    # pass
    global mydict
    for t in os.listdir(path):
        sub_path = os.path.join(path, t)
        if not os.path.isfile(sub_path):
            fact(sub_path)
        else:
            f = open(sub_path, 'r', encoding="ISO-8859-15")
            mylist = f.readlines()

            for line in mylist:
                line = line.lower()
                for word in re.split("[^a-z]", line):
                    if word in mydict.keys():
                        mydict[word] += 1
                    elif word != '':#stranggggggggggggggggge
                        mydict[word] = 1
            f.close()
    return mydict


# 主函数
if __name__ == '__main__':
    # 示例:
    print(fact('./email/'))
