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
#Entrada en la que el usuario va a ingresar el rol que tiene para así saber qué opciones mostrarle
boolUsuario = True
TipoUsuario = ""
while boolUsuario == True: #Se le va a preguntar el tipo de Rol hasta que ingrese un valor válido
    RolUsuario = int(input("¿Cuál es su rol dentro de CampusLands?\n 1. Camper\n 2. Trainer\n 3. Coordinador\n"))
   
    if RolUsuario == 1: #Dependiendo de la elección numerica, esta va a tomar un valor de texto
        TipoUsuario = "Camper"
        boolUsuario = False

    elif RolUsuario == 2: 
        TipoUsuario = "Trainer"
        boolUsuario = False

    elif RolUsuario == 3:
        TipoUsuario = "Coordinador"
        boolUsuario = False

    else:
        print("Este no es un número válido")
        input("Presione ENTER para continuar")
        system("cls")

print("Hola", TipoUsuario)
print("")
#El ROL de "Coordinador" Debe tener la opción de registrar la nota de los campers para cambiar el estado de "Aprobado" (Prom_PT_PP>=60 = Aprobado)

if RolUsuario == 1:
    print("---CAMPER---")
    print("")
    print(""" 
MENÚ DEL CAMPER
1. Ver notas
2. Ver Ruta de Estudio.
3. Ver Horario y salon de clases.
4. Ver módulo en el que está registrado
5. Salir.
          """)


elif RolUsuario == 2:
    print("---TRAINER---")
    print("")
    print(""" 
MENÚ DEL TRAINER
1. Ver Ruta de Estudio.
2. Ver Horario.
3. Ver salones.
4. Ver Modulos.
5.Salir.
          """)

elif RolUsuario == 3:
    boolCoordinador = True
    while boolCoordinador == True:
        print("---COORDINADOR---")
        print("")
        print(""" 
    MENÚ DEL TRAINER
    1. Registrar nuevo Camper.
    2. Registrar nota de los Campers que se han registrado.
    3. Ver Docentes dentro de Campus.
    4. Ver Grupos y la Ruta de Estudio que llevan.
    5. Salir.
            """)
        eleccionCoordinador = int(input("¿Qué desea hacer?: "))
        #if eleccionCoordinador == 1:
         #   print("---REGISTRAR CAMPER A LA PLATAFORMA---")
          #  GeneralData = abrirArchivo()
           # GeneralData[0]["EstudiantesGeneral"].append ({
            #        "Identificacion": 1,
             #       "Nombres": str(input("Ingrese los Nombres del Camper: ")),
              #      "Apellidos": str(input("Ingrese los apellidos del Camper: ")),
               #     "Direccion": str(input("Ingrese la dirección del Camper: ")),
                #    "Acudiente": str(input("Ingrese el nomnbre de el/la acudiente del Camper: ")),
                 #   "Celular": input("Ingrese el número de celular del Camper: "),
                  #  "Fijo": input("Ingrese el telefono fijo del Camper: "),
                   # "Trainer": str(input("Ingrese el nombre del Trainer")),
                    #"Ruta": str(input("Ingrese la ruta de estudio del Camper: ")),
                    #"FechaInicio": input("Ingrese la fecha de Inicio del Camper: "),
                    #"FechaFinal": input("Ingrese la fecha de finalización del proceso del Camper: "),
                    #"Rendimiento": input("Rendimiento: "),
                    #"Riesgo": input("Riesgo"),
                    #"Estado": input("Estado: "),
                    #"Notas": {
                    #input("Notas")
                    #}
            #})
            #guardarArchivo(GeneralData)
            #print("Camper Registrado!")
            #print("")
            #input("Presione ENTER para continuar")
            #system("cls")
            #boolCoordinador = False
    
#Desarrollado por Brayan Maldonado Y Maria Lizarazo - Campers