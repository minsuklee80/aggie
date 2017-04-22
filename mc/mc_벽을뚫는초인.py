from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blockType = 0

while True:
    playerPos = mc.player.getPos()
    x = int(playerPos.x)
    y = int(playerPos.y)
    z = int(playerPos.z)
    mc.setBlocks(x+1, y+2, z+1, x-1, y, z-1, blockType)
    

    



    
    
