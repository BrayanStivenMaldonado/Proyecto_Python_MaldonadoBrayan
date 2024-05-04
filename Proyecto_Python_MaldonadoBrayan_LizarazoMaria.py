#Proyecto para el filtro de Python

#Importación de librerias
import json
from os import system

#Definición de funciones
def abrirArchivo(): #Función que va a servir para abrir el archivo
    miJSON=[]
    with open('mainIndex.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)
    return miJSON

def guardarArchivo(miData): #Función que va a servir para guardar los datos que se realicen al archivo
    with open("mainIndex.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

#================================================================ INICIO DEL PROGRAMA =======================================================================

#Entrada en la que el usuario va a ingresar el rol que tiene para así saber qué opciones mostrarle
boolUsuario = True
TipoUsuario = ""

while boolUsuario == True: #Se le va a preguntar el tipo de Rol hasta que ingrese un valor válido

    boolTryCatch = True
    while boolTryCatch == True: 
        try: 
            RolUsuario = int(input("¿Cuál es su rol dentro de CampusLands?\n 1. Camper\n 2. Trainer\n 3. Coordinador\n"))
            break
        except ValueError:
            input("Debe ingresar un número entero")
            system("cls")
    
   
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

#=================================== MODULO DEL CAMPER ===========================================================
if RolUsuario == 1:
    system("cls")
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
#=================================== MODULO DEL TRAINER ===========================================================
elif RolUsuario == 2:
    system("cls")
    boolTrainer = True
    while boolTrainer == True: 

        boolTryCatch = True
        while boolTryCatch == True:
            try: 
                print("---TRAINER---")
                print("")
                print(""" 
MENÚ DEL TRAINER
1. Ver Grupos.
5.Salir.
            """)
                eleccionTrainer = int(input("¿Qué desea hacer: ?"))
                boolTryCatch = False
            except ValueError:
                input("Debe ingresar un valor entero, presione ENTER para continuar")
                system("cls")

        
        system("cls")

        #=========================== VER GRUPOS Y LOS Estudiantes QUE HAY DENTRO ==================================
        if eleccionTrainer == 1:
            GeneralData = abrirArchivo()
            GrupoT1 = {}
            GrupoT2 = {}
            GrupoT3 = {}
            #Se guardan los Estudiantes en el salon que correspondan
            for i in range (len(GeneralData[3]["Estudiantes"])):
                if GeneralData[3]["Estudiantes"][i]["Grupo"] == "T1":
                    GrupoT1 = (GeneralData[3]["Estudiantes"])

                elif GeneralData[3]["Estudiantes"][i]["Grupo"] == "T2":
                    GrupoT2 = (GeneralData[3]["Estudiantes"])
                
                elif GeneralData[3]["Estudiantes"][i]["Grupo"] == "T3":
                    GrupoT3 = (GeneralData[3]["Estudiantes"])
            GeneralData[6]["Grupos"][0]["GrupoT1"]= GrupoT1
            GeneralData[6]["Grupos"][1]["GrupoT2"]= GrupoT2
            GeneralData[6]["Grupos"][2]["GrupoT3"]= GrupoT3
            guardarArchivo(GeneralData)

            print ("GRUPOS"),print()
            GeneralData = abrirArchivo() #Mostrar los grupos
            print("GRUPO T1"),print("")
            contador = 0
            for i in GeneralData[6]["Grupos"][0]["GrupoT1"]:
                contador+=1
                print("Estudiante #",contador)
                print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Grupo:",i["Grupo"]),print("Salon:",i["Salon"]),print("Trainer:",i["Trainer"])
                print("================")
            
            print("GRUPO T2"),print("")
            contador = 0
            for i in GeneralData[6]["Grupos"][1]["GrupoT2"]:
                contador+=1
                print("Estudiante #",contador)
                print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Grupo:",i["Grupo"]),print("Salon:",i["Salon"]),print("Trainer:",i["Trainer"])
                print("================")

            print("GRUPO T3"),print("")
            contador = 0
            for i in GeneralData[6]["Grupos"][2]["GrupoT3"]:
                contador+=1
                print("Estudiante #",contador)
                print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Grupo:",i["Grupo"]),print("Salon:",i["Salon"]),print("Trainer:",i["Trainer"])
                print("================")

        elif eleccionTrainer == 5:
            print("Saliendo del módulo del trainer")
            input("Presione ENTER para continuar")
            boolTrainer = False

#=================================== MODULO DEL COORDINADOR ===========================================================
elif RolUsuario == 3:
    system("cls")
    boolCoordinador = True
    while boolCoordinador == True:
        boolTryCatch = True
        while boolTryCatch == True:
            try: 
                print("---COORDINADOR---")
                print("")
                print(""" 
    MENÚ DEL COORDINADOR
    1. Registrar nuevo Camper.
    2. Ingresar Nota de la prueba inicial al Camper.
    3. Crear Ruta.
    4. Añadir Ruta de Estudio a los Campers, asignación de trainer, salon y definicion de horario.
    5. Añadir Notas del Módulo a los Campers.
    6. Salir del módulo de coordinador.
            """)
                eleccionCoordinador = int(input("¿Qué desea hacer?: "))
                break
            except ValueError:
                input("Debe ingresar un valor entero, presione ENTER para continuar")
                system("cls")

        
        system("cls")

        #=====Crear Nuevo Camper=====
        if eleccionCoordinador == 1:
            print("---REGISTRAR CAMPER A INSCRITOS---")

            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    DocumentoNuevo = int(input("Ingrese su documento: "))
                    break
                except:
                    input("En este dato, debe ingresar números, presione ENTER para continuar")
                    system("cls")
            
            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    NombreNuevo = str(input("Ingrese los Nombres del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar letras, presione ENTER para continuar")
                    system("cls")
            
            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    ApellidoNuevo = str(input("Ingrese los apellidos del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar letras, presione ENTER para continuar")
                    system("cls")
                
            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    DireccionNueva = str(input("Ingrese la dirección del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar letras, presione ENTER para continuar")
                    system("cls")

            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    AcudienteNuevo = str(input("Ingrese el nomnbre de el/la acudiente del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar letras, presione ENTER para continuar")
                    system("cls")

            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    CelularNuevo = int(input("Ingrese el número de celular del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar números, presione ENTER para continuar")
                    system("cls")

            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    FijoNuevo = int(input("Ingrese el telefono fijo del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar números, presione ENTER para continuar")
                    system("cls")
         
            GeneralData = abrirArchivo()
            GeneralData[2]["Estudiantes"].append ({
                    "Identificador" : len(GeneralData[2]["Estudiantes"])+1,
                    "Estado" : "Inscrito",
                    "Ruta" : "",
                    "Documento": DocumentoNuevo,
                    "Nombres": NombreNuevo,
                    "Apellidos": ApellidoNuevo,
                    "Direccion": DireccionNueva,
                    "Acudiente": AcudienteNuevo,
                    "Celular": CelularNuevo,
                    "Fijo": FijoNuevo,
                    "NotaPrueba" : 0
                    })
            guardarArchivo(GeneralData)
            print("Camper Registrado!")
            print("")
            input("Presione ENTER para continuar")
            system("cls")
            break
    
        #INGRESAR NOTA DE LA PRUEBA INICIAL
        elif eleccionCoordinador == 2: 
            print("---INGRESAR LA NOTA DE LA PRUEBA INICIAL---")
            
            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    contador = 0 
                    GeneralData = abrirArchivo()
                    for i in GeneralData[2]["Estudiantes"]:
                        contador+=1
                        print("==========================")
                        print("Idetinficador:",contador)
                        print("Documento:",i["Documento"])
                        print("Nombres:",i["Nombres"])
                        print("Apellidos:",i["Apellidos"]) 
                    print("==========================")
                    CamperParaNota = int(input("Ingrese el identificador del Camper: "))
                    break
                except:
                    input("En este dato, debe ingresar un número, presione ENTER para continuar")
                    system("cls")

            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    PruebaTeorica = int(input("Ingrese la nota de la prueba teorica: "))                    
                    break
                except:
                    input("En este dato, debe ingresar un número, presione ENTER para continuar")
                    system("cls")

            boolTryCatch = True
            while boolTryCatch == True: 
                try:
                    PruebaPractica = int(input("Ingrese la nota de la prueba practica: "))                    
                    break
                except:
                    input("En este dato, debe ingresar números, presione ENTER para continuar")
                    system("cls")

            NotaCamper = (PruebaPractica+PruebaTeorica)/2 #La nota de la prueba general del camper es el prom de las dos que realizó
            GeneralData[2]["Estudiantes"][CamperParaNota-1]["NotaPrueba"] = NotaCamper
            guardarArchivo(GeneralData)
            print("Nota Agregada!")
            input("Presione ENTER para continuar")
            system("cls")

            AprobadosInicial = {}
            ReprobadosInicial = {}          
                
            GeneralData = abrirArchivo()
            for i in range (0,(len(GeneralData[2]["Estudiantes"]))):
                if GeneralData[2]["Estudiantes"][i]["NotaPrueba"]>=60:
                    AprobadosInicial = GeneralData[2]["Estudiantes"][i] #Dependiendo de la nota que se le dé al camper 
                    GeneralData[3]["Estudiantes"].append(AprobadosInicial) #Se va a añadir a la lista de "Cursando"
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Aprobado" # o a la de "Expulsados"
                    del GeneralData[2]["Estudiantes"][i]
                    guardarArchivo(GeneralData)
                    break

            GeneralData = abrirArchivo()
            for i in range (0,(len(GeneralData[2]["Estudiantes"]))):
                if GeneralData[2]["Estudiantes"][i]["NotaPrueba"]<=59 and GeneralData[2]["Estudiantes"][i]["NotaPrueba"]>0: #Primero se Guardan en un diccionario y posteriormente
                    ReprobadosInicial = GeneralData[2]["Estudiantes"][i] #se agregan al json
                    GeneralData[4]["Estudiantes"].append(ReprobadosInicial)
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Reprobado"
                    del GeneralData[2]["Estudiantes"][i]
                    guardarArchivo(GeneralData)
                    break
            else:
                print("")

            guardarArchivo(GeneralData)    
            print(AprobadosInicial)  
            print(ReprobadosInicial)          

        #===CREAR RUTA===        
        elif eleccionCoordinador == 3:
            print("----CREAR RUTA----")

            GeneralData = abrirArchivo()
            if len(GeneralData[8]["NombresRutas"])>= 8:
                print(""),print("LO SIENTO, YA SE HA ALCANZADO EL MAXIMO DE RUTAS")
            else:

                NombreRutaNueva = str(input("Ingrese el nombre de la Ruta que va a Crear: "))
                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        boolParaPFNueva = True
                        while boolParaPFNueva == True:
                            ProgramacionFormalNueva = int(input("\n1. Java\n2. JavaScript\n3. C#\n ¿Que materia desea agregar al módulo programación formal?: "))
                            if ProgramacionFormalNueva == 1:
                                ProgramacionFormalNueva = "Java"
                                boolParaPFNueva = False
                            elif ProgramacionFormalNueva == 2:
                                ProgramacionFormalNueva = "JavaScript"
                                boolParaPFNueva = False
                            elif ProgramacionFormalNueva == 3:
                                ProgramacionFormalNueva = "C#"
                                boolParaPFNueva = False
                            else:
                                print("Esta no es una opción válida")
                        break
                    except ValueError:
                        input("Debe ingresar un valor númerico, presione ENTER para continuar")
                        system("cls")
                
                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        boolParaBDNueva = True
                        while boolParaBDNueva == True:
                            BaseDatosNuevaPrincipal = int(input("\n1.Mysql \n2. MongoDb \n3. Progresql\n ¿Qué materia desea agregar como principal al módulo Base de Datos?: "))
                            if BaseDatosNuevaPrincipal == 1:
                                BaseDatosNuevaPrincipal = "Mysql"
                                boolParaBDNueva = False
                            elif BaseDatosNuevaPrincipal == 2:
                                BaseDatosNuevaPrincipal = "MongoDb"
                                boolParaBDNueva = False
                            elif BaseDatosNuevaPrincipal == 3:
                                BaseDatosNuevaPrincipal = "Progresql"
                                boolParaBDNueva = False
                            else:
                                print("Esta no es una opción válida")
                        break
                    except ValueError:
                        input("Debe ingresar un valor numérico, presione ENTER para continuar")
                        system("cls")
                    
                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        boolParaBDNueva = True
                        while boolParaBDNueva == True:
                            BaseDatosNuevaAlternativa = int(input("\n1.Mysql \n2. MongoDb \n3. Progresql \n ¿Qué materia desea agregar como Secundaria al módulo Base de Datos?: "))
                            if BaseDatosNuevaAlternativa == 1:
                                BaseDatosNuevaAlternativa = "Mysql"
                                boolParaBDNueva = False
                            elif BaseDatosNuevaAlternativa == 2:
                                BaseDatosNuevaAlternativa = "MongoDb"
                                boolParaBDNueva = False
                            elif BaseDatosNuevaAlternativa == 3:
                                BaseDatosNuevaAlternativa = "Progresql"
                                boolParaBDNueva = False
                            else:
                                print("Esta no es una opción válida")
                        break
                    except ValueError:
                        input("Debe ingresar un valor numérico, presione ENTER para continuar")
                        system("cls")

                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        boolParaBackEndNueva = True
                        while boolParaBackEndNueva == True:
                            BackendNuevo = int(input("\n1.NetCore \n2. SpringBoot \n3. Node \n4. Express \n ¿Qué materia desea agregar al módulo BackEnd?: "))
                            if BackendNuevo == 1:
                                BackendNuevo = "NetCore"
                                boolParaBackEndNueva = False
                            elif BackendNuevo == 2:
                                BackendNuevo = "SpringBoot"
                                boolParaBackEndNueva = False
                            elif BackendNuevo == 3:
                                BackendNuevo = "Node"
                                boolParaBackEndNueva = False
                            elif BackendNuevo == 4:
                                BackendNuevo = "Express"
                                boolParaBackEndNueva = False
                            else:
                                print("Esta no es una opción válida")
                        break
                    except ValueError:
                        input("Debe ingresar un valor numérico, presione ENTER para continuar")
                        system("cls")

                NuevaRuta = {
                    NombreRutaNueva : [
                        {
                            "FundamentosProgramacion" : ["Pseint","Python", "Introduccion a la algoritmia"]
                        },
                        {
                            "ProgramacionWeb" : ["HTML", "CSS", "BootStrap"]
                        },
                        {
                            "ProgramacionFormal" : [ProgramacionFormalNueva]
                        },
                        {
                            "BaseDatos" : [BaseDatosNuevaPrincipal,BaseDatosNuevaAlternativa]
                        },
                        {
                            "Backend" : [BackendNuevo]
                        }
                    ]
                }

            GeneralData = abrirArchivo()
            GeneralData[7]["Rutas"].append(NuevaRuta)
            GeneralData[8]["NombresRutas"].append(NombreRutaNueva) 
            guardarArchivo(GeneralData) 

            GeneralData = abrirArchivo()
            if len(GeneralData[8]["NombresRutas"]) == 4:
                GeneralData[0]["Trainers"][0]["Ruta"].append(NombreRutaNueva)
            if len(GeneralData[8]["NombresRutas"] ) == 5:
                GeneralData[0]["Trainers"][1]["Ruta"].append(NombreRutaNueva)
            if len(GeneralData[8]["NombresRutas"] )== 6:
                GeneralData[0]["Trainers"][2]["Ruta"].append(NombreRutaNueva)
            if len(GeneralData[8]["NombresRutas"]) == 7:
                GeneralData[0]["Trainers"][0]["Ruta"].append(NombreRutaNueva)
            guardarArchivo(GeneralData)

            input("Cambios guardados!, presione ENTER para continuar")
            system("cls")

        #===DEFINIR RUTA DEL CAMPER, ASIGNACION DE TRAINER, SALON Y DEFINICION DE HORARIO===        
        elif eleccionCoordinador == 4:
            print("----REGISTRAR RUTA DE ESTUDIO, ASIGNACION DE TRAINER, SALON Y DEFINICION DE HORARIO----")
            GeneralData = abrirArchivo()
            if len(GeneralData[3]["Estudiantes"]) == 0:
                print("")
                print("No hay ningun estudiante disponible para registrarle Ruta de Estudio")
                input("Presione ENTER para continuar")
                system("cls")
            else:
                boolTryCatch = True
                while boolTryCatch == True: 
                    try:
                        GeneralData = abrirArchivo()
                        contador = 0
                        for i in GeneralData[3]["Estudiantes"]:
                            contador+=1
                            print("=================")
                            print("Idetinficador:",contador)
                            print("Documento:",i["Documento"])
                            print("Nombres",i["Nombres"])
                            print("Apellidos",i["Apellidos"])
                        print("=================")
                        Camper = int(input("\nIngrese el identificador del Camper que desea escoger: "))                    
                        break
                    except:
                        input("En este dato, debe ingresar números, presione ENTER para continuar")
                        system("cls")

                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        GeneralData = abrirArchivo()
                        contador = 0
                        for i in GeneralData[8]["NombresRutas"]:
                            contador += 1
                            print("Ruta #",contador)
                            print(i)
                            print("====")
                        eleccionRuta = int(input("¿A qué ruta desea agregar al Camper?: "))
                        break
                    except ValueError:
                        input("Debe ingresar un valor númerico, presione ENTER para volver a intentar")
                        system("cls")     

                NombreRutaAgregada1 = ""
                if len (GeneralData[8]["NombresRutas"])==4:
                    GeneralData = abrirArchivo()
                    NombreRutaAgregada1 = GeneralData[8]["NombresRutas"][3]
                NombreRutaAgregada2 = ""
                if len(GeneralData[8]["NombresRutas"])==5:
                    GeneralData = abrirArchivo()
                    NombreRutaAgregada2 = GeneralData[8]["NombresRutas"][4]
                NombreRutaAgregada3 = ""
                if len(GeneralData[8]["NombresRutas"])==6:
                    GeneralData = abrirArchivo()
                    NombreRutaAgregada3 = GeneralData[8]["NombresRutas"][5]
                NombreRutaAgregada4 = ""
                if len(GeneralData[8]["NombresRutas"])==7:
                    GeneralData = abrirArchivo()
                    NombreRutaAgregada4 = GeneralData[8]["NombresRutas"][6]

                if eleccionRuta == 1:
                    eleccionRutaStr = "Java"
                elif eleccionRuta == 2:
                    eleccionRutaStr = "NetCore"
                elif eleccionRuta == 3:
                    eleccionRutaStr = "NodeJS"  
                elif eleccionRuta == 4:
                    eleccionRutaStr = NombreRutaAgregada1
                elif eleccionRuta == 5:
                    eleccionRutaStr = NombreRutaAgregada2
                elif eleccionRuta == 6:
                    eleccionRutaStr = NombreRutaAgregada3
                elif eleccionRuta == 7:
                    eleccionRutaStr = NombreRutaAgregada4

                GeneralData = abrirArchivo()
                for i in range (0,len(GeneralData[8]["NombresRutas"])):
                    if eleccionRutaStr == "Java":
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = "Java"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Miguel Sanchez"
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T1"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Sputnik"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "6am-10am"
                        guardarArchivo(GeneralData)

                    elif eleccionRutaStr == "NetCore":
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = "NetCore"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Jholver Garcia"
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T2"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Apolo"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "6am-10am"
                        guardarArchivo(GeneralData)
                    
                    elif eleccionRutaStr == "NodeJS":
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = "NodeJS"
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T3"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Pedro Gomez"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Artemis"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "6am-10am"
                        guardarArchivo(GeneralData)

                    elif eleccionRutaStr == GeneralData[8]["NombresRutas"][3]:
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = GeneralData[8]["NombresRutas"][3]
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T4"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Miguel Sanchez"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Sputnik"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "2pm-6pm"
                        guardarArchivo(GeneralData)

                    elif eleccionRutaStr == GeneralData[8]["NombresRutas"][4]:
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = GeneralData[8]["NombresRutas"][4]
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T5"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Jholver Garcia"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Apolo"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "2pm-6pm"
                        guardarArchivo(GeneralData)

                    elif eleccionRutaStr == GeneralData[8]["NombresRutas"][5]:
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = GeneralData[8]["NombresRutas"][5]
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T6"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Pedro Gomez"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Artemis"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "2pm-6pm"
                        guardarArchivo(GeneralData)

                    elif eleccionRutaStr == GeneralData[8]["NombresRutas"][6]:
                        GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = GeneralData[8]["NombresRutas"][6]
                        GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T7"
                        GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Miguel Sanchez"
                        GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Artemis"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                        GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "6pm-10pm"
                        guardarArchivo(GeneralData)


                AgregarGrupoT1 = {}
                AgregarGrupoT2 = {}
                AgregarGrupoT3 = {}
                AgregarGrupoT4 = {}
                AgregarGrupoT5 = {}
                AgregarGrupoT6 = {}
                AgregarGrupoT7 = {}

                GeneralData = abrirArchivo()
                for i in range (0,(len(GeneralData[3]["Estudiantes"]))):
                    if GeneralData[3]["Estudiantes"][i]["Ruta"] == "Java":
                        AgregarGrupoT1 = GeneralData[3]["Estudiantes"][i]
                        GeneralData[6]["Grupos"][0]["GrupoT1"].append(AgregarGrupoT1)
                        del GeneralData[3]["Estudiantes"][i]
                        guardarArchivo(GeneralData)
                        break

                GeneralData = abrirArchivo()
                for i in range (0,(len(GeneralData[3]["Estudiantes"]))):
                    if GeneralData[3]["Estudiantes"][i]["Ruta"] == "NetCore":
                        AgregarGrupoT2 = GeneralData[3]["Estudiantes"][i]
                        GeneralData[6]["Grupos"][1]["GrupoT2"].append(AgregarGrupoT2)
                        del GeneralData[3]["Estudiantes"][i]
                        guardarArchivo(GeneralData)
                        break
                
                GeneralData = abrirArchivo()
                for i in range (0,(len(GeneralData[3]["Estudiantes"]))):
                    if GeneralData[3]["Estudiantes"][i]["Ruta"] == "NodeJS":
                        AgregarGrupoT3 = GeneralData[3]["Estudiantes"][i]
                        GeneralData[6]["Grupos"][2]["GrupoT3"].append(AgregarGrupoT3)
                        del GeneralData[3]["Estudiantes"][i]
                        guardarArchivo(GeneralData)
                        break

                GeneralData = abrirArchivo()
                for i in range (0,(len(GeneralData[3]["Estudiantes"]))):
                    if GeneralData[3]["Estudiantes"][i]["Ruta"] == GeneralData[8]["NombresRutas"][3]:
                        AgregarGrupoT4 = GeneralData[3]["Estudiantes"][i]
                        GeneralData[6]["Grupos"][3]["GrupoT4"].append(AgregarGrupoT4)
                        del GeneralData[3]["Estudiantes"][i]
                        guardarArchivo(GeneralData)
                        break
            input("Cambios guardados!, presione ENTER para continuar")
            system("cls")

        #===AÑADIR NOTA DE MODULOS===        
        elif eleccionCoordinador == 5:
            print("----AÑADIR NOTA DE MODULOS A LOS CAMPERS----")

            boolAñadirNotas=True
            while boolAñadirNotas==True:
                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        EleccionNotaModulo= int(input("\n1. T1\n2. T2\n3. T3\n4. T4\n5. T5\n6. T6\n7. T7\n8. Salir\n\nSeleccione el grupo que desea editar: "))
                        break
                    except ValueError:
                        input("En este dato, debe ingresar un número, presione ENTER para continuar")
                        system("cls")

                if EleccionNotaModulo == 1:
                    print("T1")
                    contador=0
                    GeneralData=abrirArchivo()
                    if len(GeneralData[6]["Grupos"][0]["GrupoT1"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][0]["GrupoT1"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT1=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")
                        
                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][0]["GrupoT1"][EscogerEstudianteT1-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][0]["GrupoT1"][EscogerEstudianteT1-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][0]["GrupoT1"][EscogerEstudianteT1-1]["Estado"] = "Reprobado"
                            print("Reprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        guardarArchivo(GeneralData)


                elif EleccionNotaModulo == 2:
                    print("T2")
                    contador=0
                    GeneralData=abrirArchivo()
                    if len(GeneralData[6]["Grupos"][1]["GrupoT2"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][1]["GrupoT2"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT2=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")

                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][1]["GrupoT2"][EscogerEstudianteT2-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][1]["GrupoT2"][EscogerEstudianteT2-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][1]["GrupoT2"][EscogerEstudianteT2-1]["Estado"] = "Reprobado"
                            print("Reprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        guardarArchivo(GeneralData)

                elif EleccionNotaModulo == 3:
                    print("T3")
                    contador=0
                    GeneralData=abrirArchivo()
                    if len(GeneralData[6]["Grupos"][2]["GrupoT3"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][2]["GrupoT3"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT3=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")
                        
                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][2]["GrupoT3"][EscogerEstudianteT3-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][2]["GrupoT3"][EscogerEstudianteT3-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][2]["GrupoT3"][EscogerEstudianteT3-1]["Estado"] = "Reprobado"
                            print("Reprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        guardarArchivo(GeneralData)
                
                elif EleccionNotaModulo == 4:
                    print ("T4")
                    contador = 0
                    GeneralData = abrirArchivo()
                    if len(GeneralData[6]["Grupos"][3]["GrupoT4"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][3]["GrupoT4"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT4=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")
                
                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][3]["GrupoT4"][EscogerEstudianteT4-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][3]["GrupoT4"][EscogerEstudianteT4-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][3]["GrupoT4"][EscogerEstudianteT4-1]["Estado"] = "Reprobado"
                            print("Reprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        guardarArchivo(GeneralData)


                elif EleccionNotaModulo == 5:
                    print ("T5")
                    contador = 0
                    GeneralData = abrirArchivo()
                    if len(GeneralData[6]["Grupos"][4]["GrupoT5"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][4]["GrupoT5"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT5=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")

                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][4]["GrupoT5"][EscogerEstudianteT5-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][4]["GrupoT5"][EscogerEstudianteT5-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][4]["GrupoT5"][EscogerEstudianteT5-1]["Estado"] = "Reprobado"
                            print("Reprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        guardarArchivo(GeneralData)
                
                elif EleccionNotaModulo == 6:
                    print ("T6")
                    contador = 0
                    GeneralData = abrirArchivo()
                    if len(GeneralData[6]["Grupos"][5]["GrupoT6"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][5]["GrupoT6"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT6=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")

                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][5]["GrupoT6"][EscogerEstudianteT6-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][5]["GrupoT6"][EscogerEstudianteT6-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][5]["GrupoT6"][EscogerEstudianteT6-1]["Estado"] = "Reprobado"
                        guardarArchivo(GeneralData)
                
                elif EleccionNotaModulo == 7:
                    print ("T7")
                    contador = 0
                    GeneralData = abrirArchivo()
                    if len(GeneralData[6]["Grupos"][6]["GrupoT7"])==0:
                        input("No hay ningun Camper dentro de éste grupo, presione ENTER para continuar")
                        system("cls")
                    else:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            contador+=1
                            print("Identificador #",contador)
                            print("Nombres:",i["Nombres"])
                            print("Apellidos:",i["Apellidos"])
                        boolTryCatch = True
                        while boolTryCatch == True:
                            try:
                                EscogerEstudianteT7=int(input("Ingrese el identificador del estudiante al que le desea agregar notas: "))
                                break
                            except ValueError:
                                input("Debe ingresar un número, presione ENTER para continuar.")
                                system("cls")

                        GeneralData=abrirArchivo()
                        NotaPruebaTeorica = int(input("Ingrese la nota de la prueba teórica: "))
                        NotaPruebaPractica = int(input("Ingrese la nota de la prueba practica: "))
                        CantidadQuizes = int(input("¿Cuántos quizes hizo el trainer?: "))
                        contador = 0
                        NotaQuizes = 0
                        for i in range (0,CantidadQuizes):
                            contador += 1
                            print("Quiz #",contador)
                            NotaQuizes += int(input("Nota: "))                        
                        NotaQuizesFinal = NotaQuizes/CantidadQuizes
                        NotaFinalModulo = (NotaPruebaTeorica*0.30)+(NotaPruebaPractica*0.60)+(NotaQuizesFinal*0.10)
                        GeneralData[6]["Grupos"][6]["GrupoT7"][EscogerEstudianteT7-1]["NotaModulo"] = NotaFinalModulo

                        if NotaFinalModulo>=60:
                            GeneralData[6]["Grupos"][6]["GrupoT7"][EscogerEstudianteT7-1]["Estado"] = "Aprobado"
                            print("Aprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        else:
                            GeneralData[6]["Grupos"][6]["GrupoT7"][EscogerEstudianteT7-1]["Estado"] = "Reprobado"
                            print("Reprobado")
                            input("Presione ENTER para continuar")
                            system("cls")
                        guardarArchivo(GeneralData)

                elif EleccionNotaModulo == 8:
                    input("Presione ENTER para continuar")
                    system("cls")
                    boolAñadirNotas = False
                    break

                else:
                    input("Esta no es una opción válida, presione ENTER para continuar")
                    system("cls")
        
        elif eleccionCoordinador == 6:
            print("Saliendo del módulo del coordinador")
            input("Presione ENTER para continuar")
            system("cls")
            boolCoordinador = False

        else:
            input("Esta no es una opción válida, presione ENTER para continuar")

#==================================== MODULO DE REPORTES ==================================================
boolReportes = True
while boolReportes == True:
    boolTryCatch = True
    while boolTryCatch == True: 
        try:
            print("""Modulo de reportes: 
    1. Listar los campers que se encuentren en estado de inscrito.
    2. Listar los campers que aprobaron el examen inicial.
    3. Listar los entrenadores que se encuentran trabajando con CampusLands.
    4. Listar los campers que cuentan con bajo rendimiento.
    5. Listar los Campers y Trainers que se encuentren asociados a una ruta de entrenamiento.
    6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
    7. Salir.
          """)
            eleccionReportes = int(input("¿Qué desea hacer?: "))                    
            break
        except:
            input("En este dato, debe ingresar un número, presione ENTER para continuar")
            system("cls")
    
    system("cls")

    #=============================LISTAR CAMPERS EN ESTADO INSCRITO================================================
    if eleccionReportes == 1: 
        CampersInscritos = {}
        GeneralData = abrirArchivo()
        for i in range (len(GeneralData[2]["Estudiantes"])):
            if GeneralData[2]["Estudiantes"][i]["NotaPrueba"] == 0:
                CampersInscritos = GeneralData[2]["Estudiantes"]
            elif GeneralData[2]["Estudiantes"][i]["NotaPrueba"] != 0:
                continue
        print("Campers en estado inscrito")
        print("")
        
        if len(CampersInscritos)>=1:
            contador = 0
            for i in CampersInscritos:
                contador+=1
                print("Camper en Estado Inscrito #",contador),print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Nota:",i["NotaPrueba"])
                print("=================")
        else:
            print("No hay campers inscritos")

        input("Presione ENTER para continuar")
        system("cls")
    #===============================LISTAR CAMPERS QUE APROBARON LA PRUEBA INCIAL===================================
    elif eleccionReportes == 2:
        ListarAprobados = {}

    #============================== LISTAR TRAINERS DENTRO DE CAMPUSLANDS===========================================
    elif eleccionReportes == 3:
        print("Listar Trainers"),print("")
        GeneralData = abrirArchivo()
        contador = 0 
        for i in (GeneralData[0]["Trainers"]):
            contador+=1
            print("Trainer #",contador),print("Nombre:",i["Nombre"]),print("Ruta:",i["Ruta"]),print("Horario:",i["Horario"]),print("Grupo:",i["Grupo"])
            print("=================")
        
        input("Presione ENTER Para continuar")
        system("cls")


    elif eleccionReportes == 4:
        print("Listar Campers con rendimiento Bajo")
        
    #============================ LISTAR TRAINERS Y CAMPERS CON LA MISMA RUTA DE ENTRENAMIENTO ================================================================
    elif eleccionReportes == 5:
        TrainerRutaNodeJS = []
        CampersRutaNodeJS = []
        TrainerRutaNetCore = []
        CampersRutaNetCore = []
        TrainerRutaJava = []
        CampersRutaJava = []

        GeneralData = abrirArchivo()
        for i in range (0,(len(GeneralData[0]["Trainers"]))):
            if GeneralData[0]["Trainers"][i]["Ruta"] == "NetCore":
                TrainerRutaNetCore.append(GeneralData[0]["Trainers"][i])
        if len(GeneralData[6]["Grupos"][0]["GrupoT1"])>=1:
            for i in range (0,len(GeneralData[6]["Grupos"][0]["GrupoT1"])):
                if GeneralData[6]["Grupos"][0]["GrupoT1"][i]["Ruta"] == "NetCore":
                    CampersRutaNetCore.append(GeneralData[6]["Grupos"][0]["GrupoT1"][i])

        GeneralData = abrirArchivo()
        for i in range (0,(len(GeneralData[0]["Trainers"]))):
            if GeneralData[0]["Trainers"][i]["Ruta"] == "Java":
                TrainerRutaJava.append(GeneralData[0]["Trainers"][i])
        if len(GeneralData[6]["Grupos"][1]["GrupoT2"])>=1:
            for i in range (0,len(GeneralData[6]["Grupos"][1]["GrupoT2"])):
                if GeneralData[6]["Grupos"][1]["GrupoT2"][i]["Ruta"] == "Java":
                    CampersRutaJava.append(GeneralData[6]["Grupos"][1]["GrupoT2"][i])

        GeneralData = abrirArchivo()
        for i in range (0,(len(GeneralData[0]["Trainers"]))):
            if GeneralData[0]["Trainers"][i]["Ruta"] == "NodeJS":
                TrainerRutaNodeJS.append(GeneralData[0]["Trainers"][i])
        if len(GeneralData[6]["Grupos"][2]["GrupoT3"])>=1:
            for i in range (0,len(GeneralData[6]["Grupos"][2]["GrupoT3"])):
                if GeneralData[6]["Grupos"][2]["GrupoT3"][i]["Ruta"] == "NodeJS":
                    CampersRutaNodeJS.append(GeneralData[6]["Grupos"][2]["GrupoT3"][i])

        boolReportesRutas = True
        while boolReportesRutas == True:
            print("Listar Campers y Trainers asociados a una misma ruta de entrenamiento")
            boolTryCatch = True
            while boolTryCatch == True:
                try:
                    eleccionReportesRutas = int(input("\nRutas: \n1. NetCore \n2. Java \n3. NodeJS \n4. Salir del modulo \n¿Qué desea hacer?: "))
                    break
                except ValueError:
                    input("Debe ingresar un númerom, presione ENTER para continuar")
                    system("cls")
            system("cls")

            if eleccionReportesRutas == 1:
                print("Trainer de la ruta de aprendizaje NetCore:")
               
                for i in TrainerRutaNetCore:
                    print ("Nomrbre",i["Nombre"])
                    print("Grupo:",i["Grupo"])
                print("==============="),print("Campers: ")
                if len(CampersRutaNetCore)==0:
                    print("")
                    print("En esta ruta de Entrenamiento no hay ningún Camper")
                else:
                    contador = 0
                    for i in CampersRutaNetCore:
                        contador +=1
                        print("Camper #",contador)
                        print("Nombres:",i["Nombres"])
                        print("Apellidos:",i["Apellidos"])
                        print("Grupo:",i["Grupo"])
                        print("===============")
                    input("Presione ENTER para continuar")
                    system("cls")

            elif eleccionReportesRutas == 2:
                print("Trainer de la ruta de aprendizaje Java:")
                for i in TrainerRutaJava:
                    print ("Nombre:",i["Nombre"])
                    print("Grupo:",i["Grupo"])
                    print("==============="),print("Campers: ")
                if len(CampersRutaJava) == 0:
                    print("")
                    print("Enesta ruta de Entrenamiento no hay ningún Camper")
                else:
                    contador = 0
                    for i in CampersRutaJava:
                        contador +=1
                        print("Camper #",contador)
                        print("Nombres:",i["Nombres"])
                        print("Apellidos:",i["Apellidos"])
                        print("Grupo:",i["Grupo"])
                        print("===============")
                    input("Presione ENTER para continuar")
                    system("cls")

            elif eleccionReportesRutas == 3:
                print("Trainer de la ruta de aprendizaje NodeJS:")
                for i in TrainerRutaNodeJS:
                    print ("Nombre:",i["Nombre"])
                    print("Grupo:",i["Grupo"])
                print("==============="),print("Campers: ")
                if len(CampersRutaNodeJS) == 0:
                    print("")
                    print("En esta ruta de entrenamiento no hay ningún Camper")
                else:
                    contador = 0
                    for i in CampersRutaNodeJS:
                        contador +=1
                        print("Camper #",contador)
                        print("Nombres:",i["Nombres"])
                        print("Apellidos:",i["Apellidos"])
                        print("Grupo:",i["Grupo"])
                        print("===============")
                    input("Presione ENTER para continuar")
                    system("cls")

            elif eleccionReportesRutas == 4:
                boolReportesRutas = False
                input("Saliendo, presione ENTER para continuar")
                system("cls")

            else:
                input("Esta no es una opción válida, presione ENTER para intentar de nuevo")
                system("cls")


    elif eleccionReportes == 6:
        print("Listar Campers que perdieron y aprobaron cada uno de los modulos dependiendo la ruta de entrenamiento")


    elif eleccionReportes == 7:
        print("Saliendo del programa")
        boolReportes = False
        
    else:
        print("Esta no es una opción válida, intente de nuevo")
        input("Presione ENTER para continuar")
        system("cls")
      
#Desarrollado por Brayan Maldonado Y Maria Lizarazo - Campers