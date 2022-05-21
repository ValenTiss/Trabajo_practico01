import sys 
import matplotlib.pyplot as plotter
from PIL import Image, ImageOps
import numpy as np
import time #Clase que permite mostrar el tiempo de ejecución del sistema
from calculo_media import Calculo_Media #Clase que sirve para calcular el filtro de medias a una matriz
from Apertura import Apertura #Clase creada para convertir la imagen y mostrarla


#Se crea una instancia de la clase Apertura
aper = Apertura()
#Matriz que contiene la imagen
matriz = aper.probar_apertura_archivo()
#Instancia de la clase Calculo_Media
cm = Calculo_Media(matriz)
#Tamaño de la ventana
dimension_ventana = int(input("Ingrese el tamaño de la ventana: "))
#Opción de algoritmo de ordenamiento que se quiera usar
selector = int(input("Ingrese el algoritmo de ordenamiento que quiere usar (1) o (2)"))
#Si los datos introducidos por el usuario son los esperados
if isinstance(dimension_ventana,int) and dimension_ventana % 2 == 1 and isinstance(selector,int) and (1 == selector or selector == 2):
  #Calcula el momento en que se empieza a correr el programa
  inicio= time.time()
  #Calcula 2 veces el filtro de medianas
  resultado= cm.calcular_matriz_de_medias(cm.calcular_matriz_de_medias(matriz,0,dimension_ventana,selector),0,dimension_ventana,selector)
  #Calcula el filtro de medianas nuevamente y muestra la imagen generada
  mostrar = aper.abrir_nuevo_archivo(cm.calcular_matriz_de_medias(matriz,0,dimension_ventana,selector))
else:
  raise ValueError("Tipo de dato tiene que ser un entero impar y el algoritmo solo existen dos opciones de algoritmo,intentelo nuevamente.")

#Momento de finalización de la prueba
fin= time.time()

print("Tiempo que tardo el programa en ejecutarse: "+str(int((fin-inicio)*1000)) + " milisegundos.")

