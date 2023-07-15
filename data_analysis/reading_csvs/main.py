# with open("weather_data.csv",mode="r") as f:
#     file = f.readlines()
#     print(file)

# import csv

# with open("weather_data.csv",mode="r") as f:
#     out = csv.reader(f)
#     print(out)
#     temperature = []
#     for row in out:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
import numpy

data = pandas.read_csv("weather_data.csv")
print(data["temp"])



mean_data = data["temp"].mean()
print(mean_data)