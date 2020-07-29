from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

for i in range(20):
    mc.setBlock(x+i,y-1,z+i,1)
    mc.setBlock(x+i+1,y-1,z+i,1)
    mc.setBlock(x+i+2,y-1,z+i,1)
    mc.setBlock(x+i+3,y-1,z+i,1)
    mc.setBlock(x+i+4,y-1,z+i,1)
    mc.setBlock(x+i+5,y-1,z+i,1)
    mc.setBlock(x+i+6,y-1,z+i,1)
    mc.setBlock(x+i+7,y-1,z+i,1)
    mc.setBlock(x+i+8,y-1,z+i,1)
    mc.setBlock(x+i+9,y-1,z+i,1)
    mc.setBlock(x+i+10,y-1,z+i,1)
    mc.setBlock(x+i+11,y-1,z+i,1)
    mc.setBlock(x+i+12,y-1,z+i,1)
    mc.setBlock(x+i+13,y-1,z+i,1)
    mc.setBlock(x+i+14,y-1,z+i,1)
    mc.setBlock(x+i+15,y-1,z+i,1)