import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240607.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels["Primary Fur Color"])

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels["Primary Fur Color"])

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels["Primary Fur Color"])


df = pandas.DataFrame(
    {
        "Fur Color": ["Gray", "Red", "Black"],
        "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
    }
)
df.to_csv("squirrel_count.csv")
