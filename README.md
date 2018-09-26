# minecraft
Minecraft framework for projects with the Raspberry Pi using the GPIO and OpenCV with the Raspberry Pi camera.

## Installation
Start Minecraft by 
* enter `minecraft-pi` in the terminal.
* click on **Start Game**
* click on **Create New**
* press `tab` to release focus from Minecraft

In terminal
```
git clone -v https://github.com/Bugnon/minecraft
```

## Virtual environment for OpenCV
The RPi.GPIO module needs to be re-installed for the virtual environment (py3cv3). Type the following command into the console:
```
(py3cv3) pi@raspberrypi:~ $ pip3 install RPi.GPIO
Collecting RPi.GPIO
...
Successfully installed RPi.GPIO-0.6.3
```
Furthermore it is necessary to re-install the `mcpi` module. Unfortunately it cannot be found on the on the PyPI (Python Package Index), which would make it easy to be installed with `pip`. However it comes preinstalled on the Raspberry Pi. Use the copy command: 
```
cp -R /usr/lib/python3/dist-packages/mcpi /home/pi/.virtualenvs/py3cv3/lib/python3.4/site-packages
```

## Taking screenshots from Minecraft
http://www.stuffaboutcode.com/2016/03/raspberry-pi-take-screenshot-of.html

Install `raspi2png`
