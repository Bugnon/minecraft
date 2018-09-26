# Tutorial
Source: [Getting started with Minecraft Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi)

Clone the files from Github onto the Raspberry Pi.
```
git clone https://github.com/Bugnon/minecraft
```
Change into the __tutorial__ directory, and run the Python code.
```
cd minecraft/tutorial
python3 hello.py
```
Open the file with a text editor such as __nano__ or __Thonny__ and modifiy the Python code.
```
nano hello.py
```

## hello.py
Writes "Hello world" to the Minecraft chat.

## getPos.py
Writes the current position to the Minecraft chat as well as to the console.

## teleport.py
Makes the player jump 20 blocks into the air.

## setBlock.py
Asks in a menu loop for the material (rock, grass, soil) and places a block in front of the player, while moving one block backwards.

## setBlocks.py
Places a 7x7-block rock platform beneath the player. A 2-block wall of the same material surrounds the platform.

## trace.py
Leaves a trace of flowers behind if walking on grass, otherwise the block below the player is turned into grass.

## tnt.py
Creates a 10x10x10 block of TNT.

## lava.py
Lava flows for 20 seconds from an elevated position. Thereafter water flows on top of it for 4 seconds. This transforms the lava into rock.
