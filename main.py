import sys 

import matplotlib.pyplot as plotter
from PIL import Image, ImageOps
import numpy as np
import time


def probar_apertura_archivo():
    #cambia el limite de la pila
    sys.setrecursionlimit(10**6)
    numFilas = 60;
    numColumnas = 60;
    #inicializacion en ceros de la imagen
    imagen_vacia = np.zeros((numFilas, numColumnas))
    #print("Test 1 running");
    #lectura de la imagen en escala de grises
    imagen = Image.open('mujerRuido.PNG')
    #imagen.show()
    
    #crea la imagen a escala de grises
    gray_image = ImageOps.grayscale(imagen)
    gray_image.show()
    #convierte la imagen a escala de grises a numpy array
    gray_image_np = np.asarray(gray_image)
   
    gray_image_lists_py = gray_image_np.tolist()
    num_filas = len(gray_image_lists_py)
    #print("numero de filas ", num_filas)
    num_columnas = len(gray_image_lists_py[0])
    #print("numero de columnas ", num_columnas)
    return gray_image_np


def abrir_nuevo_archivo(matriz):
  image = Image.fromarray(matriz)
  image.show() 

#---------------------------------------------------------------------------------------------------------
def media(lista):
        """
        Función que encuentra el valor medio de una lista
        parámetro: lista de la que se encontrará la media
        Return: número medio
        Restricción: Para listas de tamaño n (un número par) toma la media como el valor en la posición
        """
        #Se ordena la lista de menor a mayor
        copia_lista= quick_sort(lista)
        #Se calcula el índice en el que se encuentra el valor medio
        numero_medio = int(len(copia_lista)/2)
        return copia_lista[numero_medio]

def quick_sort(lista):
  lista_fin = lista.copy()
  if len(lista)>1:
    return quick_sort_aux(list(lista_fin),[])
  else:
    return lista

def quick_sort_aux(lista,lista_ord):
  try:
    elemento_min = min(lista)
    lista_ord.append(elemento_min)
    lista.remove(elemento_min)
    return quick_sort_aux(lista,lista_ord)

  except IndexError:
    matriz_res = np.array(lista_ord)
    return matriz_res

  except ValueError:
    elemento_min = lista[0]
    lista_ord.append(elemento_min)
    lista.remove(elemento_min)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

a=[1,2,3,4,5,6,7]
b=[1,2,3,4,5,6,7]
c=[1,2,3,4,5,6,7]
e=[1,2,3,4,5,6,7]
f=[1,2,3,4,5,6,7]
g=[1,2,3,4,5,6,7]
h=[1,2,3,4,5,6,0]
#d=np.array([a,b,c,e,f,g,h])
#print(len(d[6,]))





#-----------------------------------------------------------------------------------------------------------
def calcular_matriz_de_medias(matriz, contador_fila, ventana):
  if contador_fila!=len(matriz):
    resultado= calcular_media_ventana(matriz, contador_fila, 0,ventana)
    return [resultado]+calcular_matriz_de_medias(matriz, contador_fila+1, ventana)
  else:
    return []




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
        return [media(media_por_sacar.flatten())] + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)        
      #La ventana se sale de la matriz por la izquierda
      elif fila < radio and len(matriz[0,])-1-radio >= fila:
        media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:contador_columna+radio+1]        
        return [media(media_por_sacar.flatten())] + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale de la matriz por la derecha
      elif fila >= radio and len(matriz[0,])-1-radio < fila:
        media_por_sacar=matriz[fila-radio: , contador_columna-radio:contador_columna+radio+1]            
        return [media(media_por_sacar.flatten())] + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale de la matriz lateralmente por ambos lados
      else:
        media_por_sacar=matriz[0: , contador_columna-radio:contador_columna+radio+1]             
        return [media(media_por_sacar.flatten())] + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    #La ventana se sale de la matriz por arriba 
    elif contador_columna < radio and len(matriz)-1-radio >= contador_columna:     
      return calcular_media_arriba(matriz, fila, contador_columna, radio) + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    #La ventana se sale por abajo
    elif contador_columna >= radio and len(matriz)-1-radio < contador_columna:      
      return calcular_media_abajo(matriz, fila, contador_columna, radio) + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    #La ventana se sale por arriba y por abajo
    else:      
      return calcular_media_abajo_arriba(matriz, fila, contador_columna, radio) + calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
  else:
    return []

def calcular_media_arriba(matriz, fila, contador_columna, radio):
  """
  Se calcula la media de una ventana que se sale por arriba
  """
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, 0:contador_columna+radio+1]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, 0:contador_columna+radio+1]
    return [media(media_por_sacar.flatten())]  
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , 0:contador_columna+radio+1]
    return [media(media_por_sacar.flatten())]     
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , 0:contador_columna+radio+1]
    return [media(media_por_sacar.flatten())]     



def calcular_media_abajo(matriz, fila, contador_columna, radio):
  """
  Se calcula la media de una ventana que se sale por abajo
  """
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , contador_columna-radio:]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , contador_columna-radio:]
    return [media(media_por_sacar.flatten())]    


def calcular_media_abajo_arriba(matriz, fila, contador_columna, radio):
  """
  Se calcula la media de una ventana que se sale por arriba y abajo
  """
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, 0:]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, 0:]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , 0:]
    return [media(media_por_sacar.flatten())]    
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , 0:]
    return [media(media_por_sacar.flatten())]


inicio= time.time()
matriz = probar_apertura_archivo()
resultado= calcular_matriz_de_medias(np.array(calcular_matriz_de_medias(matriz,0,3)),0,3)
mostrar = abrir_nuevo_archivo(np.array(calcular_matriz_de_medias(np.array(resultado),0,3)))
fin= time.time()
print(fin-inicio)
