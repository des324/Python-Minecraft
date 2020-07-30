# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:27:28 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
listowo = []
listoao = []
listoyo = []
for i in range(1,4):
    listowo.append(i*1)
    listoao.append(i*2)
    listoyo.append(i*3)
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,2,str(listowo),str(listoao)str(listoyo))





