import numpy as np 
import os
import funcionesCasa as ca 

matriz=np.empty((10,4), type(int))
otra=np.empty((4,3), type(int))
ruts=[]
costo=0
piso=0

while(True):
    print("1. Comprar departamento ")
    print("2. Mostrar departamentos disponibles ")
    print("3. Ver listado de compradores ")
    print("4. Mostrar ganancias totales ")
    print("5. Salir                        ")
    opcion=input("Seleccione una opción: ")
    op=ca.validaOp()
    if(op==1):
        ca.mostrarDisponibles(piso)
        os.system("pause")
    if (op==2):
        ca.mostrarDisponibles(piso,tipo)
        os.system('pause')
    if(op==3):
        ca.listado(ruts)
        os.system("pause")
    if(op==4):
        suma=0
        suma=ca.totalVenta(otra)
        if(suma==0):
            print("\t No se han vendido dptos aún")
        else:
            print("\t El total vendido hasta ahora es de : $", suma)
        os.system("pause")
    if (op==5):
        print("Matias Cheuque 11/07/2023 ")
        os.system('pause')    

