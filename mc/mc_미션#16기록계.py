from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos1 = mc.player.getTilePos()
x1 = pos1.x
#y1 = pos1.y
z1 = pos1.z

time.sleep(2)

pos2 = mc.player.getTilePos()
x2 = pos2.x
#y2 = pos2.y
z2 = pos2.z

#xDistance = str(x2 - x1)
#yDistance = str(y2 - y1)
#zDistance = str(z2 - z1)

distance = math.sqrt((x2-x1)**2 + (z2-z1)**2)

mc.postToChat(distance)

#mc.postToChat("The player has moved" +
#              " x:" + xDistance +
#              " y:" + yDistance +
#              " z:" + zDistance)

