import pandas as pd
import matplotlib.pyplot as plt


def myfunc(dict):
    return dict["DATE"].split('T')[0]


def main():
    df = pd.read_excel("D:\python_class\Experiment\weatherData.xlsx")
    f = open("D:\python_class\Experiment\distance.txt", 'r')
    city2dist = {}
    tem_list = f.readlines()

    day_append = []
    distance_append = []
    for i in tem_list:
        list_str = i.replace('\n', '').split('  ', maxsplit=1)
        list_str[1] = list_str[1].strip(' ')
        if list_str[0] == 'CHICAGO':
            list_str[0] += ' '
        city2dist[list_str[0]] = list_str[1]
    for index, row in df.iterrows():
        distance_append.append(city2dist[row['CITY']])
        day_append.append(row['DATE'].split('T')[0])
    df["DISTANCE"] = distance_append
    df["DAY"] = day_append

    print(df)
    eight_pieces = dict(list(df.groupby('CITY')))
    fig1 = plt.figure('分析城市气温、露点与海洋距离的关系')  # 2x4
    fig1.text(0.3, 0.95, 'Red for TEMPERATURE,Blue for DEWP', color='y')
    fig2 = plt.figure('分析每个城市的风速和风向的分布情况')  # 2x4
    fig2.text(0.3, 0.95, 'Red for WIND-AVG-SPEED,Blue for WIND-DIRECTION', color='y')
    fig3 = plt.figure('分析气温和气压的关系')  # 2x4
    fig3.text(0.3, 0.95, 'Red for TEMPERATURE,Blue for PRESSURE', color='y')
    cnt = 1
    for city in city2dist.keys():
        # small_pieces = eight_pieces[city].groupby(myfunc, axis=0)
        # print(eight_pieces[city])
        x = range(1, 366)
        y11 = []
        y12 = []
        y21 = []
        y22 = []
        y3 = []
        for day_pieces in list(eight_pieces[city].groupby('DAY')):
            y11.append(day_pieces[1]["TEMPERATURE"].mean())
            y12.append(day_pieces[1]["DEWP"].mean())
            y21.append(day_pieces[1]["WIND-AVG-SPEED"].mean())
            y22.append(day_pieces[1]["WIND-DIRECTION"].mean())
            y3.append(day_pieces[1]["PRESSURE"].mean())
        p1 = fig1.add_subplot(2, 4, cnt)
        p1.plot(x, y11, '*', color='r')
        p1.plot(x, y12, '.', color='b')
        p1.set_title(city)

        p21 = fig2.add_subplot(2, 4, cnt)
        p21.scatter(x, y21, color='r')
        p21.set_title(city)
        p22 = p21.twinx()
        p22.plot(x, y22, color='b')

        p31 = fig3.add_subplot(2, 4, cnt)
        p31.plot(x, y11, '*', color='r')
        p32 = p31.twinx()
        p32.plot(x, y3, color='b')

        cnt += 1
    plt.show()


if __name__ == '__main__':
    main()
