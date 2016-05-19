print('ESCUELA POLITECNICA NACIONAL'+'\nPrueba Primer Bimestre\n')
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
		y=int(input('ingrese posicion '+str(j)+' del segundo vector: '))
		c.append(y)
	print("\n")
	for k in range(0,3):
		z=int(input('ingrese posicion '+str(k)+' del tercer vector: '))
		d.append(y)
	print("\n")
pass