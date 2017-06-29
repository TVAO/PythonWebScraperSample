
# Extract weather information from SF
# Source: http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WVTaZ-uGOUk

"""""
Guide on scraping:
1) Navigate HTML structure with browser dev tools to familiarize with structure
2) Download web page containing information
3) Find the tags of interest and extract them
"""

import requests
from bs4 import BeautifulSoup
from pkg_resources._vendor.six import print_

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify()) # First item with name, description, short descr and temperature

# Extract name, description and temperature of forecast item
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

# Extract title from image
img = tonight.find("img")
desc = img['title']
print(desc)

# Extract all at once using CSS and BS
seven_day = soup.find(id="seven-day-forecast")
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

# Extract description and temperature
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)

# Combine data into Panda DataFrame for analytical purposes
# DataFrame object can store tabular data for easy analysis
# Pass list of items as part of dictionary where each key is a column
import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
weather

# Analysis of data - regular expression used to extract numeric temperature values
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+", expand=False)
weather["temp_num"] = temp_nums.astype('int')
temp_nums

# Find mean (average) temperature
mean = weather["temp_num"].mean()

# Show rows at night
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
nightWeatherDays = is_night

exit(0)


