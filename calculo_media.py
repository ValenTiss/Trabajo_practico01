import numpy as np
import sys
import matplotlib.pyplot as plotter
from ordenamiento_media import Ordenamiento,Ordenamiento_2
from Apertura import Apertura


class Calculo_Media():
  
  def __init__(self,matriz):
    self.matriz_de_medias= np.zeros((len(matriz), len( matriz[0,] )))
  
  def calcular_matriz_de_medias(self,matriz, contador_fila, ventana,selector):
    """
    Función que recorre cada una de las filas de la matriz para construir cada fila de la matriz de medianas.
    Parametro 1: matriz a la que se le aplicará el filtro de medianas
    Parametro 2: contador que representa la fila a la cual se calculara la mediana al rededor de cada uno de sus valores
    Parametro 3: tamaño de la ventana
    Parametro 4: Algoritmo de ordenamiento que se desea utilizar. Opciones: 1 o 2
    Return: matriz de medianas, la cual representa la imagen filtrada
    """
    #Si ya se recorrieron todas las filas
    if contador_fila!=len(matriz):
      calcular_media_ventana(self,matriz, contador_fila,0,ventana,selector)
      return self.calcular_matriz_de_medias(matriz, contador_fila+1, ventana,selector)
    else:
      return self.matriz_de_medias


def calcular_media_ventana(self,matriz, fila, contador_columna,ventana,selector):
  """
  Calcula la mediana de cada posición de una fila de la matriz dada una ventana de cierto tamaño.
  Parametro 1: matriz a la que se le aplicará el filtro de medianas
  Parametro 2: fila de la matriz que se recorrerá
  Parametro 3: contador que representa la posición de la fila sobre la que se calculará la ventana
  Parametro 4: tamaño de la ventana
  Parametro 5: Algoritmo de ordenamiento que se desea utilizar. Opciones: 1 o 2
  Return: lista que contiene las medianas de la n-ésima fila de la matriz
  """
  #Si se desea usar el segundo algoritmo de ordenamiento
  if selector == 2 :
    orde = Ordenamiento_2()
  #Si se desea usar el primer algoritmo de ordenamiento
  else:
    orde = Ordenamiento()

  #Cantidad de posiciones a la izquierda/derecha arriba/abajo de la posición específica que pertenecen a la ventana
  radio= int(ventana/2)
  #Si no se ha llegado al final de la columna 
  if len(matriz[fila,])!=contador_columna :
    #Si se está dentro de la ventana y la ventana no se salga de la matriz por arriba ni por abajo
    if contador_columna >= radio and len(matriz)-1-radio >= contador_columna:
      #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
      if fila >= radio and len(matriz[0,])-1-radio >= fila:
        media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:contador_columna+radio+1]
        self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())     
        return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)
      #La ventana se sale de la matriz por la izquierda
      elif fila < radio and len(matriz[0,])-1-radio >= fila:
        media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:contador_columna+radio+1]
        self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())     
        return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)
      #La ventana se sale de la matriz por la derecha
      elif fila >= radio and len(matriz[0,])-1-radio < fila:
        media_por_sacar=matriz[fila-radio: , contador_columna-radio:contador_columna+radio+1]
        self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
        return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)
      #La ventana se sale de la matriz lateralmente por ambos lados
      else:
        media_por_sacar=matriz[0: , contador_columna-radio:contador_columna+radio+1]
        self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())     
        return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)
    #La ventana se sale de la matriz por arriba 
    elif contador_columna < radio and len(matriz)-1-radio >= contador_columna:
      calcular_media_arriba(self,matriz, fila, contador_columna, radio,selector)
      return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)
    #La ventana se sale por abajo
    elif contador_columna >= radio and len(matriz)-1-radio < contador_columna:
      calcular_media_abajo(self,matriz, fila, contador_columna, radio,selector)
      return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)
    #La ventana se sale por arriba y por abajo
    else:
      calcular_media_abajo_arriba(self,matriz, fila, contador_columna, radio,selector)
      return calcular_media_ventana(self,matriz, fila, contador_columna+1,ventana,selector)


def calcular_media_arriba(self,matriz, fila, contador_columna, radio,selector):
  """
  Se calcula la media de una ventana que se sale por arriba
  """
  #Si se desea usar el segundo algoritmo de ordenamiento
  if selector == 2 :
    orde = Ordenamiento_2()
  #Si se desea usar el primer algoritmo de ordenamiento
  else:
    orde = Ordenamiento()
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, 0:contador_columna+radio+1]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, 0:contador_columna+radio+1]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())  
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , 0:contador_columna+radio+1]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())     
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , 0:contador_columna+radio+1]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())     

def calcular_media_abajo(self,matriz, fila, contador_columna, radio,selector):
  """
  Se calcula la media de una ventana que se sale por abajo
  """
  
  if selector == 2 :
    orde = Ordenamiento_2()
  else:
    orde = Ordenamiento()
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , contador_columna-radio:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , contador_columna-radio:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    

def calcular_media_abajo_arriba(self,matriz, fila, contador_columna, radio,selector):
  """
  Se calcula la media de una ventana que se sale por arriba y abajo
  """
  
  if selector == 2 :
    orde = Ordenamiento_2()
  else:
    orde = Ordenamiento()
  #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
  if fila >= radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[fila-radio:fila+radio+1, 0:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la izquierda
  elif fila < radio and len(matriz[0,])-1-radio >= fila:
    media_por_sacar=matriz[0:fila+radio+1, 0:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz por la derecha
  elif fila >= radio and len(matriz[0,])-1-radio < fila:
    media_por_sacar=matriz[fila-radio: , 0:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())    
  #La ventana se sale de la matriz lateralmente por ambos lados
  else:
    media_por_sacar=matriz[0: , 0:]
    self.matriz_de_medias[fila,contador_columna]=orde.media(media_por_sacar.flatten())

def get(self):
  return self.matriz_de_medias
