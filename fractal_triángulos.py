#Bibliotecas que se importan
import matplotlib.pyplot as plt
import numpy as np
import random
# Funciones y procedimientos
#Esta función realiza reresentaciones de cada 10% de los puntos, 
#con el objeto de comprender mejor como se va formando el fractal
def ver_pasos(fx,fy):
    plt.ion() # Prende la animación
    for corte in range(iteraciones//10, int(iteraciones*1.1), iteraciones//10):
        plt.scatter(fx[:corte], fy[:corte], s=5, color="purple") 
        plt.pause(0.5) # Muestra los puntos de a 100 y frena medio segundo
    plt.ioff() # Apaga la animación
    plt.show() # Deja la ventana abierta al final
#Se ingresan las coordenadas de los vértices, tanto en formato latino como anglosajón
def ingresa_vertices_triang():
    print ("Ingresá dos puntos")
    entrada=input("Coordenada X del primer vértice: ")
    vert0x=float(entrada.replace(",","."))
    entrada=input("Coordenada Y del primer vértice: ")
    vert0y=float(entrada.replace(",","."))
    entrada=input("Coordenada X del segundo vértice: ")
    vert1x=float(entrada.replace(",","."))
    entrada=input("Coordenada Y del segundo vértice: ")
    vert1y=float(entrada.replace(",","."))
    entrada=input("Coordenada X del tercer vértice: ")
    vert2x=float(entrada.replace(",","."))
    entrada=input("Coordenada Y del tercer vértice: ")
    vert2y=float(entrada.replace(",","."))
    coordx=np.array([vert0x,vert1x,vert2x])
    coordy=np.array([vert0y,vert1y,vert2y])
    return coordx, coordy
#Se eligen vértices azarosamente
def sortear_vertices():
    v=random.randint(0,2)
    vx=coordx[v]
    vy=coordy[v]
    return vx,vy
#Se construye el fractal
def fractales():
    p0x=2.0 #más adelante se puede elegir el punto de inicio de las iteraciones
    p0y=2.0
    for i in range(iteraciones):
        vx,vy=sortear_vertices()
        x=(p0x+vx)/2;y=(p0y+vy)/2
        fx.append(x)
        fy.append(y)
        p0x=x;p0y=y
    return fx,fy 
#---------------------Código principal---------------------
#establece la cantidad de iteraciones,
#más adelante las podría ingresar el usuario
#se recomienda que sea multiplos de 10,
#preferentemente multiplos de 100
iteraciones=10000
coordx, coordy=ingresa_vertices_triang()
fx=[]
fy=[]
fractales()
plt.ion() # Prende la animación
ver_pasos(fx,fy)
plt.ioff() # Apaga la animación
plt.show() # Deja la ventana abierta al final

