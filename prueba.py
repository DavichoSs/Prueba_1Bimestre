print('ESCUELA POLITECNICA NACIONAL'+'\nPrueba Primer Bimestre\n')
opc=int(input('Escoja una de las siguientes opciones:'+'\n1.-suma de vectores'+'\n2.-Ingresar numeros'+'\n3.-dividir en tres partes un archivo de texto'+'\n4.-Salir\n'))
if opc==1:
	b=[]
	c=[]
	for i in range(0,3):
		x=int(input('ingrese posicion:'+str(i)+' del primer vector'))
		b.append(x)
	for j in range(0,3):
		y=int(input('ingrese posicion:'+str(j)+' del segundo vector'))
		c.append(y)
pass