import bs4
from requests import get
import io
import time

# Class for the temp element
classname = "CurrentConditions--tempValue--3KcTQ"
url = "https://weather.com/weather/today/l/51eb5b5645368dc08f436af4fc2fda52a1a35c8149921daad786678267c60e78"

def refresh_temp():
    response = get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    current_temp = soup.find("span", {"class":classname})
    return current_temp.string

# Refresh the current temperature and write it to a file every 30 minutes 
while(1):
    temp = refresh_temp()
    with open("temp_file", "w") as f:
        f.write(temp)
    time.sleep(1800)
