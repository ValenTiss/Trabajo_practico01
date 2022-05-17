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



def calcular_matriz_de_medias(matriz, contador_fila, ventana):
  #matriz_de_medias= np.ones((len(matriz),len(matriz[0,]) ))*0
  if contador_fila!=len(matriz):
    calcular_media_ventana(matriz, contador_fila, 0,ventana)
    return calcular_matriz_de_medias(matriz, contador_fila+1, ventana)
  else:
    return matriz_de_medias


def calcular_media_ventana(matriz, fila, contador_columna,ventana):
  """
  Calcula la mediana de cada posición de una fila de la matriz dada una ventana de cierto tamaño 
  """
  #Cantidad de posiciones a la izquierda/derecha arriba/abajo de la posición específica que pertenecen a la ventana
  radio= int(ventana/2)
  #Si no se ha llegado al final de la columna 
  if len(matriz[fila,])!=contador_columna :
    #Si se está dentro de la ventana y la ventana no se salga de la matriz por arriba ni por abajo
    if contador_columna >= radio and len(matriz)-1-radio >= contador_columna:
      #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
      if fila >= radio and len(matriz[0,])-1-radio >= fila:
        media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:contador_columna+radio+1]
        matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())     
        return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale de la matriz por la izquierda
      elif fila < radio and len(matriz[0,])-1-radio >= fila:
        media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:contador_columna+radio+1]
        matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())     
        return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale de la matriz por la derecha
      elif fila >= radio and len(matriz[0,])-1-radio < fila:
        media_por_sacar=matriz[fila-radio: , contador_columna-radio:contador_columna+radio+1]
        matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
        return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale de la matriz lateralmente por ambos lados
      else:
        media_por_sacar=matriz[0: , contador_columna-radio:contador_columna+radio+1]
        matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())     
        return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    #La ventana se sale de la matriz por arriba 
    elif contador_columna < radio and len(matriz)-1-radio >= contador_columna:
      calcular_media_arriba(matriz, fila, contador_columna, radio)
      return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    #La ventana se sale por abajo
    elif contador_columna >= radio and len(matriz)-1-radio < contador_columna:
      calcular_media_abajo(matriz, fila, contador_columna, radio)
      return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    #La ventana se sale por arriba y por abajo
    else:
      calcular_media_abajo_arriba(matriz, fila, contador_columna, radio)
      return calcular_media_ventana(matriz, fila, contador_columna+1,ventana)


def calcular_media_arriba(matriz, fila, contador_columna, radio):
  """
  Se calcula la media de una ventana que se sale por arriba
  """
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, 0:contador_columna+radio+1]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, 0:contador_columna+radio+1]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())  
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , 0:contador_columna+radio+1]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())     
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , 0:contador_columna+radio+1]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())     



def calcular_media_abajo(matriz, fila, contador_columna, radio):
  """
  Se calcula la media de una ventana que se sale por abajo
  """
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , contador_columna-radio:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , contador_columna-radio:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    


def calcular_media_abajo_arriba(matriz, fila, contador_columna, radio):
  """
  Se calcula la media de una ventana que se sale por arriba y abajo
  """
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, 0:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, 0:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , 0:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , 0:]
    matriz_de_medias[fila,contador_columna]=media(media_por_sacar.flatten())    




inicio= time.time()
matriz= probar_apertura_archivo()
#print(d,"\n")
#calcular_media_ventana(d, 0, 0,3)
#print(matriz_de_medias)
#matriz=np.random.randint(500, size=(520, 500))
matriz_de_medias= np.zeros((len(matriz), len( matriz[0,] ))) 
resultado= calcular_matriz_de_medias(matriz,0,9)
#print(resultado)
fin= time.time()
print(fin-inicio)
final = abrir_nuevo_archivo(resultado)

