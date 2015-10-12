# Autor: Kamil Sijko kamil@coderdojo.org.pl
# standardowa inwokacja z założeniem, że Python uruchamiany jest na tej samej maszynie co Minecraft 
# (np. na RaspberryPi, do którego logujemy się przez SSH)
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create() 	# jeśli łączymy się z lokalnego Pythona do zdalnego Minecrafta,
					# to w nawiasie trzeba w cudzysłowiu podać IP serwera Minecraft,
					# np. ("192.168.0.36"), na RaspberryPi IP sprawdzisz komendą
					# hostname -I (inne sposoby na https://goo.gl/Vp2qe0)

# Wysyłamy testowy komunikat do serwera Minecraft 
mc.postToChat("Tutaj Kamil - udało mi się! :-)")
