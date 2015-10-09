import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("192.168.0.11")

mc.postToChat("Wojtek1")

time.sleep(0.2)

mc.player.setPos(0,0,0)

pozycja = mc.player.getPos()
#mc.setBlocks(pozycja.x-150, 30, pozycja.z-150, pozycja.x+150, 30, pozycja.z+150, block.GRASS.id)
mc.setBlocks(pozycja.x-150, 0, pozycja.z-150, pozycja.x+150, 0, pozycja.z+150, block.GRASS.id)

mc.postToChat(pozycja)
time.sleep(1)
mc.postToChat("Wojtek1: gotowe")

