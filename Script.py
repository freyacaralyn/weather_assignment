# Part 3
import json
from csv import DictReader

## reading the stations file
with open("stations.csv") as file:
    reader = DictReader(file)
    station_data = list(reader)

# reading the stations code
## creating the precipitation_dict to store all of the data
precipitation_dict = {}
## making the station dictionary to be able to convert the station code into the location 
station_dict = {}
for location in station_data:
    station_dict[location["Station"]] = location["Location"]
    precipitation_dict[location["Location"]] = {}
    precipitation_dict[location["Location"]]["station"] = location["Station"]
    precipitation_dict[location["Location"]]["state"] = location["State"]

## reading the json file
with open("precipitation.json") as file:
    precipitation_data = json.load(file)

## grouping the data by station
precipitation_data_station = {}
for data in precipitation_data:
    if data["station"] not in precipitation_data_station:
        precipitation_data_station[data["station"]] = []
        precipitation_data_station[data["station"]].append(data)
    else:
        precipitation_data_station[data["station"]].append(data)

# calculating monthly and total year precipitation 
# iterating for every station
for station in precipitation_data_station:
## creating a new dictionary and list for every iteration
    station_precipitation_dict = {}
    station_precipitation_list = []
    total_yearly_precipitation = 0
    ## iterating every line in the data for each station
    for data in precipitation_data_station[station]:
        ## fill the dictionary with sum of precipitation for each month
        date = data["date"]
        month = (date.split("-"))[1]
        if month not in station_precipitation_dict:
            station_precipitation_dict[month] = data["value"]
        else:
            station_precipitation_dict[month] += data["value"]
        total_yearly_precipitation += data["value"]
    ## converting the dictionary into a list
    for data in station_precipitation_dict:
        station_precipitation_list.append(station_precipitation_dict[data])
    ## putting the individual station data into a dictionary with all of the other stations
    precipitation_dict[station_dict[station]]["total_monthly_precipitation"] = station_precipitation_list
    precipitation_dict[station_dict[station]]["total_yearly_precipitation"] = total_yearly_precipitation

# calculating the relative_monthly_precipitation
## iterating every station in the dictionary
for location in precipitation_dict:
    ## creating the empty list for relative_monthly_precipitation inside the dictionary
    precipitation_dict[location]["relative_monthly_precipitation"] = []
    ## iterating every monthly precipitation data in the station
    for data in precipitation_dict[location]["total_monthly_precipitation"]:
        ## calculation, rounding it to 4 decimal points
        calculation = round(data/precipitation_dict[location]["total_yearly_precipitation"], 4)
        ## adding it to the main dictionary
        precipitation_dict[location]["relative_monthly_precipitation"].append(calculation)

# calculating the relative_yearly_precipitation
## calculating the sum of all stations
total_yearly_all = 0
for location in precipitation_dict:
    total_yearly_all += (precipitation_dict[location]["total_yearly_precipitation"])

## calculating the relative_yearly_precipitation and adding it to the dictionary
for location in precipitation_dict:
    calculation = round(precipitation_dict[location]["total_yearly_precipitation"]/total_yearly_all, 4)
    precipitation_dict[location]["relative_yearly_precipitation"] = calculation

## dumping into json
with open("results.json", "w") as file:
    json.dump(precipitation_dict, file, indent = 4)