import pandas
import csv

# with open("./weather_data.csv",mode="r")as file:
#     data = file.readlines()
#     print(data)


# with open("./weather_data.csv")as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# length = len(temp_list)
# cnt=0
# for i in temp_list:
#     cnt = cnt+ i
# print(cnt/length)

# print(data["temp"].mean())
#
# maxi = data["temp"].max()
# print(data.day[data.temp == maxi])
# print(data)
# cel_temp = data.temp[data.day == "Monday"]
# far_temp = 9/5*(cel_temp) + 32
# print(far_temp)

# data_dict = {
#     "students":["anjali","neha","komal","pari"],
#     "scores":["80","82","81","90"]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")
# gray_sq_cnt = len(data[data["Primary Fur Color"] == "Gray"])
# red_sq_cnt = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_sq_cnt = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_sq_cnt)
# print(red_sq_cnt)
# print(black_sq_cnt)
#
# data_dict = {
#     "Fur Color":["Gray","Cinnamon","Black"],
#     "Count":[gray_sq_cnt, red_sq_cnt, black_sq_cnt]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('squirrel_count.csv')