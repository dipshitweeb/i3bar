# i3bar
My i3 bar configuration with a weather scraper. Move .xinitrc to your home directory. Move the other files to .config/i3/. In cockscraper.py change the url variable to whatever your weather.com/weather/l/XXXX...X is. To find this simply find the home page for your location by typing in your zip code to the weather.com search bar.
## How it works:
On X server start the commands in .xinitrc are executed. So on X server start we execute the python script cockscraper.py in the background to scrape weather.com for the current temperature every 30 minutes. We then output that temperature to a file called temp_file. Afterwards cockbar.sh reads this temperature and appends it to our stdout formatted in JSON. The stdout is then sent to i3bar's protocol via status_command as stated in the file config (Which is i3's config file). Status_command then displays the stdout via our bar.
## Dependencies:
Arch:

`sudo pacman -S python3 python-pip && pip install beautifulsoup4`

## Resources:
https://i3wm.org/docs/i3bar-protocol.html
