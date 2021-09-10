"""
Primoaventuras
Al quitarle cuatro años a la edad de Hugo se obtiene dos veces la edad de Paco y si sumamos las edades de Hugo
y Paco se obtiene cinco veces la edad de Luis (todos en años enteros). En el país del Sagrado Corazón de Jesús
se dice que una persona está en etapa 'uno' si está entre 0 y 20 años, en etapa 'dos' si está entre 21 y 30 
años, en etapa 'tres si está entre 31 y 50 años y en etapa 'cuatro' si está por encima de 50 años. Dada la edad
de Paco, realizar un programa que imprima en la primera línea las edades de Paco, Hugo y Luis separadas por un 
solo espacio y en la segunda línea indique en qué etapa se encuentra Luis.
"""
def edades():
    Edad_Paco = int(input("Ingrese la edad de paco: "))
    Edad_Hugo = (Edad_Paco * 2) + 4
    Edad_Luis = (Edad_Paco + Edad_Hugo)//5
    print(Edad_Paco, Edad_Hugo, Edad_Luis)
    if (Edad_Luis >= 0 and Edad_Luis <= 20):
        print("uno")
    elif (Edad_Luis >= 21 and Edad_Luis <= 30):
        print("dos")
    elif (Edad_Luis >= 31 and Edad_Luis <= 50):
        print("tres")
    elif (Edad_Luis >= 51):
        print("cuatro")
    else:
        return False
edades()