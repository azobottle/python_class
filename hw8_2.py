from pandas import Series, DataFrame

def fact():

    answer = []
    # 创建字典data
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

    # 创建列表col，index1
    col = ['year', 'state', 'pop', 'debt']
    index1 = ['one', 'two', 'three', 'four', 'five']

    # 利用data创建DataFrame对象frame1,并指定该对象列为col，索引为index1
    frame1 = DataFrame(data,columns=col,index=index1)
    answer.append(frame1.copy())

    # 排序
    # 根据索引，对frame1进行降序排序，并指定轴为1
    frame2 = frame1.sort_index(axis=1,ascending=False)
    answer.append(frame2.copy())

    # 根据值，对frame1的year列进行排序(升序）并打印
    frame3 = frame1.sort_values(by='year',ascending=True)
    answer.append(frame3.copy())

    # 处理缺失数据
    # 对于frame1，只要有某行有NaN就全部删除
    frame4 = frame1.dropna()
    answer.append(frame4.copy())

    # 对于frame1，某行全部为NaN才删除
    frame5 = frame1.dropna(how='all')
    answer.append(frame5.copy())

    # 填充缺失数据
    # 对于frame1，将元素为NaN替换成0
    frame6 = frame1.fillna(0)
    answer.append(frame6.copy())

    return answer