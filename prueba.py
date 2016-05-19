print('ESCUELA POLITECNICA NACIONAL'+'\nPrueba Primer Bimestre\n')
print("Alexander Figueroa \nRuben Pozo \nJean Carlos Chamba \n Santiago Toapanta")
opc=int(input('Escoja una de las siguientes opciones:'+'\n1.- Suma de vectores'+'\n2.- Ingresar numeros'+'\n3.- Dividir en tres partes un archivo de texto'+'\n4.- Salir\n'))
if opc==1:
	b=[]
	c=[]
	d=[]
	for i in range(0,3):
		x=int(input('Ingrese posicion '+str(i)+' del primer vector: '))
		b.append(x)
	print("\n")
	for j in range(0,3):
		y=int(input('Ingrese posicion '+str(j)+' del segundo vector: '))
		c.append(y)
	print("\n")
	for k in range(0,3):
		valor=b[k]+c[k]
		d.append(valor)
		
	print("\n")
	print("El vector 1 es: "+str(b))
	print("El vector 2 es: "+str(c))
	print("El vector resultante es: "+str(d))

if opc==2:
	num=1
	promedio=0
	res=0
	a=[]
	while (num!=0):
		num=int(input('Ingrese cualquier cantidad de numeros: '))
		res=res+1
		a.append(num)
		promedio=promedio+num
	a.sort()
	print("Los numeros ingresados son: "+str(a))
	print("El promedio es: "+str(promedio/(res-1)))
if opc==3:
	print("NO DEFINIDA")
	'''
	def archivo():
	archi= open('libro.txt', 'r')
	linea = archi.readline()
	b = len(linea)
	a=round(b,0)
	archi.close()
	print (a)
	return a

	tex=archivo()

def dividir_archi(tex):
	c=tex/3
	res=round(c,0)
	print(res)
	return res

total = dividir_archi(tex)

def grabaTxt1(tot):
	archi= open('libro.txt', 'w')
	linea = archi.readline()
	archi.close()
	primero=linea[:tot]
	archi=open('primera_parte.txt','a')
	archi.write(primero)

def grabarTxt2(tot):
	x=tot+tot
	archi= open('libro.txt', 'w')
	linea = archi.readline()
	archi.close()
	archi=open('segunda_parte.txt','a')
	segundo=linea[:x]
	archi.write(segundo)
def grabarTxt3(tot):
	y=tot+tot+tot
	archi= open('libro.txt', 'w')
	linea = archi.readline()
	archi.close()
	archi=open('tercera_parte.txt','a')
	tecero=linea[:y]
	archi.write(tercero)

def creartxt():
	archi=open('primera_parte.txt','a')
	grabaTxt1(total)	#archi.write()
	archi.close()
def creartxt2():
	archi=open('segunda_parte.txt','a')
	grabarTxt2(total)
	archi.close()
def creartxt3():
	archi=open('tercera_parte.txt','a')
	grabarTxt3(total)
	archi.close()


def crear_archi(tot,tex):
	for i in range (0,tex):
		if i==tot:
			creartxt()
			#grabaTxt(total)
			print (i)
		if i==tot+tot:
			creartxt2()
			print (i)
		if i==tot+tot+tot:
			creartxt3()
			print (i)
		
resultado=crear_archi(total,tex)
		
'''
if opc==4:
	exit()