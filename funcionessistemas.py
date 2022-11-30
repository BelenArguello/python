python ="Lenguaje de programación"
print(python.lower())

frase = "Funciones del sistema"
print(frase.lower())

#cadena mayuscula
python="lenguaje de programacion"
print(python.upper())
#cadena mayuscula/minuscula
frase="funciones del sistema"
print(frase.swapcase())

#cadena normal
frase="lenguaje de programacion"
print(frase.capitalize())

#alineacion a la derecha
frase="lenguaje"
f = frase.rjust(20," ")
print(f)

#alineacion a la izquierda
frase="lenguaje"
f = frase.ljust(20, " ")
print(f)

#centrar
frase = "lenguaje"
f = frase.center(20," ")#la cantidad de espacios que quieres, " " es el espacio, tambien se puede agregar =
print(f)


