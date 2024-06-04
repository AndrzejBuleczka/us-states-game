import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()

max_temp = data.temp.max()
print(data.temp[0] * 9/5 + 32)
