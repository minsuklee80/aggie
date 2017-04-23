from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import math
import time

pos0 = mc.player.getTilePos()
x0 = pos0.x
y0 = pos0.y
z0 = pos0.z

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

inWater = 9

while mc.getBlock(x1, y1, z1) != inWater:
    pos1 = mc.player.getTilePos()
    x1 = pos1.x
    y1 = pos1.y
    z1 = pos1.z
    
distance = str(math.sqrt((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2))
mc.postToChat("distance: " + distance)
mc.postToChat("The end")




