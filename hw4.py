def fact():
    answer = []
    # 字典dictionary
    # 根据{'Beijing':'010','Guangzhou':'020'} 创建字典对象dict
    mydict = {'Beijing': '010', 'Guangzhou': '020'}
    answer.append(mydict.copy())

    # 添加{'Shanghai':'021'}元素
    mydict['Shanghai'] = '021'
    answer.append(mydict.copy())

    # 判断dict是否存在'Shenzhen'这个key，并将结果存到tag中
    tag = mydict.get('Shenzhen')

    return answer, tag
