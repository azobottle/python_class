import pandas as pd


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
    seven_pieces = dict(list(df.groupby('CITY')))
    for city in city2dist.keys():
        #small_pieces = seven_pieces[city].groupby(myfunc, axis=0)
        #print(seven_pieces[city])
        for day_pieces in list(seven_pieces[city].groupby('DAY')):
            print(day_pieces)


if __name__ == '__main__':
    main()