from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

while True:
    hit=mc.events.pollProjectileHits()
    if len(hit)>0:
        hit=hit[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.createExplosion(x,y,z)