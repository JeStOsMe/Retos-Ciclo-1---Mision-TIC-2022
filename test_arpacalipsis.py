from arpacalipsis import *
#Para la funcion tipo_melenudos()
lista_funcion_1 = ["jalacables", "poguero", "jalacables", "showsero", "poguero", "poguero"]
print(tipo_melenudos(lista_funcion_1))

#Para la funcion si_son()
turnos = [1, 3, 5, 7]
melenudos = ["jalacables", "poguero", "jalacables", "showsero", "poguero", "poguero", "showsero", "jalacables"]
melenudo_especifico = "jalacables"
print(si_son(turnos, melenudos, melenudo_especifico))

#Para la funcion no_estan()
lista_deiv_1 = [1, 2, 3, 5, 7, 8]
lista_james_1 = [2, 3, 7, 8]
print(no_estan(lista_deiv_1, lista_james_1))

#Para la funcion uno_y_uno()
lista_deiv_2 = [1, 2, 4, 5, 7, 8]
lista_james_2 = [2, 3, 7, 8]
print(uno_y_uno(lista_deiv_2, lista_james_2))

#DATOS QUE ME ENTREGA EL JUEZ
print("! " * 30)
#Para la función si_son:
turnos = [13, 30, 43, 11, 26, 18, 16, 42, 39, 33, 45, 34, 29, 35, 47, 9, 17, 21, 3]
melenudos = [3, 2, 1, 3, 1, 5, 5, 4, 5, 2, 5, 3, 4, 3, 4, 2, 2, 1, 4, 3, 2, 2, 2, 4, 5, 5, 3, 1, 5, 1, 4, 2, 1, 4, 1, 5, 1, 3, 1, 4, 4, 1, 1, 1, 4, 3, 4, 2]
melenudo_especifico = 4
print(si_son(turnos, melenudos, melenudo_especifico))

#Para la funcion no_estan:
lista_deiv_1 = [11, 5, 12, 20, 0, 19, 1, 27, 26, 8, 15, 28, 22, 14]
lista_james_1 = [5, 11, 8, 6, 10, 25, 12, 24, 23, 31, 3, 28, 2, 29, 27]
print(no_estan(lista_deiv_1, lista_james_1))

#Para la funcion uno_y_uno:
lista_deiv_2 = [6, 13, 23, 5, 8, 16, 22, 20, 25, 7, 0, 24, 21, 12, 19]
lista_james_2 = [5, 6, 3, 1, 7, 13, 24, 17, 19, 23, 14, 16]
print(uno_y_uno(lista_deiv_2, lista_james_2))