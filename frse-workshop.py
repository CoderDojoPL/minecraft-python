# Kamil Sijko kamil@coderdojo.org.pl
# Wojtek Gembalczyk w.gembalczyk@coderdojo.org.pl

# books:
# teacher ed.	https://arghbox.files.wordpress.com/2013/06/teacheredition.pdf
# student ed.	https://arghbox.files.wordpress.com/2013/06/minecraftbook.pdf
# chetsheet:	https://arghbox.files.wordpress.com/2013/06/table.pdf

# SSID:		frselte3
# password:	#frselte#

# Windows: 	putty for SSH ()
# 			Notepad++ for code
			
# RPi IP:	192.168.1.3 # to check RPi IP type hostname -I in RPi's terminal
# user:		pi
# password:	raspberry

# command:	python

# repo: https://github.com/CoderDojoPL/minecraft-python

# those are preliminary steps to start "minecrafting" in python :-)
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

# now let's sent message to chat: 
mc.postToChat("Hi, I'm Kamil, and I know how to code :-)")

# now loops!

for i in range(1, 10, 1): #start-stop-step
	mc.postToChat("Hey hey x"+str(i))

# now we will build a tower!
# but first where are we?
mc.player.getPos() # this will just print coordinates
mc.player.getPos() = pos # this will save to vector-variable "pos"
# second - how to put a block?
mc.setBlock(1, 1, 4, 1) # x, y, z, whatblock?

x, y, z = mc.player.getPos() # this will store the coordinates to 3 variables
mc.setBlock(x, y, z+2, 1) # x, y, z, whatblock?

for i in range(1, 10, 1): #start-stop-step
	mc.postToChat("Hey hey!")

for i in range(0, 4, 1):
	x, y, z = mc.player.getPos() # this will get the fresh coordinates (but don't move!)
	mc.setBlock(x+5, y+i, z+5, 1)

import time

for i in range(0, 40, 1):
	x, y, z = mc.player.getPos() # this will get the fresh coordinates (but don't move!)
	mc.setBlock(x+5, y+i, z+5, 1)
	time.sleep(0.3)

	
	
	
	
