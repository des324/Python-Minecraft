from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
for i in range(5):
    mc.setBlocks(x+i,y+i,z+i,x,y,z,10)
    time.sleep(0.5)