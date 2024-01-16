# Part 2
## Station code for Seattle: GHCND:US1WAKG0038

## reading the json file
import json
with open("weather_assignment/precipitation.json") as file:
    precipitation_data = json.load(file)

## putting the Seattle data in a list called seattle_data
seattle_data = []
for data in precipitation_data:
    if data["station"] == "GHCND:US1WAKG0038":
        seattle_data.append(data)

## creating a dictionary to store the sum of precipitation per month and total_yearly_precipitation
seattle_monthly_precipitation_dict = {}
total_yearly_precipitation = 0
for data in seattle_data:
    date = data["date"]
    month = (date.split("-"))[1]
    if month not in seattle_monthly_precipitation_dict:
        seattle_monthly_precipitation_dict[month] = data["value"]
    else:
        seattle_monthly_precipitation_dict[month] += data["value"]
    total_yearly_precipitation += data["value"] 
    
## transforming the dictionary into a list
seattle_monthly_precipitation = []
for data in seattle_monthly_precipitation_dict:
    seattle_monthly_precipitation.append(seattle_monthly_precipitation_dict[data])

## calculating relative_monthly_precipitation
relative_monthly_precipitation = []
for data in seattle_monthly_precipitation:
    calculation = round(data/total_yearly_precipitation, 4)
    relative_monthly_precipitation.append(calculation)

## creating the output data
output = {
    "Seattle":{
            "station": "GHCND:US1WAKG0038",
            "state": "WA",
            "total_monthly_precipitation": seattle_monthly_precipitation,
            "total_yearly_precipitation": total_yearly_precipitation,
            "relative_monthly_precipitation": relative_monthly_precipitation
        }    
}    

## dumping into json
with open("weather_assignment/results.json", "w") as file:
    json.dump(output, file, indent = 4)
