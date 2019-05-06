#CALCULO DE FIGURAS GEOMETRICAS


#esta funcion dibuja un triangulo
def triangulito(l):
	for i in range(0,l,1):
		for j in range(0, i+1, 1):
			print("*", end="")
		print("")

#esta funcion dibuja un cuadrado 
def cuadrito(m,n):
	for i in range(1, m+1):
		for j in range(1,n+1):
			print("*", end="")
		print(" ")
#el ciclo while condicionado por un True
while True:
#figuras a las cuales se le puede calcular el area 
	print("Bienvenido a Geometric Tool")
	print("1_TRIANGULO")
	print("2_CUADRADO")
	print("3_CIRCULO")
	print("4_RECTANGULO")
#seleccion de la figura a calcular el area
	seleccion = (input("Que figura desea calcular el area:"))
	seleccion2 =seleccion.upper()
#confirmacion de la figura seleccionada 
	print("Ud escogio un {}".format(seleccion2))
#if anidhado. se desplegara una opcion de acuerdo a la seleccion.
	if seleccion2 == "CUADRADO":
		dato1=int(input("ingrese el valor de uno de los lados del cuadrado: "))
		area1=dato1*4
		print("el area del cuadrado es:",area1)
	elif seleccion2 == "TRIANGULO":
		dato2=int(input("ingrese el valor del lado del triangulo:"))
		dato2a=int(input("ingrese el valor del alto del triangulo:"))
		area2=(dato2*dato2a)/2
		print("el area del triangulo es:",round(area2))
		triangulito(5)
	elif seleccion2 == "CIRCULO":
		dato3=int(input("ingrese el valor del radio:"))
		area3=(3.1416)*(dato3)**2
		print("el area del circulo es:",area3)
	elif seleccion2 == "RECTANGULO":
		dato4=int(input("ingrese el valor del alto del rectangulo:"))
		dato5=int(input("ingrese el valor del ancho del rectangulo:"))
		area4 = dato4*dato5
		print("el area del rectangulo es:",area4)
		cuadrito(dato4,dato5)
	else:
		print("Introduzca un valor correcto, CUADRADO, TRIANGULO, CIRCULO O RECTANGULO")
	#condicion para seguir con el ciclo o salir del programa
	seguir = int(input("1 para seguir 0 para salir: "))
	if seguir != 1:
		break
print("hasta luego")	

	





