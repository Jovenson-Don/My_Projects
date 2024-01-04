import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        row[1]
        if row != "temp":
            temperatures.append(row[1])
    print(temperatures)
