import sys 
import matplotlib.pyplot as plotter
from PIL import Image, ImageOps
import numpy as np
import time
from calculo_media import Calculo_Media
from ordenamiento_media  import Ordenamiento


def probar_apertura_archivo():
    """
    Función que busca una imagen en la dirección digitada y la transforma en una matriz 
    Return: matriz de la imagen
    Restricción: Se debe digitar correctamente la dirección de la imagen previamente guardada que se desea filtrar
    """
    #cambia el limite de la pila
    #sys.setrecursionlimit(10**6)
    #inicializacion en ceros de la imagen
    #lectura de la imagen en escala de grises
    imagen = Image.open('pixelesimagen.jpeg')
    #crea la imagen a escala de grises
    gray_image = ImageOps.grayscale(imagen)
    gray_image.show()
    #convierte la imagen a escala de grises a numpy array
    gray_image_np = np.asarray(gray_image)
    gray_image_lists_py = gray_image_np.tolist()
    return gray_image_np


def abrir_nuevo_archivo(matriz):
    """
    Función que transforma en una imagen una matriz recibida
    """
    image = Image.fromarray(matriz)
    image.show() 


def calcular_matriz_de_medias(matriz, contador_fila, ventana):
  if contador_fila!=len(matriz):
    calculo_media = Calculo_Media()
    resultado = calculo_media.calcular_media_ventana(matriz,0,contador_fila,ventana)
    return [resultado]+calcular_matriz_de_medias(matriz, contador_fila+1, ventana)
  else:
    return []



inicio= time.time()
matriz = probar_apertura_archivo()
resultado= np.array(calcular_matriz_de_medias(np.array(calcular_matriz_de_medias(matriz,0,3)),0,3))
print(resultado)
mostrar = abrir_nuevo_archivo(np.array(calcular_matriz_de_medias(np.array(resultado), 0,3)))
fin= time.time()
print(fin-inicio)
