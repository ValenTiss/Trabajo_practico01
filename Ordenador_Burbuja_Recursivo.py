class Ordenador_Burbuja_Recursivo:

    def intercambiar(self, lista, posicion_1, posicion_2):
        """
        Intercambia los elementos de la posicion_1 a la posicion_2
        param posicion_1: se asume posicion valida dentro de la lista
        param posicion_2: se asume posicion valida dentro de la lista
        return: lista con el intercambio de los elementos
        """
        var_temporal = lista[posicion_1]
        lista[posicion_1] = lista[posicion_2]
        lista[posicion_2] = var_temporal


    def flotar_burbuja(self, lista, pivote_burbuja, posicion_actual):
        """
        Recibe una lista, con un pivote de la burbuja y la posicion actual para flotar
        la burbuja
        param pivote_burbuja: limite maximo hasta donde puede flotar la burbuja
        param posicion_actual: pivote que indica la posicion que analiza para el intercambio 
        (flotado de la burbuja)    
        """
        #siempre y cuando la posicion_actual no este antes del pivote de la burbuja
        #se sigue analizando la lista desde posicion_actual hasta pivote_burbuja
        if(posicion_actual < pivote_burbuja):
            #verifica si se debe hacer el intercambio (para que flote la burbuja)
            if(lista[posicion_actual] > lista[posicion_actual + 1]):
                #se realiza el intercambio en caso afirmativo
                self.intercambiar(lista, posicion_actual, posicion_actual + 1)
            #se hace el llamado recursivo incrementando la posicion_actual
            return self.flotar_burbuja(lista, pivote_burbuja, posicion_actual + 1)    

    def ordenar(self, lista):
        """
        Ordena la lista de forma ascendente
        param lista: lista a ordenar
        return: lista ordenada
        """
        lista_copia = lista.copy()
        if(isinstance(lista, list)):
            #se inicializa el pivote de la burbuja
            pivote_burbuja = len(lista_copia) - 1 
            return self.ordenar_burbuja_aux(lista_copia, pivote_burbuja)
        else:
            raise ValueError("Tipo de datos incorrecto")

    def ordenar_burbuja_aux(self, lista, pivote_burbuja):
        """
        Funcion que implementa de forma recursiva el algoritmo de burbuja
        param lista: lista a ordenar
        param pivote_burbuja: marca hasta donde debe flotar la burbuja
        return: lista ordenada
        """
        #se verifica que el pivote_burbuja no haya llegado al inicio de la lista
        if(pivote_burbuja > 0):
            #se inicializa la posicion_actual siempre en 0
            posicion_actual = 0
            #se invoca a flotar_burbuja
            self.flotar_burbuja(lista, pivote_burbuja, posicion_actual)
            #se hace un llamado recursivo
            pivote_burbuja -= 1
            return self.ordenar_burbuja_aux(lista, pivote_burbuja)
        else:
            #se llega a la condicion de parada, por lo que se retorna la lista
            return lista

def probar_algoritmo_burbuja():
    lista_1 = [3, 7, 2, 1, -1] 
    print("lista_1 antes de ordenar ", lista_1)
    #se construye la instancia del ordenador
    ordenador_burbuja = Ordenador_Burbuja_Recursivo()
    #se invoca al metodo ordenar del ordenador_burbuja
    lista_ordenada = ordenador_burbuja.ordenar(lista_1)
    print("lista_1 despues de ordenar ", lista_1)
    print("lista_ordenada ", lista_ordenada)
    
probar_algoritmo_burbuja()
