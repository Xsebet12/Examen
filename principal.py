import os
os.system ("cls")
import Funciones as F
u=0
lista=  ["Juan Pérez", "María García" , "Carlos López" , "Ana Martínez" , "Pedro Rodríguez" , "Laura Hernández" , "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz" , "Elena Fernández"]
while (True):
    os.system ("cls")
    print ("MENU")
    print ("1. Asignar sueldos aleatorios")
    print ("2. Clasificar sueldos")
    print ("3. Ver estadistica")
    print ("4. Reporte de sueldos")
    print ("5. Salir del programa")
    op= F.ValidarOP ()
    if op==1:
            Nlista=F.OP1 (lista)
            u=1
    if op==2:
        if u==1:
            F.OP2 (Nlista)
        else:
            print ("No se han asignado sueldos")
            os.system ("pause")
    if op ==3:
        if u==1:
            F.op3 (Nlista)
        else:
            print ("No se han asignado sueldos")
            os.system ("pause")
    if op==4:
        if u == 1:    
            F.OP4 (Nlista)
        else:
            print ("No se han asignado sueldos")
            os.system ("pause")
    if op==5:
        print("Finalizando programa…")
        print("Desarrollado por Sebastián Cornejo")
        print("RUT 21.813.827-6")
        break

