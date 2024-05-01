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
GeneralData = abrirArchivo()
GrupoT1 = []
GrupoT2 = []
GrupoT3 = []
#Se guardan los estudiantes en el salon que correspondan
for i in range (len(GeneralData[3]["Estudiantes"])):
    if GeneralData[3]["Estudiantes"][i]["Grupo"] == "T1":
        GrupoT1.append(GeneralData[3]["Estudiantes"])

    elif GeneralData[3]["Estudiantes"][i]["Grupo"] == "T2":
        GrupoT2.append(GeneralData[3]["Estudiantes"])
    
    elif GeneralData[3]["Estudiantes"][i]["Grupo"] == "T3":
        GrupoT3.append(GeneralData[3]["Estudiantes"])

GeneralData[6]["Grupos"][0]["GrupoT1"]= GrupoT1
GeneralData[6]["Grupos"][1]["GrupoT2"]= GrupoT2
GeneralData[6]["Grupos"][2]["GrupoT3"]= GrupoT3
guardarArchivo(GeneralData)



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
    boolTrainer = True
    while boolTrainer == True: 
        print("---TRAINER---")
        print("")
        print(""" 
MENÚ DEL TRAINER
1. Ver Grupos.
5.Salir.
          """)
        eleccionTrainer = int(input("¿Qué desea hacer: ?"))
        system("cls")

        if eleccionTrainer == 1:
            print ("GRUPOS")
            GeneralData = abrirArchivo()
            for i in range (len(GeneralData[6]["Grupos"][0])):
                print("Nombres:",i["Nombres"])
                print("Apellidos:",i["Apellidos"]) ####################################
                print("Grupo:",i["Grupo"])         #################################
                print("Salon:",i["Salon"])         ###################################
                print("Trainer:",i["Trainer"])
                print("Horario:",i["Horario"])
               

elif RolUsuario == 3:
    boolCoordinador = True
    while boolCoordinador == True:
        print("---COORDINADOR---")
        print("")
        print(""" 
    MENÚ DEL TRAINER
    1. Registrar nuevo Camper.
    2. Ingresar Nota del Camper.
    3. Añadir Ruta de Estudio a los Campers, asignación de trainer, salon y definicion de horario.
            """)
        eleccionCoordinador = int(input("¿Qué desea hacer?: "))
        system("cls")

        #=====Crear Nuevo Camper=====
        if eleccionCoordinador == 1:
            print("---REGISTRAR CAMPER A INSCRITOS---")
            GeneralData = abrirArchivo()
            GeneralData[2]["Estudiantes"].append ({
                    "Identificador" : len(GeneralData[2]["Estudiantes"])+1,
                    "Estado" : "Inscrito",
                    "Documento": (input("Ingrese su documento: ")),
                    "Nombres": (input("Ingrese los Nombres del Camper: ")),
                    "Apellidos": (input("Ingrese los apellidos del Camper: ")),
                    "Direccion": (input("Ingrese la dirección del Camper: ")),
                    "Acudiente": (input("Ingrese el nomnbre de el/la acudiente del Camper: ")),
                    "Celular": input("Ingrese el número de celular del Camper: "),
                    "Fijo": input("Ingrese el telefono fijo del Camper: "),
                    "NotaPrueba" : 0
                    })
            guardarArchivo(GeneralData)
            print("Camper Registrado!")
            print("")
            input("Presione ENTER para continuar")
            system("cls")
            break
    

        #INGRESAR NOTA DE LA PRUEBA INICIAL
        if eleccionCoordinador == 2: 
            GeneralData = abrirArchivo()
            print("---INGRESAR LA NOTA DE LA PRUEBA---")
            for i in GeneralData[2]["Estudiantes"]:
                print("Idetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"]) 
            CamperParaNota = int(input("Ingrese el Camper que desea Agregar: "))
            NotaCamper = int(input("Ingrese la nota: "))
            GeneralData[2]["Estudiantes"][CamperParaNota-1]["NotaPrueba"] = NotaCamper
            guardarArchivo(GeneralData)
            print("Nota Agregada!")
            input("Presione ENTER para continuar")
            system("cls")

            GeneralData = abrirArchivo()
            for i in range (len(GeneralData[2]["Estudiantes"])):
                if GeneralData[2]["Estudiantes"][i]["NotaPrueba"]>=60:
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Aprobado"

                elif GeneralData[2]["Estudiantes"][i]["NotaPrueba"]<=59:
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Reprobado"
            guardarArchivo(GeneralData)                  

        #===DEFINIR RUTA DEL CAMPER, ASIGNACION DE TRAINER, SALON Y DEFINICION DE HORARIO===        
        if eleccionCoordinador == 3:
            print("----REGISTRAR RUTA DE ESTUDIO, ASIGNACION DE TRAINER, SALON Y DEFINICION DE HORARIO----")
            GeneralData = abrirArchivo()
            for i in GeneralData[3]["Estudiantes"]:
                print("Idetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])
            #DEFINIR RUTA DE ESTUDIO
            Camper = int(input("\nIngrese el identificador del Camper que desea escoger: "))
            print("\nPara la ruta de estudio elige entre:\n NoteCore \n Java \n NoteJS") 
            RutaElegida = str(input("Ingrese el nombre de la Ruta que le desea definir: "))
            GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = RutaElegida
            guardarArchivo(GeneralData)
            #ASIGNAR TRAINER
            print("\n Los Trainers disponibles son:\n Pedro Perez \n Jholver Garcia \n Stiven Carvajal")
            TrainerConfirmado = str(input("Ingrese el nombre del Trainer que desea asignar: "))
            GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = TrainerConfirmado
            guardarArchivo(GeneralData)
            #ASIGNAR SALON
            print("\nLos salones a usar son:\n Sputnik\n Apolo\n Artemis")
            SalonAsignado = str(input("Ingrese el nombre del salon que le desea asignar: "))
            GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = SalonAsignado
            guardarArchivo(GeneralData)
            #ASIGNAR HORARIO
            print("\nLos horarios son:\n 6am-10am\n 10am-2pm\n 2pm-6pm\n 6pm-10pm")
            HorarioAsignado = str(input("Ingrese el horario a asignar: "))
            GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = HorarioAsignado
            guardarArchivo(GeneralData)

            print("Cambios Realizados!")
            input("Presione ENTER para continuar")
            system("cls")

      
#Desarrollado por Brayan Maldonado Y Maria Lizarazo - Campers