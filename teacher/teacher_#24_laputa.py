# 임의의 한 곳으로 텔레포트하고 지상까지 계단 만들기
from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
blockID = 41 # gold

pos = mc.player.getPos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

rx = random.randint(-10, 10)
ry = random.randint(5, 10)
rz = random.randint(-10, 10)

mc.setBlocks(x+rx-1,y+ry-1,z+rz-1, x+rx,y+ry,z+rz, blockID) # station1
'''
for i in range(ry+2):
    mc.setBlock(x+rx,y+ry-i,z+rz-i, blockID)
    mc.setBlock(x+rx+1,y+ry-i,z+rz-i, blockID)
    mc.setBlock(x+rx+2,y+ry-i,z+rz-i, blockID)
'''
