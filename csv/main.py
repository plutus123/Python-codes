# # with open("/Users/HP/Desktop/python/csv/weather_data.csv") as file:
# #     content=file.readlines()
# #     print(content)
# import csv
# with open("/Users/HP/Desktop/python/csv/weather_data.csv") as file:
#     data=csv.reader(file)
#     # print(data)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(row[1])
#     # print(temperatures)
# s=" ".join(temperatures)
# print(s)
import pandas as pd
data=pd.read_csv("/Users/HP/Desktop/python/csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(my_data)
Gray_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
Cinnamon_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
Black_squirrels=len(data[data["Primary Fur Color"]=="Black"])
dict={
    "Color":["Gray","Cinnamon","Black"],
    "Count":[Gray_squirrels,Cinnamon_squirrels,Black_squirrels]
}
data_frame=pd.DataFrame(dict)
print(data_frame)
