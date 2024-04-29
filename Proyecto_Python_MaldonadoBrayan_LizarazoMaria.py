#Proyecto para el filtro de Python

import json
from os import system

def abrirArchivo(): #Función que va a servir para abrir el archivo
    miJSON=[]
    with open('mainIndex.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)
    return miJSON

def guardarArchivo(miData): #Función que va a servir para guardar los datos que se realicen al archivo
    with open("mainIndex.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

#INICIO DEL PROGRAMA
sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=4:  # hacemos un while para hacer un bucle a nuestras cuatro opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ------BIENVENIDO AL PROGRAMA PARA EL FILTRO DE PYTHON DE BRAYAN Y MARIA------
    1. ¿Eres un camper?.                                            
    2. ¿Eres trainer?.
    3. Soy el Coordinador :D
    4. ¿Desea terminar el programa?.
    ------------------------------------------------------------------------------
    """) #Creo un menú
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.

    if sel == 1:
        
        
        input("Para volver al menú principal, presione enter.") # este input nos ayuda con el limpiar pantalla

    if sel == 2:
        GeneralData = abrirArchivo()
        contador = 0
        for i in GeneralData[0]["EstudiantesGeneral"]:
            contador += 1
            print("ESTUDIANTE #",contador)
            print("# de identificación:",i["Identificación"])
            print ("Nombres:",i["Nombres"])
            print ("Apellidos:",i["Apellidos"])
            print ("Dirección:",i["Dirección"])
            print ("Acudiente:",i["Acudiente"])
            print ("Celular:",i["Celular"])
            print ("Fijo:",i["Fijo"])
            print("Trainer:",i["Trainer"])
            print("Ruta:",i["Ruta"])
            print("Fechad de inicio:",i["FechaInicio"])
            print("Fecha final:",i["FechaFinal"])
            print("Rendimiento:",i["Rendimiento"])
            print("Riesgo:",i["Riesgo"])
            print("Estado:",i["Estado"])
            print("")        
    
        input("Para volver al menú principal, presione enter.") # este input nos ayuda con el limpiar pantalla

    if sel == 3:
        
    
        input("Para volver al menú principal, presione enter.") # este input nos ayuda con el limpiar pantalla

else:
    print("El programa ha terminado.")    
    input("Presione enter para finalizar.")


#Entrada en la que el usuario va a ingresar el rol que tiene para así saber qué opciones mostrarle
RolUsuario = str(input("¿Cuál es su rol dentro de CampusLands?\n 1. Camper\n 2. Trainer\n 3. Coordinador\n"))
print("Hola", RolUsuario)
print("")
#El ROL de "Coordinador" Debe tener la opción de registrar la nota de los campers para cambiar el estado de "Aprobado" (Prom_PT_PP>=60 = Aprobado)



