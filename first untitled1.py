from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
print(mc.player.getTilePos())
x=254
y=69
z=220
time.sleep(5)
mc.player.setTilePos(x,y,z)
print(3**3)
