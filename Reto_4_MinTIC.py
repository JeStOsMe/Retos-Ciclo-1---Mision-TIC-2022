'''ArpaLlanera Hero: "Fail in the Note"

Conjunto de cuerdas válidas = {"i": 90, "n": 25, "t": 32, "l": 24, "j": 23, "r": 54, "h": 34, "z": 36, "p": 95, "k": 86, "e": 67, "g": 27, "u": 54, "x": 57, "m": 94}
Cuerdas escritas por el jugador: r-p-q-g-h-k-l-x-b-s-o-e-y-m-z
Entonces el puntaje sería 574, debido a que las notas válidas a las que atino el jugador son: r,p,g,h,k,l,x,e,m,z; así que el puntaje se calcula: 54+95+27+34+86+24+57+67+94+36=574.

Usted se cansó de ser el jalacables de los otros melenudos raros, así que se contacta con Deiv para desarrollar el video juego en versión de móvil. Así, usted va a desarrollar un programa que reciba el conjunto de cuerdas válidas junto con el puntaje que otorgan, y las cuerdas escritas por el jugador seperadas por un guión. Calculará el puntaje, y se lo mostrará al usuario, junto con las cuerdas correctas de las escritas por el jugador, y separadas por coma.

    Entrada

En la primera línea, va a recibir una cadena de caracteres, que contendrá un diccionario cuyas claves serán cadenas de caracteres y sus valores serán números enteros. En la segunda línea, va a recibir una cadena de caracteres que corresponde a las cuerdas escritas por el jugador, y separadas por guión.

    Salida

En la primera línea se debe escribir el puntaje obtenido por el jugador. En la segunda línea, se debe escribir una cadena de caracteres con las cuerdas válidas que atino el jugador, en el mismo orden que las escribió el jugador, y separadas por coma.
'''

def convertir_a_diccionario(cuerdas):
    diccionario = dict()
    cuerdas = cuerdas.split("{")
    cuerdas = cuerdas[1].split("}")
    cuerdas = cuerdas[0].split(", ")
    for elemento in cuerdas:
        elemento = elemento.split(": ")
        diccionario[str(elemento[0].split('"')[1])] = int(elemento[1])
    return diccionario
def obteniendo_puntaje(cuerdas, juego):
    puntaje = 0
    acertados = list()
    for i in range(len(juego)):
        if juego[i] in cuerdas.keys():
            puntaje += cuerdas[juego[i]]
            acertados.append(juego[i])
    print(puntaje)
    for i in range(len(acertados)):
        if i == (len(acertados) - 1):
            print(acertados[i])
        else:
            print(acertados[i], end=",")

cuerdas = input("Ingrese las notas que jugaran, con su respectivo puntaje: ")
cuerdas = convertir_a_diccionario(cuerdas)
juego = input("Ingrese las notas a atinar, separadas por guiones: ")
juego = juego.split("-")
obteniendo_puntaje(cuerdas, juego)

#Hecho por Jeaniel Osorno, 02/07/2021
