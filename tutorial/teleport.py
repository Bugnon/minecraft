from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Teleport")
x, y, z = mc.player.getPos()
mc.player.setPos(x, y+20, z)
