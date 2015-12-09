# Kamil Sijko kamil@coderdojo.org.pl
# scenariusz: Wojtek Gembalczyk w.gembalczyk@coderdojo.org.pl
# wiki pod adresem zasoby.coderdojo.org.pl

# importujemy bibliotekę potrzebną do manipulowania Minecraftem (wbudowana w instalację RaspberryPi,
# ale jeśli korzystamy z modów PC trzeba ją ręcznie zdobyć)
import mcpi.minecraft as minecraft
# importujemy również bibliotekę umozliwiającą m.in. "pauzowanie" - dzieki temu będziemy w stanie
# animować nasze budowle
import time
# i bibliotekę do matematyki
import math
# i bibliotekę do losowania
import random
# tworzymy obiekt reprezentujący świat Minecrafta
mc = minecraft.Minecraft.create()

# prosty test - czy działa czat?: 
mc.postToChat("Hej swiecie, tu Kamil, czy mnie slyszysz?")

# najprostsza pętla (struktura):
for i in range(1, 10, 1): #start-stop-step
	mc.postToChat("Owca nr. "+str(i))
	time.sleep(0.1)

# żeby zacząć budować musimy wiedzieć gdzie jesteśmy, sprawdźmy:
mc.player.getPos() # to wydrukuje współrzędne w konsoli
pos = mc.player.getPos() # to zapisze współrzędne do zmiennej "pos"
mc.postToChat("Wspolrzedne to x %s (szerokosc), y %s (wysokosc), z %s (glebokosc)." % (pos.x, pos.y, pos.z))

# w ten sposób z kolei układamy blok (położymy go dokładnie tam, gdzie staliśmy chwilę wczesniej,
# więc warto się przesunąć):
mc.setBlock(pos.x, pos.y, pos.z, 17)	# x, y, z, jaki bloczek (drewno)

# teraz czyścimy teren - wygodnie jest to zrobić za pomocą funkcji
def wyczysc(promien):
	pozycja = mc.player.getPos()
	mc.setBlocks(pozycja.x-promien, pozycja.y, pozycja.z-promien, pozycja.x+promien, pozycja.y+promien, pozycja.z+promien, 0)
	mc.setBlocks(pozycja.x-promien, pozycja.y-1, pozycja.z-promien, pozycja.x+promien, pozycja.y+1, pozycja.z+promien, 2)
	mc.player.setPos(pozycja.x, pozycja.y+10, pozycja.z)

# wywołujemy funckję
wyczysc(150)

# dla wygody zapisze sobie promień konaru drzewa do zmiennej
promien = 10

pos = mc.player.getPos() # zapisujemy "świeże" współrzędne
for i in range (-promien, promien+1):
	mc.setBlock (pos.x + i, pos.y+10, pos.z, 17)

# teraz kwadrat z kreski
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		mc.setBlock (pos.x + i, pos.y + j, pos.z, 17)

# teraz sześcian
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		for k in range (-promien, promien+1):
			mc.setBlock (pos.x + i, pos.y + j, pos.z + k, 17)

# zanim znów spróbujemy - czyścimy
wyczysc(150)
pos = mc.player.getPos() # zapisujemy "świeże" współrzędne
# modyfikacja powyższego kodu, z warunkiem, który pozwala narysować tylko płaskie koło
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		for k in range (-promien, promien+1):
			if (j == pos.y) and (math.sqrt (i*i + k*k) <= promien):
				mc.setBlock (pos.x + i, pos.y + j, pos.z + k, 17)

# zanim znów spróbujemy - czyścimy
wyczysc(150)
pos = mc.player.getPos() # zapisujemy "świeże" współrzędne
# modyfikacja powyższego kodu bez warunku rysuje walec
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		for k in range (-promien, promien+1):
			if (math.sqrt (i*i + k*k) <= promien):
				mc.setBlock (pos.x + i, pos.y + j, pos.z + k, 17)

# zanim znów spróbujemy - czyścimy
wyczysc(150)
pos = mc.player.getPos() # zapisujemy "świeże" współrzędne
# teraz kula
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		for k in range (-promien, promien+1):
			if (math.sqrt (i*i + j*j + k*k) <= promien):
				mc.setBlock (pos.x + i, pos.y + j + 10, pos.z + k, 17) # j+10 żeby kula nie była w połowie pod ziemią

# zanim znów spróbujemy - czyścimy
wyczysc(150)
pos = mc.player.getPos() # zapisujemy "świeże" współrzędne
# teraz kulista chmura liści
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		for k in range (-promien, promien+1):
			if (math.sqrt (i*i + j*j + k*k) <= promien) and (random.randint (0, 9) == 0):
				mc.setBlock (pos.x + i, pos.y + 10 + j, pos.z + k, 35, 5)

# zanim znów spróbujemy - czyścimy
wyczysc(150)
pos = mc.player.getPos() # zapisujemy "świeże" współrzędne
mc.player.setPos(pos.x+10, pos.y, pos.z)
# teraz wszystko składamy w całość!
promien=3
for i in range (-promien, promien+1):
	for j in range (0, 15):
		for k in range (-promien, promien+1):
			if (math.sqrt (i*i + k*k) <= promien):
				mc.setBlock (pos.x + i, pos.y + j, pos.z + k, 17)

promien=15
for i in range (-promien, promien+1):
	for j in range (-promien, promien+1):
		for k in range (-promien, promien+1):
			if (math.sqrt (i*i + j*j + k*k) <= promien) and (random.randint (0, 9) == 0):
				mc.setBlock (pos.x + i, pos.y + 20 + j, pos.z + k, 35, 5)