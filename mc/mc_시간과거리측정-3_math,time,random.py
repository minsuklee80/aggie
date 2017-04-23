from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time
import math

pos = mc.player.getTilePos()
x = pos0.x
y0 = pos0.y
z0 = pos0.z
t0 = time.clock()

second = 2

for i in range(3):
    time.sleep(second)
    where = random.randint(1,10)
    x1 = pos1.x
    y1 = pos1.y
    z1 = pos1.z
    t1 = time.clock()

time.sleep(second)

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
