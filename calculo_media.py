import numpy as np
import sys
import matplotlib.pyplot as plotter
from ordenamiento_media import Ordenamiento
class Calculo_Media():
  def __init__(self):
    sys.setrecursionlimit(10**6)
    

  def calcular_media_ventana(self, matriz, fila, contador_columna, ventana):
    """
    Calcula la mediana de cada posición de una fila de la matriz dada una ventana de cierto tamaño 
    """
    #Cantidad de posiciones a la izquierda/derecha arriba/abajo de la posición específica que pertenecen a la ventana
    orde = Ordenamiento()
    radio= int(ventana/2)
    #Si no se ha llegado al final de la columna 
    if len(matriz[fila,])!=contador_columna :
      #Si se está dentro de la ventana y la ventana no se salga de la matriz por arriba ni por abajo
      if contador_columna >= radio and len(matriz)-1-radio >= contador_columna:
        #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
        if fila >= radio and len(matriz[0,])-1-radio >= fila:
          media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:contador_columna+radio+1]    
          return [orde.media(media_por_sacar.flatten())] + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)        
        #La ventana se sale de la matriz por la izquierda
        elif fila < radio and len(matriz[0,])-1-radio >= fila:
          media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:contador_columna+radio+1]        
          return [orde.media(media_por_sacar.flatten())] + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
        #La ventana se sale de la matriz por la derecha
        elif fila >= radio and len(matriz[0,])-1-radio < fila:
          media_por_sacar=matriz[fila-radio: , contador_columna-radio:contador_columna+radio+1]            
          return [orde.media(media_por_sacar.flatten())] + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
        #La ventana se sale de la matriz lateralmente por ambos lados
        else:
          media_por_sacar=matriz[0: , contador_columna-radio:contador_columna+radio+1]             
          return [orde.media(media_por_sacar.flatten())] + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale de la matriz por arriba 
      elif contador_columna < radio and len(matriz)-1-radio >= contador_columna:     
        return self.calcular_media_arriba(matriz, fila, contador_columna, radio) + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale por abajo
      elif contador_columna >= radio and len(matriz)-1-radio < contador_columna:      
        return self.calcular_media_abajo(matriz, fila, contador_columna, radio) + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
      #La ventana se sale por arriba y por abajo
      else:      
        return self.calcular_media_abajo_arriba(matriz, fila, contador_columna, radio) + self.calcular_media_ventana(matriz, fila, contador_columna+1,ventana)
    else:
      return []

  def calcular_media_arriba(self, matriz, fila, contador_columna, radio):

    """
    Se calcula la media de una ventana que se sale por arriba
    """
    orde = Ordenamiento()
    #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
    if fila >= radio and len(matriz[0,])-1-radio >= fila:
      media_por_sacar=matriz[fila-radio:fila+radio+1, 0:contador_columna+radio+1]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz por la izquierda
    elif fila < radio and len(matriz[0,])-1-radio >= fila:
      media_por_sacar=matriz[0:fila+radio+1,0:contador_columna+radio+1]
      return [orde.media(media_por_sacar.flatten())]  
    #La ventana se sale de la matriz por la derecha
    elif fila >= radio and len(matriz[0,])-1-radio < fila:
      media_por_sacar=matriz[fila-radio: , 0:contador_columna+radio+1]
      return [orde.media(media_por_sacar.flatten())]     
    #La ventana se sale de la matriz lateralmente por ambos lados
    else:
      media_por_sacar=matriz[0: , 0:contador_columna+radio+1]
      return [orde.media(media_por_sacar.flatten())]     

  def calcular_media_abajo(self, matriz, fila, contador_columna, radio):
    """
    Se calcula la media de una ventana que se sale por abajo
    """
    orde = Ordenamiento()
    #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
    if fila >= radio and len(matriz[0,])-1-radio >= fila:
      media_por_sacar=matriz[fila-radio:fila+radio+1, contador_columna-radio:]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz por la izquierda
    elif fila < radio and len(matriz[0,])-1-radio >= fila:
      media_por_sacar=matriz[0:fila+radio+1, contador_columna-radio:]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz por la derecha
    elif fila >= radio and len(matriz[0,])-1-radio < fila:
      media_por_sacar=matriz[fila-radio: , contador_columna-radio:]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz lateralmente por ambos lados
    else:
      media_por_sacar=matriz[0: , contador_columna-radio:]
      return [orde.media(media_por_sacar.flatten())]    

  def calcular_media_abajo_arriba(self, matriz, fila, contador_columna, radio):
    """
    Se calcula la media de una ventana que se sale por arriba y abajo
    """
    orde = Ordenamiento()
    #Si la ventana no se sale de la matriz por la derecha ni por la izquierda
    if fila >= radio and len(matriz[0,])-1-radio >= fila:
      media_por_sacar=matriz[fila-radio:fila+radio+1, 0:]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz por la izquierda
    elif fila < radio and len(matriz[0,])-1-radio >= fila:
      media_por_sacar=matriz[0:fila+radio+1, 0:]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz por la derecha
    elif fila >= radio and len(matriz[0,])-1-radio < fila:
      media_por_sacar=matriz[fila-radio: , 0:]
      return [orde.media(media_por_sacar.flatten())]    
    #La ventana se sale de la matriz lateralmente por ambos lados
    else:
      media_por_sacar=matriz[0: , 0:]
      return [orde.media(media_por_sacar.flatten())]




    

