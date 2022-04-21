# 从pandas库导入Series,DataFrame
from pandas import Series, DataFrame

def fact():
    answer =[]
    # 创建列表lst
    lst = [4, 7, -5, 3]

    # 使用列表list生成Series对象obj
    obj =Series(lst)
    answer.append(obj.copy())

    # 创建数组index
    index1 = ['d', 'b', 'a', 'c']

    # 创建数据为lst，索引为index1的Series对象obj2
    obj2=Series(lst,index=index1)
    answer.append(obj2.copy())

    # 将obj2中索引值为d对应的值赋值为6
    obj2['d']=6
    answer.append(obj2.copy())

    # 将obj2中索引值为d对应的值存储到ans1中
    ans1=obj2['d']
    answer.append(ans1)

    # 从obj2找出大于0的元素并存储到ans2中
    ans2=obj2[obj2<0]
    answer.append(ans2)

    # 创建字典sdata
    sdata = {'Ohio': 45000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

    # 利用sdata生成Series对象obj3
    obj3= Series(sdata)
    answer.append(obj3.copy())

    # 创建列表states
    states = ['California', 'Ohio', 'Oregon', 'Texas']

    # 创建数据为sdata，索引为states的Series对象obj4
    obj4= Series(sdata,index=states)
    answer.append(obj4.copy())

    # 将obj3和obj4进行相加，相同索引部分相加，存储到obj5
    obj5 = Series(obj3,obj4)
    answer.append(obj5.copy())

    # 指定obj4的名字为population
    obj4.name='population'
    answer.append(obj4.copy())

    # 指定obj4的索引的名字为state
    obj4.index.name='state'
    answer.append(obj4.copy())
    return answer