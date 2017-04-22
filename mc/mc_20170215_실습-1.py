from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

blockType = 41

playerPos0 = mc.player.getPos()
x0 = int(playerPos0.x)
y0 = int(playerPos0.y)
z0 = int(playerPos0.z)

while True:
    playerPos = mc.player.getPos()
    x = int(playerPos.x)
    y = int(playerPos.y)
    z = int(playerPos.z)
    mc.postToChat("x: %d, y: %d, z: %d" %(x,y,z))
    



    
    
