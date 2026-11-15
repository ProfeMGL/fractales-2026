import matplotlib.pyplot as plt
import numpy as np
import random
#Esta función realiza reresentaciones de cada 10% de los puntos, 
#con el objeto de comprender mejor como se va formando el fractal
def ver_pasos(fx,fy):
    for corte in range(iteraciones//10, int(iteraciones*1.1), iteraciones//10):
        plt.scatter(fx[:corte], fy[:corte], s=5, color="purple") 
        plt.pause(0.5) # Muestra los puntos de a 100 y frena medio segundo
#sortea un vértice distinto del anterior
def sortear_vertices(ultimo):
    eleg=random.randint(0,3)
    while  eleg==ultimo:
        eleg=random.randint(0,3)
    return eleg
#guarda los puntos a representar gráficamente
def fractales(x,fy):
    #Probamos con distintos puntos, dentro y fuera del triangulo e igual funciona.
    p0x=2.0
    p0y=2.0
    ultimo=random.randint(0,3)
    for i in range(iteraciones):
        elegido=sortear_vertices(ultimo)
        #obtenemos las coordenadas del vértice elegido
        vx=coordx[elegido]
        vy=coordy[elegido]
        ultimo=elegido
        #obtenemos el punto a graficar
        x=(p0x+vx)/2;y=(p0y+vy)/2
        fx.append(x)
        fy.append(y)
        p0x=x;p0y=y
    return fx,fy
#Esta función realiza reresentaciones de cada 10% de los puntos, 
#con el objeto de comprender mejor como se va formando el fractal
def ver_pasos(fx,fy):
    for corte in range(iteraciones//10, int(iteraciones*1.1), iteraciones//10):
        plt.scatter(fx[:corte], fy[:corte], s=5, color="purple") 
        plt.pause(0.5) # Muestra los puntos de a 100 y frena medio segundo
#---------------------------------------------------------
iteraciones=10000
coordx=np.array([2,2,0,0])
coordy=np.array([2,0,2,0])
#Agregamos las listas vacias fx, fy donde se van a guardar los puntos intermedios.
fx=[]
fy=[]
fractales(fx,fy)
plt.ion() # Prende la animación
plt.axis("equal") #Establece una cuadrícula 1:1
ver_pasos(fx,fy) 
plt.ioff() # Apaga la animación
print("Finalizado")
plt.show() # Deja la ventana abierta al final