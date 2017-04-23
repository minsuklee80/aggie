from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

blockType = 41

playerPos1 = mc.player.getPos()
x = playerPos1.x
y = playerPos1.y
z = playerPos1.z

'''
for i in range(3):
    time.sleep(5)
    where = random.randint(1,10)
    x+=where
    y+=where
    z+=where
    mc.player.setTilePos(x,y,z)
'''
time.sleep(5)
where = random.randint(1,10)
x1 = x + where
y1 = y
z1 = z
mc.player.setTilePos(x1,y1,z1)
mc.setBlocks(x, y-1, z, x1, y1-1, z1, blockType)
    



