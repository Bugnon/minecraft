# minecraft
Minecraft framework for projects with the Raspberry Pi using the GPIO.

## Description

## Table of contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)


Place common source code into files
* buildings
* tunnels
* bridges
* weather

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
The RPi.GPIO module needs to be re-installed for the virtual environment (py3cv3). Type the following command into the console
```
(py3cv3) pi@raspberrypi:~ $ pip3 install RPi.GPIO
Collecting RPi.GPIO
...
Successfully installed RPi.GPIO-0.6.3
```
