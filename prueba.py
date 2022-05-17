import sys 
import numpy as np 
"""
def quick_sort(lista):
  if len(lista)>1:
    return quick_sort_aux(list(lista),[])
  else:
    return lista

def quick_sort_aux(lista,lista_ord):
	lista_fin = lista.copy()
	for i in range(0,len(lista_fin)):
		lista_fin[i] = int(lista_fin[i])
	
	try:
		elemento_min = min(lista_fin)
		lista_ord.append(elemento_min)
		lista_fin.remove(elemento_min)
		return quick_sort_aux(lista_fin,lista_ord)

	except IndexError:
		matriz_res = np.array(lista_ord)
		return matriz_res

	except ValueError:
		elemento_min = lista_fin[0]
		lista_ord.append(elemento_min)
		lista_fin.remove(elemento_min)
"""
matriz = np.array([1,2,3,4,5,6,2,54,78])
resultado = quick_sort(matriz)
print(resultado)



def quick_sort(lista):
  """
  Ordena la lista usando el lgoritmo de ordenamiento quick sort
  Entradas: lista a ordenar
  Return: lista ordenada
  """
  if len(lista)>1:
    return quick_sort(menores(lista[0], lista[1:],0,[])) + [lista[0]] + quick_sort(mayores(lista[0],lista[1:],0,[]))
  else:
    return lista

def mayores(valor,lista, contador,lista_mayores):
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
        return mayores(valor, lista, contador, lista_mayores)
      #El número de la lista es menor a valor
      else:
        contador+=1
        return mayores(valor,lista, contador, lista_mayores)
    #Se recorrió toda la lista 
    else:
      return lista_mayores
  #Si el único valor de la lista es mayor a valor
  elif lista[0]>=valor:
    return lista
  #La lista está vacía
  else:
      return[]

def menores(valor,lista, contador,lista_menores):
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
        return menores(valor,lista, contador, lista_menores)
      #El número de la lista es menor a valor
      else:
        contador+=1
        return menores(valor,lista, contador, lista_menores)
    #Se recorrió toda la lista
    else:
      return lista_menores
  #Si el único valor de la lista es mayor a valor
  elif lista[0]<valor:
    return lista
  #La lista está vacía
  else:
      return[]

#lista=[2,2,3,2,5,2,7,2]
#lista=[9,8,7,6,5,4,3,2]
#lista=[1,9,2,8,6,5,7,3,2,1]
#lista=[84,3,2,1,7,6,5]
#lista=[0,1,2,3]
#lista=[0,1]
#lista=[1,0]
#lista=[]
#lista=[3]
lista=[3,2,0,5,9,5]
#print("qs: ", quick_sort(lista), "   lista: ", lista)
#media(lista)

