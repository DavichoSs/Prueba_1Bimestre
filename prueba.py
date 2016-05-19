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
