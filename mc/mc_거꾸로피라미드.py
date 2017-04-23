# 마인크래프트에 연결하기
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 현재 좌표
Pos = mc.player.getPos()

x = Pos.x    #x = 플레이어의 현재 x좌표
y = Pos.y    #y = 플레이어의 현재 y좌표
z = Pos.z    #z = 플레이어의 현재 z좌표

blockType = 95              # 블럭 종류

# 윗변 'size'의 피라미드 만들기
size = 5
for i in range(size//2+1):         #피라미드 높이만큼 반복((size/2)+1)
    mc.setBlocks(x-i, y+i, z-i, x+i, y+i, z+i, blockType)


