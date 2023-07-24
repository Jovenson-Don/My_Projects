# import pandas
#
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

# print(temp_list)
print(data["temp"].max())

print(data.condition)
print(data[data["condition"] == "Sunny"])
fur_color = data[data["Primary Fur Color"] == "Gray"]

# print(data[data.day == "Sunday"])
# print(data[data.temp == data.temp.max()])
#
monday = data[data.day == "Monday"]
print(monday.temp)
#
# fahrenheit = monday.temp * 1.8 + 32
# print(fahrenheit)
#
# data_dict = {
#     "student": ["Amy", "Joey", "Don"],
#     "scores": [72, 100, 99]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
#
# print(data)

# import pandas
#
# TOTAL_GRAY = 0
# TOTAL_BLACK = 0
# TOTAL_RED = 0
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = data["Primary Fur Color"].to_list()
#
# for squirrel in fur_color:
#     if squirrel == "Gray":
#         TOTAL_GRAY += 1
#     elif squirrel == "Cinnamon":
#         TOTAL_RED += 1
#     elif squirrel == "Black":
#         TOTAL_BLACK += 1
#
#
# squirrel_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [f"{TOTAL_GRAY}", f"{TOTAL_RED}", f"{TOTAL_BLACK}"]
# }
#
# new_data = pandas.DataFrame(squirrel_dict)
# new_data.to_csv("squirrel_count.csv")

# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = data[data["Primary Fur Color"] == "Gray"]
# print(fur_color)
