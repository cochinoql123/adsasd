def llenarmatriz(piso,tipo):
    p=1
    for i in range(10):
            for j in range(4):
                tipo[i,j]=p
                piso[i,j]=p
                p+=1

def mostrarDisponibles(piso,tipo):
    os.system('cls')
    for i in range(10):
        print('\n')
        for j in range(4):
            if(j==1 or j==5):
                print('\t',piso[i,j], end="  ")
            else:
                print('\t',tipo[i,j], end="  ")
    print('\n\n')      
def validaOp():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp                 
def salir():
    print("Matias Cheuque 11/07/2023 ")   

while(True):
                        try:
                            rut=int(input("Rut debe tener 7 digitos minimo "))
                            if(rut<999999):
                                print("Error, debe tener 7 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                        if(len(ruts)>0): 
                            sw=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya existe y no se puede agregar el comprador")
                        else:
                            ruts.append(rut)
                            break
                                else:
                                ruts.append(rut)
                                break
def listado(r):
    r.sort()
    print("Listado de compradores ordenados de menor a mayor ")
    print("\t",r)                            

def tipo():
    os.system("cls")
    tip=""
    while(len(tip)<=0):
        print("A ")
        print("B ")
        print("C ")
        print("D ")
        print("")
        tip=input("   Elija tipo de departamento:").lower()
        if(tip!="A" and tip!="B" and tip!="C" and tip!="D"):
            print("Debe ingresar una opcion correcta")
            tip=""
    return tip 
def validaPiso():
    piso=0
    while(True):
        try:
            piso=int(input(" Ingrese número de piso entre 1 y 10: "))
            if(piso>=1 and piso<=10):
                break
            else:
                print("Error debe ingresar un piso entre 1 y 10")
        except ValueError:
            print("Debe ser un número entero")
    return piso 
def disponible(piso,tipo):
    for i in range(10):
        for j in range(4):
            if(piso==tipo[i,j]):
                return True    