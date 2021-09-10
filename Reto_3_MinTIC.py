'''
James Hammett y Kirk Hetfield ya están en Colombia, y su juego ArpaLlanera Hero ha sido todo un éxito. 
Sin embargo, el juego se les está haciendo un poco predecible y repetitivo, así que deciden consultar a Cliff 
Newsted y a Lars Trujillo por alguna idea innovadora para sacar la versión Pro del video juego. Éstos deciden 
sentarse a estudiar escalas y entrenar el oído musical, y se les ocurre una variación del juego para hacerlo 
más entretenido.

La dinámica del nuevo componente es la siguiente: en el juego van a sonar una serie de cuerdas, una cuerda a la
vez, y cada cuerda asociada a una letra distinta del alfabeto; lamentablemente, el sonido algunas veces no suena
con calidad perfecta, así que el sonido de la cuerda puede llegar representado por la letra del alfabeto en 
minúscula o en mayúscula. La idea es que la persona luego de escuchar la sucesión de sonidos, determine en 
primera instancia cuál cuerda sonó y cuántas veces sono la misma cuerda de manera consecutiva.

Un ejemplo sencillo de ésta dinámica se puede hacer con la canción “Master of Python”, que inicia con la 
secuencia: E,E,e,E,E,d,E,E,D,c,C. En este caso, los sonidos inferidos serán E (con cinco repeticiones), D 
(con una repetición), E (con dos repeticiones), D (con una repetición), y C (con dos repeticiones).

Como usted cumple ahora dos roles, "jalacables" y programador, decide construir un programa que resuelve la 
extensión propuesta. En este caso, usted va a hacer un programa que recibe la sucesión de cuerdas que está 
escuchando (y adivinando) el jugador, que puede estar en minúscula o en mayúscula, y cada sonido separado por 
coma. La salida debe ser en primera instancia la sucesión de cuerdas, representadas en mayúscula, sin tener en 
cuenta los sonidos repetidos, y debajo de cada cuerda, la cantidad de veces que sonó esta de manera consecutiva.
'''
def juego(notas):
    notas = notas.split(",")
    lista_1 = list(notas[0].upper())
    lista_2 = [0]
    indice = 0
    for nota in notas:
        if nota.upper() == lista_1[indice]:
            lista_2[indice] += 1
        else:
            lista_1.append(nota.upper())
            lista_2.append(1)
            indice += 1
    return lista_1, lista_2

notas = input("Ingrese las notas musicales que adivinó, separadas por comas: ")
adivinadas, puntaje = juego(notas)
for nota in adivinadas:
    print(nota, end=" ")
print()
for puntos in puntaje:
    print(puntos, end=" ")

#Hecho por Jeaniel Osorno, para MisionTIC 2022