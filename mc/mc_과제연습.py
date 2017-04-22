from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import math
import time

second = 2

def timeMeasure0():
    localtime = time.asctime( time.localtime(time.time()))
    mc.postToChat("current time: " + localtime)

time.sleep(second)
timeMeasure0()



