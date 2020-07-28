# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:02:56 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x-1,y,z,103)
mc.setBlock(x+1,y,z,103)
mc.setBlock(x-1,y,z-1,103)
mc.setBlock(x-1,y,z+1,103)
mc.setBlock(x+1,y,z+1,103)
mc.setBlock(x+1,y,z-1,103)
mc.setBlock(x,y,z+1,103)
mc.setBlock(x,y,z-1,103)