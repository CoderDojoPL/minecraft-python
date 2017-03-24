# This script requires aditional extensions to mcpi library
# you can get the turtle extension at
# https://github.com/martinohanlon/minecraft-turtle/blob/master/minecraftturtle.py
# and learn more on how to use it at 
# http://www.stuffaboutcode.com/2014/05/minecraft-graphics-turtle.html
# this particular script also uses our Python-enabled Minecraft server (bukkit + raspberry juice)

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import minecraftturtle
import time

mc = Minecraft.create("alfa.cd.org.pl", 4711)

mc.getPlayerEntityIds()
mc.getPlayerEntityId("Kamil_CoderDojo") #doesn't work with regular API

mc.postToChat("Hello Minecraft World")

mc.player.getPos()

# Examples of functions
# Clean area around Player
def clean(n_blocks):
   x, y, z = mc.player.getPos()
   mc.setBlocks(x-n_blocks, y, z-n_blocks, x+n_blocks, y+n_blocks, z+n_blocks, block.AIR)
   mc.postToChat("Cleaned " + str(n_blocks) + " blocks")
   
clean(10)
   
# Move player up!
def moveup(n_blocks):
   x, y, z = mc.player.getPos()
   mc.player.setPos(x, y + n_blocks, z)
   mc.postToChat("Moved " + str(n_blocks) + " blocks up!")
   
moveup(5) # be carefull, large falls are dangerous
   
# Using the turtle
# create minecraft turtle at the players position and give it a name
steve = minecraftturtle.MinecraftTurtle(mc, mc.player.getPos())

#tell the turtle to go forward 15 blocks
steve.forward(15)

#tell the turtle to go right 90 degrees
steve.right(90)

#tell the turtle to go up by 45 degress
steve.up(45)

tell the turtle to go forward 25 blocks
steve.forward(25)