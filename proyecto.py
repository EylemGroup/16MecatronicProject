#Programa de Raspberry
#Proyecto mectronico

#FUNCION COMPARACION DE MATRICES------------------------
def compmat(a,b):

	n = len(a)
	n2 = len(a[0])
	sino= 0

	for i in range(0,n):
		for j in range(0,n2):
			if a[i][j] == b[i][j]:
				sino = sino
			else:
				sino = sino +1
	if sino==0:
		return 0
	else:
		return 1
#---------------------------------------------------------
#MAIN
# 1ER PARALELEPIPEDO

#Variables de lectura
SALIM = [[0, 0], [0, 0]]
STALA = [[0, 0], [0, 0], [0, 0]]
STUBOA = 0
STUBOT = 0

#Valores iniciales
SALIM0 = [[0, 0], [0, 0]]
STALA0 = [[0, 0], [0, 0], [0, 0]]
STUBOA0 = 0
STUBOT0 = 0

#Variables de configuracion
nTubos = 100

# 2DO ROMBO
sali = compmat(SALIM,SALIM0)
stal = compmat(STALA,STALA0)

if sali == 0  & stal ==0 & STUBOA == STUBOA0 & STUBOT == STUBOT0:
	print("johangay")
else:
	print("ALARMA")

# 3ER BLOQUE
for i in range(0,nTubos):
#	While esperara a que se detecte el tubo
	while STUBOA==0:
		input("Press Enter to continue...")
		STUBOA = 1
#	Inicializa los pistones de empuje
	PA1 = 1
	print(PA1)
print("prueba1branch")

