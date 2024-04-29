#Proyecto para el filtro de Python

import json

def abrirArchivo(): #Función que va a servir para abrir el archivo
    miJSON=[]
    with open('mainIndex.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)
    return miJSON

def guardarArchivo(miData): #Función que va a servir para guardar los datos que se realicen al archivo
    with open("mainIndex.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

#INICIO DEL PROGRAMA
print("BIENVENIDO AL PROGRAMA PARA EL FILTRO DE PYTHON DE BRAYAN Y MARIA")

#Entrada en la que el usuario va a ingresar el rol que tiene para así saber qué opciones mostrarle
RolUsuario = str(input("¿Cuál es su rol dentro de CampusLands?\n 1. Camper\n 2. Trainer\n 3. Coordinador\n"))
print("Hola", RolUsuario)
print("")
#El ROL de "Coordinador" Debe tener la opción de registrar la nota de los campers para cambiar el estado de "Aprobado" (Prom_PT_PP>=60 = Aprobado)


