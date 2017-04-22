# 마인크래프트에 연결하기
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 현재 좌표
Pos = mc.player.getPos()

x = Pos.x    #x = 플레이어의 현재 x좌표
y = Pos.y    #y = 플레이어의 현재 y좌표
z = Pos.z    #z = 플레이어의 현재 z좌표
width = 100
height = 50
length = 100
blockType = 0      # 공기

mc.setBlocks(x, y, z, x+width, y-height, z+length, blockType)      # 평지 만드는 코드






