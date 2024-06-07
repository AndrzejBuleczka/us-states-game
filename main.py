import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240607.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


df = pandas.DataFrame(
    {
        "Fur Color": ["Gray", "Red", "Black"],
        "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
    }
)
df.to_csv("squirrel_count.csv")
