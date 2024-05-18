import pandas

data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
gray_count = 0
cinnamon_count = 0
black_count = 0
for color in data['Primary Fur Color']:
    # print(type(color))
    if color == 'Gray':
        gray_count += 1
    elif color == 'Cinnamon':
        cinnamon_count += 1
    elif color == 'Black':
        black_count += 1

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_count, cinnamon_count, black_count]
}

pandas.DataFrame(data_dict).to_csv('squirrel_count.csv')
