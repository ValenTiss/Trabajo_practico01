import sys 
import matplotlib.pyplot as plotter
from PIL import Image, ImageOps
import numpy as np
import time
from ordenamiento_media  import Ordenamiento

class Apertura():
  def probar_apertura_archivo(self):
    """
    Función que pregunta la dirección de la imagen a la que se le desea sacar el filtro de medianas y transforma dicha imagen en una matriz.
    Salida: matriz que contiene los valores de la imagen
    Restricciones: Se debe escribir la dirección de una imagen previamente guardada
    """
    #cambia el limite de la pila
    sys.setrecursionlimit(10**6)
    #lectura de la imagen en escala de grises
    direccion_archivo= input("Introduzca la dirección de la imagen a la que le desea aplicar el filtro de medianas:")
    imagen = Image.open(direccion_archivo)
    #crea la imagen a escala de grises
    gray_image = ImageOps.grayscale(imagen)
    #muestra la imagen
    gray_image.show()
    #convierte la imagen a escala de grises a numpy array
    gray_image_np = np.asarray(gray_image)
    gray_image_lists_py = gray_image_np.tolist()
    return gray_image_np


  def abrir_nuevo_archivo(self,matriz):
    """
    Función que transforma una matriz en una imagen y la muestra.
    Parámetro: Matriz (matriz de madias calculada)
    """
    #Transforma la matriz en una imagen
    image = Image.fromarray(np.array(matriz))
    #muestra la imagen
    image.show() 
