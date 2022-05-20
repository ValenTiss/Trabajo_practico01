import sys 
import matplotlib.pyplot as plotter
from PIL import Image, ImageOps
import numpy as np
import time
from calculo_media import Calculo_Media
from Apertura import Apertura


inicio= time.time()
aper = Apertura()
matriz = aper.probar_apertura_archivo()
cm = Calculo_Media(matriz)
dimension_ventana = int(input("Ingrese el tamaño de la ventana: "))
selector = int(input("Ingrese el algoritmo de ordenamiento que quiere usar (1) o (2)"))
if isinstance(dimension_ventana,int) and dimension_ventana % 2 == 1 and isinstance(selector,int) and (1 == selector or selector == 2):
  resultado= cm.calcular_matriz_de_medias(cm.calcular_matriz_de_medias(matriz,0,dimension_ventana,selector),0,dimension_ventana,selector)
  mostrar = aper.abrir_nuevo_archivo(cm.calcular_matriz_de_medias(resultado,0,dimension_ventana,selector))
else:
  raise ValueError("Tipo de dato tiene que ser un entero impar y el algoritmo solo existen dos opciones de algoritmo,intentelo nuevamente.")


fin= time.time()
print("Tiempo que tardo el programa en ejecutarse: "+str(int((fin-inicio))*1000))