# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     temperature = []
#     for row in data:
#         temp.append(row[1])
#     del temp[0]
#     for value in temp:
#         integer = int(value)
#         temperature.append(integer)
#     print(temperature)
#
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather-data.csv")
print(data['temp'])
print(type(data))
print(type(data['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

# total_temp = 0
# frequency = 0
# for temperature in temp_list:
#     total_temp += temperature
#     frequency += 1
# Average_temp = total_temp/frequency
# print(Average_temp)
# OR
# Average_temp = sum(temp_list) / len(temp_list)
# print(Average_temp)
# OR
Average_temp = data['temp'].mean()
print(Average_temp)
Max_temp = data['temp'].max()
print(Max_temp)
Min_temp = data['temp'].min()
print(Min_temp)

# Get data in columns
print(data.condition)
# OR
print(data['condition'])

# Get data in rows
print(data[data.day == 'Friday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)
print(((9 * monday.temp) / 5) + 32)

# How to create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65],
}


data2 = pandas.DataFrame(data_dict)
print(data2)

data2.to_csv('new_data.csv')
