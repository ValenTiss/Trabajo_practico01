import numpy as np

class Matriz:

    def __init__(self, lista_de_listas):
        """
        Inicializa la matriz a partir de una lista de listas
        """
        self.matriz_lista_de_listas = lista_de_listas

    def mostrar_contenido(self):
        """
        Muestra el contenido en pantalla de matriz_lista_de_listas
        """
        print(self.matriz_lista_de_listas)

    def get_matriz(self):
        """
        Retorna la lista de listas que representa la matriz
        """
        return self.matriz_lista_de_listas

    def __add__(self, matriz_segundo_operando):
        """
        Sobrecarga del operador +
        param matriz_segundo_operando: matriz que se recibe como segundo operando de la suma
        return: instancia de la clase matriz con la suma
        """
        #se obtiene la lista de listas que representa a la segunda matriz
        matriz2 = matriz_segundo_operando.get_matriz()
        #se verifican los tipos de datos
        if(isinstance(self.matriz_lista_de_listas, list) and isinstance(matriz2, list) and len(self.matriz_lista_de_listas) == len(matriz2) and len(self.matriz_lista_de_listas[0]) == len(matriz2[0])):
            #se invoca la funcion auxiliar
            lista_de_listas_resultado = self.sumar_matrices_aux(self.matriz_lista_de_listas, matriz2, [], [], 0, 0)
            #creamos una instancia de la clase matriz con el resultado
            matriz_suma = Matriz(lista_de_listas_resultado)
            return matriz_suma
        else:
            raise ValueError('Tipos de datos incorrectos o largos diferentes de las matrices')



    def sumar_matrices(self, matriz_segundo_operando):
        """
        Suma dos matrices (instancias de la clase matriz)
        param matriz_segundo_operando: matriz que se recibe como segundo operando de la suma

        """
        #se obtiene la lista de listas que representa a la segunda matriz
        matriz2 = matriz_segundo_operando.get_matriz()
        #se verifican los tipos de datos
        if(isinstance(self.matriz_lista_de_listas, list) and isinstance(matriz2, list) and len(self.matriz_lista_de_listas) == len(matriz2) and len(self.matriz_lista_de_listas[0]) == len(matriz2[0])):
            #se invoca la funcion auxiliar
            lista_de_listas_resultado = self.sumar_matrices_aux(self.matriz_lista_de_listas, matriz2, [], [], 0, 0)
            #creamos una instancia de la clase matriz con el resultado
            matriz_suma = Matriz(lista_de_listas_resultado)
            return matriz_suma
        else:
            raise ValueError('Tipos de datos incorrectos o largos diferentes de las matrices')


    def sumar_matrices_aux(self, matriz1, matriz2, matriz_nueva, matriz_temporal, fila, columna):
        """
        Suma 2 matrices
        param matriz1: primer operando de la suma
        param matriz2: segundo operando de la suma
        param matriz_nueva: acumula el resultado total de la suma matricial
        param matriz_temporal: acumula la suma en la fila actual
        param fila: fila actual a visitar
        param columna: columna actual a visitar
        return: matriz_nueva con el resultado
        """
        #se recorren todas las filas, matriz_nueva acumula el resultado final
        if fila == len(matriz1):
            return matriz_nueva
        else:
            # si ya llego al ultimo elemento de la fila i
            if columna == len(matriz1[fila]):
                #se pasa a otra fila
                fila += 1
                #se reinicia el contador de la columna
                columna = 0
                #se concatena la fila con la suma, a la matriz resultante
                matriz_nueva += [matriz_temporal]
                #se reinicia el acumulador de la fila
                matriz_temporal = []
                #se hace el llamado recursivo para recorrer la proxima fila
                return self.sumar_matrices_aux(matriz1, matriz2, matriz_nueva, matriz_temporal, fila, columna)
            else:
                #se mueve por cada columna en la misma fila
                #suma los elementos correspondientes en matriz1 y matriz2
                suma = matriz1[fila][columna] + matriz2[fila][columna]
                #se concatena la suma a la fila actual
                matriz_temporal += [suma]
                # se continua con la proxima columna
                columna += 1
                #se hace el llamado recursivo en la siguiente columna
                return self.sumar_matrices_aux(matriz1, matriz2, matriz_nueva, matriz_temporal, fila, columna)

def probar_sumar_matrices_OO():
    matriz_1 = Matriz([[2, 3, 1], [1, 5, 7]])
    matriz_2 = Matriz([[3, 5, 7], [1, 50, 7]])
    matriz_suma = matriz_1 + matriz_2

    matriz_suma.mostrar_contenido()
    
def prueba_numpy():
    matriz_1 = np.ones((4, 4)) * 8
    matriz_2 = np.ones((4, 4)) * 3
    matriz_3 = np.array([[221.0, 222, 250, 251, 223, 249], [223.0, 220, 250, 251, 225, 242], [221.0, 0, 250, 251, 221, 249], [221.0, 222, 255, 251, 0, 249], [220.0, 219, 250, 251, 221, 249], [221.0, 222, 250, 251, 223, 249]])
    #suma = matriz_1 + matriz_2    
    #print(suma)
    print(matriz_3)
    print("elemento en 1,1 ", matriz_3[1, 1])
    #slicing:
    K = 3
    origen_fila = 1
    origen_columna = 1
    ventana = matriz_3[0:3, 0:3]
    print("ventana\n ", ventana)
    ventana_vectorizada = ventana.flatten()
    print("ventana vectorizada \n ", ventana_vectorizada)
    
probar_sumar_matrices_OO()
