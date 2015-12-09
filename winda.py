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
import time
import random
mc = minecraft.Minecraft.create()

# now let's sent message to chat: 
mc.postToChat("Kamil Sijko: testuje polaczenie")

# this is S*N*A*K*E
# set the stage
x, y, z = mc.player.getPos() 	# pobieramy pozycję
x, y, z = {0, 0, 0}
mc.camera.setFixed() 			# fixujemy kamerę
mc.camera.setPos(x, y+10, z)	# ustawiamy 10 bloków ponad starym
# czyszczenie terenu
mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, 0) # świeże powietrze pod kamerą
# teraz animacje
for i in range(0, 5, 1):
	for j in range(0, 5, 1):
		mc.setBlock(x+i, y, z+j, 0) # rysujemy lodem
		time.sleep(0.5)

# teraz mechanika Snake'a
while true