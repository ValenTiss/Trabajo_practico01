def intecambiar(posicion_1, posicion_2, lista):
    """
    Intercambia los valores en la lista lista, en posicion_1  y posicion_2
    param posicion_1: primer posicion a intercambiar
    param posicion_2: segunda posicion a intercambiar
    return: lista con los elementos intercambiados
    """
    variable_temporal = lista[posicion_1]
    lista[posicion_1] = lista[posicion_2]
    lista[posicion_2] = variable_temporal
    return lista


def ordenar_por_seleccion(lista_a_ordenar):
    """
    Ordena una lista usando el algoritmo de seleccion
    param lista_a_ordenar
    return: lista_ordenada
    """
    
    largo_lista = len(lista_a_ordenar)
    #va moviendo el pivote para buscar el menor elemento en la sublista desde el pivote hasta n
    for pivote in range(0, largo_lista):
        #placeholder
        (posicion_minimo, valor_minimo) = buscar_posicion_min(lista_a_ordenar, pivote)
        #realizar el intercambio
        lista_a_ordenar = intecambiar(pivote, posicion_minimo, lista_a_ordenar)
    return lista_a_ordenar
    
    
def buscar_posicion_min(lista, posicion_inicial):
    """
    Busca el menor elemento y su posicion en la lista desde posicion_inicial hasta el final
    param lista: lista de elementos
    param posicion_inicial: pivote desde donde se hace la busqueda
    return: valor y posicion del minimo
    """
    #variables que guardan el minimo y su posicion
    valor_minimo = 99999
    posicion_minimo = -1
    #pasa por todos los elementos en la sublista
    for i in range(posicion_inicial, len(lista)):
        #se encontro un nuevo valor mas chiquito
        if(lista[i] < valor_minimo):
            valor_minimo = lista[i]
            posicion_minimo = i
    #retorna el valor minimo y su posicion
    return (posicion_minimo, valor_minimo)
