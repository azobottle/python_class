import pandas as pd
import matplotlib.pyplot as plt


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
    fig1 = plt.figure('分析城市气温与海洋距离的关系')
    p1 = fig1.add_subplot()
    p1.set_xlabel('TIME/DAY')
    p1.set_ylabel('TEMPERATURE/°C')

    fig2 = plt.figure('分析城市露点与海洋距离的关系')
    p2 = fig2.add_subplot()
    p2.set_xlabel('TIME/DAY')
    p2.set_ylabel('DEWP/°C')
    for city in city2dist.keys():
        x = range(1, 366)
        y1 = []
        y2 = []
        y21 = []
        y22 = []
        y3 = []
        for day_pieces in list(eight_pieces[city].groupby('DAY')):
            y1.append(day_pieces[1]["TEMPERATURE"].mean())
            y2.append(day_pieces[1]["DEWP"].mean())
            y21.append(day_pieces[1]["WIND-AVG-SPEED"].mean())
            y22.append(day_pieces[1]["WIND-DIRECTION"].mean())
            y3.append(day_pieces[1]["PRESSURE"].mean())
        p1.plot(x, y1, linewidth=1.5, linestyle='-', label=city + '(' + city2dist[city] + ')')
        p2.plot(x, y2, linewidth=1.5, linestyle='-', label=city + '(' + city2dist[city] + ')')

        SD = plt.figure()
        SD.text(0.5, 0, s=city)
        P31 = SD.add_subplot()
        P31.plot(x, y21, linewidth=1.5, linestyle='-', label='WIND-AVG-SPEED', color='r')
        P31.set_ylabel('WIND-AVG-SPEED')
        P32 = P31.twinx()
        P32.plot(x, y22, linewidth=1.5, linestyle='-', label='WIND-DIRECTION', color='y')
        P32.set_ylabel('WIND-DIRECTION')
        P31.set_xlabel('TIME/DAY')
        P31.legend(loc="upper left")
        P32.legend(loc="upper right")

        TP = plt.figure()
        TP.text(0.5, 0, s=city)
        P41 = TP.add_subplot()
        P41.plot(x, y1, linewidth=1.5, linestyle='-', label='TEMPERATURE/°C', color='r')
        P41.set_ylabel('TEMPERATURE/°C')
        P42 = P41.twinx()
        P42.plot(x, y3, linewidth=1.5, linestyle='-', label='PRESSURE/KPa', color='y')
        P42.set_ylabel('PRESSURE/KPa')
        P41.set_xlabel('TIME/DAY')
        P41.legend(loc="upper left")
        P42.legend(loc="upper right")

    p1.legend()
    p2.legend()
    plt.show()


if __name__ == '__main__':
    main()
