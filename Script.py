# Part 3
import json
from csv import DictReader

## reading the stations file
with open("stations.csv") as file:
    reader = DictReader(file)
    station_data = list(reader)

## reading the stations code
station_dict = {}
for location in station_data:
    station_dict[location["Location"]] = location 

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

## making the dictionary where all output will go to
precipitation_dict = {}
precipitation_dict["monthly_precipitation"] = {}
precipitation_dict["yearly_precipitation"] = {}
precipitation_dict["relative_monthly_precipitation"]  = {}

## iterating for every station
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
    precipitation_dict["monthly_precipitation"][station] = station_precipitation_list
    precipitation_dict["yearly_precipitation"][station] = total_yearly_precipitation

# for station in precipitation_dict["monthly_precipitation"]:
#     for data in precipitation_dict["monthly_precipitation"][station]:
#         calculation = round(data/precipitation_dict["yearly_precipitation"][station], 4)
#         precipitation_dict["relative_monthly_precipitation"][station].append(calculation)
        



# ## calculating relative_monthly_precipitation
# relative_monthly_precipitation = []
# for data in seattle_monthly_precipitation:
#     calculation = round(data/total_yearly_precipitation, 4)
#     relative_monthly_precipitation.append(calculation)

# ## creating the output data
# output = {
#     "Seattle":{
#             "station": "GHCND:US1WAKG0038",
#             "state": "WA",
#             "total_monthly_precipitation": seattle_monthly_precipitation,
#             "total_yearly_precipitation": total_yearly_precipitation,
#             "relative_monthly_precipitation": relative_monthly_precipitation
#         }    
# }    

# ## dumping into json
# with open("weather_assignment/results.json", "w") as file:
#     json.dump(output, file, indent = 4)