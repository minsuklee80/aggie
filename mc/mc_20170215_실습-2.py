from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
blockType = 41

playerPos = mc.player.getPos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

for i in range(10):
    x = x+5
    y = mc.getHeight(x, z)
    z = z+5
    mc.player.setTilePos(x,y,z)
    time.sleep(2)

