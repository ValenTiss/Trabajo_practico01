import numpy as np 
import sys

class Ordenamiento():
  def __init__(self):
    sys.setrecursionlimit(10**6)

  def media(self,lista):
    """
    Función que encuentra el valor medio de una lista
    parámetro: lista de la que se encontrará la media
    Return: número medio
    Restricción: Para listas de tamaño n (un número par) toma la media como el valor en la posición
    """
    #Se ordena la lista de menor a mayor
    copia_lista= self.quick_sort(list(lista))
    #Se calcula el índice en el que se encuentra el valor medio
    numero_medio = int(len(copia_lista)/2)
    return copia_lista[numero_medio]
    
       

  def quick_sort(self, lista):
    lista_fin = lista.copy()
    if len(lista)>1:
      return self.quick_sort_aux(lista_fin,[])
    else:
      return lista

  def quick_sort_aux(self, lista,lista_ord):
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