from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import math
import time

#second = 2

pos0 = mc.player.getTilePos()
x0 = pos0.x
y0 = pos0.y
z0 = pos0.z
t0 = time.clock()

#time.sleep(second)

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z
t1 = time.clock()

forwhill  = t1-t0
distance  = math.sqrt(((x1-x0)**2) + ((y1-y0)**2) + ((z1-z0)**2))
localtime = time.asctime(time.localtime(time.time()))

while distance != 5:
    pos1 = mc.player.getTilePos()
    x1 = pos1.x
    y1 = pos1.y
    z1 = pos1.z
    distance  = int(math.sqrt(((x1-x0)**2) + ((y1-y0)**2) + ((z1-z0)**2)))

print("time: ", forwhill)
print("distance: ", distance)
print("current time: ", localtime)

mc.postToChat("time: " + str(forwhill))
mc.postToChat("distance: " + str(distance))
mc.postToChat("current time: " + str(localtime))




