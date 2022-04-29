# 示例：
# #设置列表lst中位置3的值为1
# lst_
# 根据注释中说明可知，此处"_"应替换成[3]=1,即有
# lst[3]=1
#请先将下面的代码复制到答题框，注意添加缩进

# 导入相关的包
import pandas as pd
import numpy as np
from numpy import nan as NA

def fact():
    answer = []

    df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
    df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

    # 指定key这一列取交集
    dataframe1 = pd.merge(df1,df2,on='key')

    answer.append(dataframe1)

    # 取df1和df2的交集
    dataframe2 = pd.merge(df1,df2)

    answer.append(dataframe2)

    # 取左连接，df1左连接df2
    dataframe3 = pd.merge(df1,df2,how='left')

    answer.append(dataframe3)

    df3 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
    df4 = pd.DataFrame({"rkey": ["a", "b", "d"], "data2": range(3)})

    # 取df3，df4的交集
    dataframe4 = pd.merge(df3,df4,left_on='lkey',right_on='rkey')

    answer.append(dataframe4)

    s1 = pd.Series([0, 1], index=["a", "b"])
    s2 = pd.Series([2, 3, 4], index=["c", "d", "e"])
    s3 = pd.Series([5, 6], index=["f", "g"])

    # 将多个Series拼接成一个DataFrame,即一个Series就是DataFrame的一列数据
    dataframe5 = pd.concat([s1,s2,s3])

    answer.append(dataframe5)


    df5 = pd.DataFrame({"a": [1, NA, 5, NA], "b": [NA, 2, NA, 6], "c": range(2, 18, 4)})
    df6 = pd.DataFrame({"a": [5, 4, NA, 3, 7], "b": [NA, 3, 4, 6, 8]})

    # 用df6的数据为df5中的数据打补丁
    dataframe6 = df5.combine_first(df6)

    answer.append(dataframe6)

    data = pd.DataFrame(np.arange(6).reshape(2, 3), index=pd.Index(["上海", "北京"], name="省份"),
    columns=pd.Index([2011, 2012, 2013], name="年份"))
    # 将data的列所引转换到行索引
    result1 = data.stack()

    answer.append(result1)

    # 将result1的行索引转化为列索引
    result2 = result1.unstack()

    answer.append(result2)

    # 将result1的行索引转化为列索引，指定要转化为层次化索引的名称为"省份"
    result3 = result1.unstack(0)

    answer.append(result3)

    data1 = pd.DataFrame({"k1": ["one"] * 3 + ["two"] * 4, "k2": [1, 1, 2, 3, 3, 4, 4]})
    # 使用DataFrame的内置函数去除重复数据，默认保留第一次出现的值
    result4 = data1.drop_duplicates()

    answer.append(result4)

    return answer

fact()

# 导入相关的包
import pandas as pd
import numpy as np
from numpy import nan as NA

def fact():
    answer = []

    df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
    df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

    # 指定key这一列取交集
    dataframe1 = pd.merge(df1,df2,on="key")

    answer.append(dataframe1)

    # 取df1和df2的交集
    dataframe2 =pd.merge(df1,df2)

    answer.append(dataframe2)

    # 取左连接，df1左连接df2
    dataframe3 = pd.merge(df1,df2,how='left')

    answer.append(dataframe3)

    df3 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
    df4 = pd.DataFrame({"rkey": ["a", "b", "d"], "data2": range(3)})

    # 取df3，df4的交集
    dataframe4 =pd.merge(df3,df4)

    answer.append(dataframe4)

    s1 = pd.Series([0, 1], index=["a", "b"])
    s2 = pd.Series([2, 3, 4], index=["c", "d", "e"])
    s3 = pd.Series([5, 6], index=["f", "g"])

    # 将多个Series拼接成一个DataFrame,即一个Series就是DataFrame的一列数据
    dataframe5 = pd.concat(s1,s2,s3)

    answer.append(dataframe5)


    df5 = pd.DataFrame({"a": [1, NA, 5, NA], "b": [NA, 2, NA, 6], "c": range(2, 18, 4)})
    df6 = pd.DataFrame({"a": [5, 4, NA, 3, 7], "b": [NA, 3, 4, 6, 8]})

    # 用df6的数据为df5中的数据打补丁
    dataframe6 =df5.combine_first(df6)

    answer.append(dataframe6)

    data = pd.DataFrame(np.arange(6).reshape(2, 3), index=pd.Index(["上海", "北京"], name="省份"),columns=pd.Index([2011, 2012, 2013], name="年份"))
    # 将data的列所引转换到行索引
    result1 =data.reset_index("columns")

    answer.append(result1)

    # 将result1的行索引转化为列索引
    result2 =result1.reset_index()

    answer.append(result2)

    # 将result1的行索引转化为列索引，指定要转化为层次化索引的名称为"省份"
    result3 = result1.unstack(0)

    answer.append(result3)

    data1 = pd.DataFrame({"k1": ["one"] * 3 + ["two"] * 4, "k2": [1, 1, 2, 3, 3, 4, 4]})
    # 使用DataFrame的内置函数去除重复数据，默认保留第一次出现的值
    result4 = data1.drop_duplicates()

    answer.append(result4)

    return answer