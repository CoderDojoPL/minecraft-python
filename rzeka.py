# -*- coding: utf-8 -*-
# Autor: Wojtek Gembalczyk w.gembalczyk@coderdojo.org.pl

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

def woda3x3(x, z):
    mc.setBlocks(x, 0, z-6, x, 2, z+6, block.AIR.id)     #powietrze nad rzeką
    mc.setBlocks(x, 0, z-5, x, 0, z+5, block.DIRT.id)    #waly powodziowe
    mc.setBlocks(x, 0, z-4, x, 1, z+4, block.DIRT.id)    #waly powodziowe
    mc.setBlocks(x, -1, z-2, x, 1, z+2, block.WATER.id)  #woda

def fragment_mostu(x, y, z):
    mc.setBlocks(x-2, y, z, x+2, y+1, z, block.GLASS.id)   
    mc.setBlocks(x-1, y, z, x+1, y, z, block.STONE.id)   
    mc.setBlocks(x-1, y+1, z, x+1, y+1, z, block.AIR.id)   

def most(x, z):
    fragment_mostu(x, 0, z-10)   
    fragment_mostu(x, 1, z-9)   
    fragment_mostu(x, 2, z-8)
    for i in range(-7, 8):
        fragment_mostu(x, 3, z+i)   
    fragment_mostu(x, 2, z+8)
    fragment_mostu(x, 1, z+9)   
    fragment_mostu(x, 0, z+10)   


mc = minecraft.Minecraft.create()
dlugosc = 100
mosty_fr = 40

mc.setBlocks(-50, 0, 0, dlugosc+50, 50, 100, block.AIR.id)
mc.setBlocks(-50, -5, 0, dlugosc+50, -1, 100, block.DIRT.id)

time.sleep(2)

mc.setBlocks(-2, -1, 45, -1, 1, 55, block.DIRT.id)

for i in range(0, dlugosc*10, 7):
    z = float(i)/100
    woda3x3(int(z*10), int(math.sin(z)*7+50))
    time.sleep(0.02)
    if i%(7*mosty_fr)==0 and i<>0:
        most(int(z*10), int(math.sin(z)*7+50))
    ostatni_x = int(z*10)
    ostatni_z = int(math.sin(z)*7+50)

mc.setBlocks(ostatni_x-1, -1, ostatni_z-5, ostatni_x, 1, ostatni_z+5, block.DIRT.id)
