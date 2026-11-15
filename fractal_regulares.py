#Bibliotecas que se importan
import matplotlib.pyplot as plt
import math
import random
# Funciones y procedimientos
#Esta función realiza reresentaciones de cada 10% de los puntos,
#con el objeto de comprender mejor como se va formando elfractal
def ver_pasos(fx,fy):
    for corte in range(iteraciones//10, int(iteraciones*1.1), iteraciones//10):
        plt.scatter(fx[:corte], fy[:corte], s=5, color="purple") 
        plt.pause(0.5) # Muestra los puntos de a 100 y frena medio segundo
#Determina los n vértices del polígono y los devuelve en vertx[] y verty[]
def nvertices(lados):
    for i in range(lados):
        vertx.append(x0 + modulo * math.cos(i*(2*valor_pi)/lados))
        verty.append(y0 + modulo * math.sin(i*(2*valor_pi)/lados))
    return vertx,verty
#Se eligen vértices azarosamente
def sortear_vertices():
    v=random.randint(0,lados-1)
    vx=vertx[v]
    vy=verty[v]
    return vx,vy
def fractales(fx,fy):
    p0x=2.0 #más adelante se puede elegir el punto de inicio de las iteraciones
    p0y=2.0
    for _ in range(iteraciones):
        vx,vy=sortear_vertices()
        x=(p0x+vx)/2;y=(p0y+vy)/2
        fx.append(x)
        fy.append(y)
        p0x=x;p0y=y
    return fx,fy
#----------------------------------------------------------------
#Inicialización de variables y constantes
#establece la cantidad de iteraciones,
#más adelante las podría ingresar el usuario
#se recomienda que sea multiplos de 10,
#preferentemente multiplos de 100
modulo = 2
valor_pi = 3.141592653589793 #math.pi también se podría haber utilizado
lados=5
iteraciones=10000
x0, y0 = 3, -1 # Punto cartesiano origen del poligono
vertx=[]
verty=[]
fx=[]
fy=[]
vertx,verty =nvertices(lados)
fractales(fx,fy)
plt.ion() # Prende la animación
ver_pasos(fx,fy)
plt.ioff() # Apaga la animación
print("Finalizado")# Tambien se puede usar plt.text(0.5, 0.5, "Finalizado", fontsize=20, color="red")
plt.show() # Deja la ventana abierta al final
