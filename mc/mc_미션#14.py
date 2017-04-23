from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

try:
    blockType = int(input("어떤 블록으로 쌓을래?"))
    for i in range(0, 10, 2):
        mc.setBlock(x+i, y, z, blockType)
    except:
    blockType = int(input("숫자를 입력하시오!"))
    mc.setBlock(x, y, z, blockType)

#blockType = int(input("어떤 블록으로 쌓을래?"))
#for i in range(height):
