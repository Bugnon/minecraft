"""
    Write "Hello world" to the Minecraft chat.
"""

from mcpi import minecraft

mc = minecraft.Minecraft.create()

# Writing to the Minecraft chat
mc.postToChat("Hello world")

#testing github by writing on chat
mc.postToChat("Github works!")

