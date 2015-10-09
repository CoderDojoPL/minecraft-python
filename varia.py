# Autor: Kamil Sijko kamil@coderdojo.org.pl
# standardowa inwokacja z założeniem, że Python uruchamiany jest na tej samej maszynie co Minecraft 
# (np. na RaspberryPi, do którego logujemy się przez SSH)
import mcpi.minecraft as minecraft
from time import sleep 					# opcjonalnie, można też po prostu zaimportować całą 
										# bibliotekę time (czyli "import time")
import math
mc = minecraft.Minecraft.create()

# Wysyłamy testowy komunikat do serwera Minecraft 
mc.postToChat("Tutaj Kamil - udało mi się! :-)")

pos = mc.player.getPos() 				# pobieramy pozycję gracza i zapisujemy ją w zmiennej Pos
pos 									# wyświetlamy pozycję gracza w konsoli Python
mc.postToChat("Pozycja gracza: " + pos)	# wyświetlamy pozyję w konsoli - dopracować

x, y, z = mc.player.getPos() 			# alternatywnie
mc.player.setPos(x,y+50,z) 				# teleport / hyperjump

mc.setBlock(pos.x+1, pos.y, pos.z, 1)
mc.setBlocks(x+1, y+1, z+1, x+3, y+3, z+3, 46, 1)

# zrzucamy kwiatki jeśli na trawie
trawa = 2
kwiatek = 38
while True:
    x, y, z = mc.player.getPos()  # player position (x, y, z)
    block_beneath = mc.getBlock(x, y-1, z)  # block ID
    if block_beneath == trawa:
        mc.setBlock(x, y, z, kwiatek)
    sleep(0.1)

# zabawy z TNT :-)
TNT = 46
x, y, z = mc.player.getPos()
mc.setBlock(x, y, z, TNT, 1)
mc.setBlocks(x+1, y+1, z+1, x+6, y+6, z+6, TNT, 1)

# pętla rysująca sinus
x, y, z = mc.player.getPos()
for n in range(1, 100):
	mc.setBlock(x+n, y+10+2*math.sin(n), z+1, 1)