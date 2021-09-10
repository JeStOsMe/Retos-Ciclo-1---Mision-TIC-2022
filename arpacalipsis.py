def tipo_melenudos(lista_melenudos):
    sin_repetir = list()
    for melenudo in lista_melenudos:
        if melenudo in sin_repetir:
            continue
        else:
            sin_repetir.append(melenudo)
    return (sin_repetir)

def si_son(turnos, lista_melenudos, melenudo_especifico):
    lista_verificados = list()
    for turno in turnos:
        if lista_melenudos[turno] == melenudo_especifico:
            lista_verificados.append(turno)
    return lista_verificados

def no_estan(turnos_deiv, turnos_james):
    lista_no_estan = list()
    for turno in turnos_deiv:
        if turno not in turnos_james and turno not in lista_no_estan:
            lista_no_estan.append(turno)
    return lista_no_estan



def uno_y_uno(lista_deiv, lista_james):
    lista_uno = list()
    lista_dos = list()
    for turno in lista_deiv:
        if turno not in lista_james and turno not in lista_uno:
            lista_uno.append(turno)
        else:
            continue
    for turno in lista_james:
        if turno not in lista_deiv and turno not in lista_dos:
            lista_dos.append(turno)
        else:
            continue
    if len(lista_uno) > len(lista_dos):
        return len(lista_uno[:len(lista_dos)])
    else:
        return len(lista_dos[:len(lista_uno)])
    