Collection of Python scripts used in the WeatherMan Pi project.

Used to display current conditions from the Dark Sky API using a Raspberry Pi, Pimoroni Unicorn HAT HD and a small servo.

The scripts assume that you've already installed the software for the Unicorn HAT HD, this can be found at https://shop.pimoroni.com/products/unicorn-hat-hd

The project write-ups can be found at:

Instructables: 

Hackster: 

YouTube:

INSTALLATION

Clone or download the "weather" folder into the "pi" folder on your raspberry pi. 

The main script functions are as follows: 

*weatherman.py*

This is the main script that extracts the weather data from Dark Sky. You'll need to set up a Dark Sky account at https://darksky.net/dev and put your Secret Key in the script where indicated. You'll also need to put in the latitude & longitude of the weather location you're interested in - this can be found on Google Maps, just right-click and select "What's Here?" and you'll get a pop-up showing the lat/long of the location.


