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
if isinstance(dimension_ventana,int) and dimension_ventana % 2 == 1:
  resultado= cm.calcular_matriz_de_medias(cm.calcular_matriz_de_medias(matriz,0,dimension_ventana),0,dimension_ventana)
  mostrar = aper.abrir_nuevo_archivo(cm.calcular_matriz_de_medias(resultado,0,dimension_ventana))
else:
  raise ValueError("Tipo de dato tiene que ser un entero impar")


fin= time.time()
print("Tiempo que tardo el programa en ejecutarse"+str((fin-inicio)*1000))