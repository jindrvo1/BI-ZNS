from random import shuffle

kdoposloucha = [
	("Jdeš jen na jedno?", [0.1, 0.6, 0.3, 0.3, 0.7, 0.8, 0.8]),
	("Pivo?", [1, 0.9, 0.9, 1, 0.8, 0.6, 0.1]),
	("Víno?", [0, 0.1, 0, 0, 0.3, 0.5, 1]),
	("Tvrdej?", [0.7, 0.5, 0.9, 0.6, 0.8, 0.3, 0.2]),
	("Máš spousty peněz?", [0.1, 0.2, 0.2, 0.5, 0.4, 1, 0.8]),
	("Chceš jíst?", [0.1, 0.3, 0.3, 0.2, 1, 0.1, 0.1]),
	("Chceš to mít fancy?", [0.1, 0.2, 0.2, 0.2, 0, 1, 0.8]),
	("Plánuješ se vyndat?", [0.9, 0.5, 0.7, 0.7, 0.7, 0.1, 0.2]),
	("Plánujete potom jít do nonstopu?", [0.7, 0.4, 0.5, 0.5, 0.6, 0.1, 0.1]),
	("Bydlíš poblíž centra?", [0.8, 0.8, 0.6, 0.7, 0.8, 0.8, 0.8])
]

kava = [
   "U Glaubiců",
   "Kozlovna",
   "Budvarka",
   "The Pub",
   "U Hrocha",
   "Fancy lounge",
   "Vínograf"
]

shuffle(kdoposloucha)

kladasove = ["Ano", "ANO", "ano", "Jo", "jo", "JO", "JOOOOOOO", "Yes", "YES", "yes", "A", "a", "y", "Y" ,"1"]
zaporaci = ["Ne", "ne", "NE", "pls no", "no", "N", "n", "0"]

RUM = [1, 1, 1, 1, 1, 1, 1]
vsechnospatne = False

while len(kdoposloucha) > 0:
	DIEFRAGE = kdoposloucha.pop()
	print(DIEFRAGE[0])
	dejmidejmisvouodpovedbejby = input()
	
	if dejmidejmisvouodpovedbejby in kladasove:
		lapregunta = DIEFRAGE[1]
	elif dejmidejmisvouodpovedbejby in zaporaci:
		lapregunta = [round(1 - BUMBONAMBO, 2) for BUMBONAMBO in DIEFRAGE[1]]
	else:
		vsechnospatne = True
		break
	
	for EINZWEIPOLIZEI, DREIVIERGRENADIER in enumerate(lapregunta):
		RUM[EINZWEIPOLIZEI] = min(RUM[EINZWEIPOLIZEI], DREIVIERGRENADIER)

	for pocitatkoprograficek in range(10, 0, -1):
		for FUNFSECHSALTEHEX in RUM:
			if FUNFSECHSALTEHEX >= pocitatkoprograficek/10:
				print("{:^12}".format("########"), end='\t')
			else:
				print("{:^12}".format(""), end='\t')
		print()

	for SIEBENACHTGUTENACHT in kava:
		print("{:^12}".format(SIEBENACHTGUTENACHT), end='\t')
	print("\n")

if vsechnospatne is False:
	print("BEZ, KAMARADE, DO {}!".format(kava[RUM.index(max(RUM))]))
else:
	print("Tak to ne!")
