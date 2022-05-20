import numpy as np 
import sys

class Ordenamiento():
  def _init_(self):
    pass
  def media(self,lista):

    """
    Función que encuentra el valor medio de una lista
    Parámetro: lista de la que se encontrará la media
    Return: número medio
    Restricción: Para listas de tamaño n (un número par) toma la media como el valor en la posición (n/2)+1
    """
    #Se ordena la lista de menor a mayor
    copia_lista= self.quick_sort(lista)
    #Se calcula el índice en el que se encuentra el valor medio
    numero_medio = int(len(copia_lista)/2)
    return copia_lista[numero_medio]

<<<<<<< HEAD

  def quick_sort(self,lista):
    """
    Ordena la lista usando el lgoritmo de ordenamiento quick sort
    Entradas: lista a ordenar
    Return: lista ordenada
    """
=======
  def quick_sort(self, lista):
    """"
    Función que utiliza el algoritmo quicksort para ordenar una lista.
    Parametro: Lista desordenada
    Return: Lista ordenada
    Nota: Se crea una copia de la lista para evitar modificar la lista original.
    """"
>>>>>>> 9de42b0e9f033ffae5f676fa78d4f3b9eeb130da
    lista_fin = lista.copy()

    if len(lista)>1:
      return self.quick_sort_aux(list(lista_fin),[])
    else:
      return self.lista

  def quick_sort_aux(self,lista,lista_ord):
    try:
      elemento_min = min(lista)
      lista_ord.append(elemento_min)
      lista.remove(elemento_min)
      return self.quick_sort_aux(lista,lista_ord)

    except IndexError:
      matriz_res = np.array(lista_ord)
      return matriz_res

    except ValueError:
      elemento_min = lista[0]
      lista_ord.append(elemento_min)
      lista.remove(elemento_min)
<<<<<<< HEAD

  def calcular_matriz_de_medias(self,matriz, contador_fila, ventana):
    #matriz_de_medias= np.ones((len(matriz),len(matriz[0,]) ))*0
    if contador_fila!=len(self.matriz):
      self.calcular_media_ventana(matriz, contador_fila, 0,ventana)
      return self.calcular_matriz_de_medias(matriz, contador_fila+1, ventana)
    else:
      return matriz_de_medias

class Ordenamiento_2():
  def _init_(self):
    pass
  def media(self,lista):

    """
    Función que encuentra el valor medio de una lista
    parámetro: lista de la que se encontrará la media
    Return: número medio
    Restricción: Para listas de tamaño n (un número par) toma la media como el valor en la posición
    """
    #Se ordena la lista de menor a mayor
    copia_lista= self.quick_sort(lista)
    #Se calcula el índice en el que se encuentra el valor medio
    numero_medio = int(len(copia_lista)/2)
    return copia_lista[numero_medio]

  def quick_sort(self,lista):
  """
  Ordena la lista usando el lgoritmo de ordenamiento quick sort
  Entradas: lista a ordenar
  Return: lista ordenada
  """
  if len(lista)>1:
    return self.quick_sort(menores(lista[0], lista[1:],0,[])) + [lista[0]] + quick_sort(mayores(lista[0],lista[1:],0,[]))
  else:
    return lista

def mayores(self, valor,lista, contador,lista_mayores):
  """
  Crea una lista con los valores mayores a un valor dado
  parametro 1: Número con el cual se comparan los números de la lista
  parametro 2: Lista de la cual se desea comparar cada número con valor
  parametro 3: Cuenta la cantidad de iteraciones, sirve para determinar el indice del valor a comparar
  parametro 4: Lista que almacenará los valores de la lista que son mayores que el el número que se recibe en la primer entrada de la función
  Return: Lista con los valores de la lista mayores a valor
  """
  #Si la lista está vacía o tiene un solo elemento
  if len(lista)>1:
    #Si no se ha evaluado el último elemento de la lista
    if contador!=len(lista):
      #Si el número de la lista es mayor o igual que valor
      if valor <= lista[contador]:
        #Agrega el número mayor al final de la lista que contiene los números mayores
        lista_mayores.append(lista[contador])
        contador+=1
        #Llamado recursivo
        return self.mayores(valor, lista, contador, lista_mayores)
      #El número de la lista es menor a valor
      else:
        contador+=1
        return self.mayores(valor,lista, contador, lista_mayores)
    #Se recorrió toda la lista 
    else:
      return lista_mayores
  #Si el único valor de la lista es mayor a valor
  elif lista[0]>=valor:
    return lista
  #La lista está vacía
  else:
      return[]

def menores(self, valor,lista, contador,lista_menores):
  """
  Crea una lista con los valores mayores a un valor dado
  parametro 1: Número con el cual se comparan los números de la lista
  parametro 2: Lista de la cual se desea comparar cada número con valor
  parametro 3: Cuenta la cantidad de iteraciones, sirve para determinar el indice del valor a comparar
  parametro 4: Lista que almacenará los valores de la lista que son mayores que el el número que se recibe en la primer entrada de la función
  Return: Lista con los valores de la lista mayores a valor
  """
  #Si la lista está vacía o tiene un solo elemento
  if len(lista)>1 :
    #Si no se ha evaluado el último elemento de la lista
    if len(lista)>1 and contador!=len(lista):
      #Si el número de la lista es menor que valor
      if valor >lista[contador]:
        #Agrega el número menor al final de la lista que contiene los números menores
        lista_menores.append(lista[contador])
        contador+=1
        #Llamado recursivo
        return self.menores(valor,lista, contador, lista_menores)
      #El número de la lista es menor a valor
      else:
        contador+=1
        return self.menores(valor,lista, contador, lista_menores)
    #Se recorrió toda la lista
    else:
      return lista_menores
  #Si el único valor de la lista es mayor a valor
  elif lista[0]<valor:
    return lista
  #La lista está vacía
  else:
      return[]

=======
>>>>>>> 9de42b0e9f033ffae5f676fa78d4f3b9eeb130da
