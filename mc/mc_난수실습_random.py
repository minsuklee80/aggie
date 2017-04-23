from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

blockType = 41

playerPos0 = mc.player.getPos()
x0 = int(playerPos.x)
y0 = int(playerPos.y)
z0 = int(playerPos.z)
goldx = x0+random.randint(-10,10)
goldy = mc.getHeight(goldx, goldz)
goldz = z0+random.randint(-10,10)

mc.setBlock(goldx, goldy, goldz, blockType)

while True:
    playerPos = mc.player.getPos()
    x = int(playerPos.x)
    y = int(playerPos.y)
    z = int(playerPos.z)
    mc.postToChat("GOLD: %d,%d,%d" %(goldx,goldy,goldz)
    mc.postToChat(" NOW: %d,%d,%d" %(x,y,z)
    if (goldx == x) and (goldy == y) and (goldz == z):
        mc.postToChat("*"*50)
        break
