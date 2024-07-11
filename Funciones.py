import os
import csv
import random 
from statistics import geometric_mean
def ValidarOP ():
    while (True):
        try:
            op=int(input("Ingrese unas de las opciones: "))
            if (op>=1 and op<=5):
                break
            else:
                print("Ingrese un valor entre los parametros")
        except ValueError:
            print("Ingrese un número entero")
    return op

def sueldo ():
    sueldo= random.randint(300000, 2500000)
    return sueldo
def OP1 (lista):
    NuevaLista=[]
    for i in lista:
        suel=sueldo()
        NuevaLista.append ((i,suel))
    print ("Listo")
    os.system ("pause")
    return NuevaLista

def OP2 (lista):
    os.system ("cls")
    MenoresDe800K= []
    cont1=0
    Entre800kY2M= []
    cont2=0
    Supeiores2M= []
    cont3=0
    total=0
    for i in lista:
        print (i)
        if len(i) >= 1:  
                valor = int(i[1])
                if valor < 800000:
                    MenoresDe800K.append((i[0],valor))
                    cont1+=1
                elif 800000 <= valor <= 2000000:
                    Entre800kY2M.append((i[0],valor))
                    cont2+=1
                else:
                    Supeiores2M.append((i[0],valor))
                    cont3+=1
                total+=valor
        else:
                print(f"Error: La lista {i} no tiene suficientes elementos.")
                os.system ("cls")
    os.system ("cls")            
    print (F"Menores a $800.000 TOTAL: {cont1}")
    print ("Nombre del empleado","Sueldo",sep= "       ")
    for i in MenoresDe800K:
        print (f"{i[0]}",f"${i[1]}", sep= "              ")
    print ()
    print ("Entre $800.000 y $2.000.000")
    print (f"TOTAL: {cont2}")
    print ("Nombre del empleado","Sueldo", sep= "       ")
    for i in Entre800kY2M:
        print (f"{i[0]}",f"${i[1]}", sep= "                ")
    print ()
    print ("Superiores a $2.000.000")
    print (f"TOTAL: {cont3}")
    print ("Nombre del empleado","Sueldo",sep= "        ")
    for i in Supeiores2M:
        print (f"{i[0]}",f"${i[1]}", sep= "                ")
    print ()
    print (F"TOTAL SUELDOS: ${total}")
    os.system ("pause")

def op3(lista):
    os.system ("cls")
    total = 0
    mayor = int(lista[0][1])
    menor = int(lista[0][1])  
    for i in lista:
        if int(i[1]) > mayor:
            mayor = int(i[1])
        elif int(i[1]) < menor:
            menor = int(i[1])
        total += int(i[1])
    print("Mayor es:", mayor)
    print("Menor es:", menor)
    print("Promedio es:", total / len(lista))
    listasueldo=[]
    for i in lista:
        listasueldo.append(i[1])
    print ("Media geométrica: ",  geometric_mean(listasueldo))
    os.system ("pause")
    
def OP4 (lista):
    os.system ("cls")
    nuevalista=[]
    for i in lista:
        valor=int(i[1])
        Salud=round(valor*0.07)
        DescuentoAFP=round(valor*0.12)
        Liquido=round(valor-Salud-DescuentoAFP)
        nuevalista.append((i[0],i[1],Salud,DescuentoAFP,Liquido))
    with open ("Reportedesueldos.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(nuevalista)
    print ("Reporte creado")
    with open("Reportedesueldos.csv", "r") as f:
        lector = csv.reader(f)
        print ("Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido",sep= "    ")
        for fila in lector:
            print(f"{fila[0]}        ${fila[1]}         ${fila[2]}           ${fila[3]}            ${fila[4]}")
    titulo= ("Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido")
    with open ("Reportedesueldos.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(titulo)
        writer.writerows(nuevalista)
    os.system ("pause")