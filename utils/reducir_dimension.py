def reducir_dimension(lista):
    salida = []
    for dato in lista:
        for link in dato:
            salida.append(link)
    return salida