Collection of Python scripts used in the WeatherMan Pi project.

Used to display current conditions from the Dark Sky API using a Raspberry Pi, Pimoroni Unicorn HAT HD and a small servo.

The scripts assume that you've already installed the software for the Unicorn HAT HD, this can be found at https://shop.pimoroni.com/products/unicorn-hat-hd

The project write-ups can be found at:

Instructables: 

Hackster: 

YouTube:

Installation & Use
------------------

Clone or download the "weather" folder into the "pi" folder on your raspberry pi. 

The main script functions are as follows: 

*weatherman.py*

This is the main script that extracts the weather data from Dark Sky. You'll need to set up a Dark Sky account at https://darksky.net/dev and put your Secret Key in the script where indicated. You'll also need to put in the latitude & longitude of the weather location you're interested in - this can be found on Google Maps, just right-click and select "What's Here?" and you'll get a pop-up showing the lat/long of the location.

The script is set to run on startup by editing the startup file...

  sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart

...and adding:

  @python3 /home/pi/weather/weatherman.py &

at the end of the file.

*icon.py*

This script takes a "current conditions" parameter from the weatherman.py script and uses it to display a 16x16 weather animation - these are all stored in the "icons" folder and are part of the standard Unicorn HAT HD documentation. You can edit the PNG animation files easily in GIMP or similar to give them more character.

*phones.py*

If the weather conditions have changed from the last API request (or it's a fresh boot and it isn't snowing) then this script is called from weatherman.py and instructs the servo to "jiggle" back & forth to alert you that conditions have changed.

*precip.py*

This script accepts a "precipitation probability" parameter from weatherman.py and displays lines in blue on the Unicorn HAT relating to the % probabilty. If 100% all rows will be blue, if 50% only 8 rows etc.

*temp.py*

Another standard Pimoroni script, this one takes a "temp" parameter from weatherman.py and displays it with scrolling text. It's set to use the Herkules truetype font (in the "fonts" folder) but could use a standard font if you prefer. 

------

My other Old Tech. New Spec projects are all on Instructables at https://www.instructables.com/member/MisterM/instructables/ 

and Hackster at https://www.hackster.io/martin-mander/projects

More details and a contact form are on our website at http://bit.ly/OldTechNewSpec. and we're on Twitter @OldTechNewSpec.




