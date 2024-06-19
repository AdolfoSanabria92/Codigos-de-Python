print("Asignacion")
print("Es la manipulacion de una variales en diferentes tiempos, donde solo afecta su contenido pero no su nombre")
mensaje="Hola"
mensaje +=" "
mensaje +="Adolfo"
print (mensaje)

print("LA Concatenacion")
print("Es una operacion que consiste en unir dos cadenas o mas, para formar una cadena de mayor tamaño")
print(" para lo cual se utiliza el signo + ")

mensaje1="Hola"
espacio=" "
nombre="Omar Adolfo"
print(mensaje1+espacio+nombre)

print("concatenacion con números")
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado1 = str(resultado)
print("El resultado es " + resultado1)

print("la Busqueda")
print("consiste en localizar dentro de una cadena, una subcadena mas pequeña a un caracter")
print(" para lo cual se utiliza el metodo 'find' ")

msn= "Hola Omar Adolfo"
buscar_subcadena=msn.find("Omar")
print(buscar_subcadena)


print("La Extraccion")
print("Se trata de sacar fuera de una cadena, una procion de la misma segun su pocision dentro de ella")
print("para ello es necesario indicar la posicion a extraer [´pocicion inicial´ 1:8 ´pocicion final´]")

MEN="Hola Adolfo"
extraer_subcadena=MEN[5:11]
print(extraer_subcadena)

print("La comparacion")
print("se utiliza para comparar dos cadenas de caracteres")
print("para ellos se utiliza el operador ==")

mensaje_uno="hola"
mensaje_dos="hola"
print(mensaje_uno==mensaje_dos)

mensaje_tres="Omar"
mensaje_dos="hola"
print(mensaje_tres==mensaje_dos)
