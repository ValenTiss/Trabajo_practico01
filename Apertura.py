import sys 
import matplotlib.pyplot as plotter
from PIL import Image, ImageOps
import numpy as np
import time
from ordenamiento_media  import Ordenamiento

class Apertura():
  def probar_apertura_archivo(self):
    #cambia el limite de la pila
    sys.setrecursionlimit(10**6)
    #inicializacion en ceros de la imagen
    #lectura de la imagen en escala de grises
    imagen = Image.open('mujerRuido.PNG')
    #crea la imagen a escala de grises
    gray_image = ImageOps.grayscale(imagen)
    gray_image.show()
    #convierte la imagen a escala de grises a numpy array
    gray_image_np = np.asarray(gray_image)
    gray_image_lists_py = gray_image_np.tolist()
    return gray_image_np


  def abrir_nuevo_archivo(self,matriz):
    image = Image.fromarray(np.array(matriz))
    image.show() 