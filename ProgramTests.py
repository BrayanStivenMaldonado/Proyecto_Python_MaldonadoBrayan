#Imprimir los datos que se tienen de los estudiantes 1
GeneralData = abrirArchivo()
contador = 0
for i in GeneralData[0]["EstudiantesGeneral"]:
    contador += 1
    print("ESTUDIANTE #",contador)
    print("# de identificacion:",i["Identificacion"])
    print ("Nombres:",i["Nombres"])
    print ("Apellidos:",i["Apellidos"])
    print ("Direccion:",i["Direccion"])
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
#====================================================

GeneralData = abrirArchivo() #Se guarda la informacion que se tiene dentro del archivo .json dentro de una variable para depués usarla dentro del programa
GuardarArchivo(GeneralData) #Guardar los cambios que se hagan al archivo.json

#Mostrar los trainers 2
GeneralData = abrirArchivo()
contador = 0
for i in GeneralData[1]["Trainers"]:
    contador += 1
    print("Trainer #",contador)
    print("Nombre:",i["Nombre"])
    print("Ruta:",i["Ruta"])
    print("Horario:",i["Horario"])

#Mostrar Rutas de Estudio 3
GeneralData = abrirArchivo()
contador = 0 
for i in GeneralData[2]["RutasEstudio"]:
    contador += 1
    print("Ruta de Estudio #",contador,":",i["NombreRuta"])

#Mostrar Roles 4
GeneralData = abrirArchivo()
print("Roles:")
for i in GeneralData[3]["Roles"]:
    print(i["Rol"])

#Mostrar Modulos de Entrenamiento 5
GeneralData = abrirArchivo()
print("Modulos:")
for i in GeneralData[4]["ModulosEntrenamiento"]:
    print(i["Modulo"])

#Mostrar Grupos 6
GeneralData = abrirArchivo()
print("Grupos:")
for i in GeneralData[5]["Grupos"]:
    print(i["Grupo"])

#Mostrar Salones 7
GeneralData = abrirArchivo()
print("Salones: ")
for i in GeneralData[6]["Salones"]:
    print(i["Salon"])

#Crear nuevo Grupo
GeneralData = abrirArchivo()
NuevoGrupo = str(input("Ingrese el nombre del nuevo grupo: "))
GeneralData[5]["Grupos"].append({
    "Grupo" : NuevoGrupo
})
print("Grupo Añadido!")
guardarArchivo(GeneralData) 




#### Guardado Copia, por si acaso.

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
                    "NotaPrueba" : input("Ingrese la nota de la prueba: ")
                    })
            guardarArchivo(GeneralData)
            print("Camper Registrado!")
            print("")
            input("Presione ENTER para continuar")
            system("cls")
            break
    
        #===DEFINIR RUTA DEL CAMPER===        
        if eleccionCoordinador == 2:
            print("---REGISTRAR RUTA DE ESTUDIO---")
            GeneralData = abrirArchivo()
            print("Elige entre:\n NoteCore \n Java \n NoteJS")
            for i in GeneralData[3]["Estudiantes"]:
                print("\nIdetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])
            
            CamperParaRuta = int(input("\nIngrese el identificador del Camper que desea escoger: "))
            #Falta hacer que escoja al camper
            RutaElegida = str(input("Ingrese el nombre de la Ruta que le desea definir: "))
            GeneralData[3]["Estudiantes"][CamperParaRuta-1]["Ruta"] = RutaElegida
            guardarArchivo(GeneralData)
            break


        if eleccionCoordinador == 3: 
           
            GeneralData = abrirArchivo()
            print("---INGRESAR LA NOTA DE LA PRUEBA---")
            for i in GeneralData[2]["Estudiantes"]:
                print("Idetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])
            
            CamperParaNota = int(input("Ingrese el Camper que desea Agregar"))
            NotaCamper = int(input("Ingrese la nota: "))
            GeneralData[2]["Estudiantes"][CamperParaNota-1]["NotaPrueba"] = NotaCamper
            guardarArchivo(GeneralData)
            break


        #===DEFINIR TRAINER===        
        if eleccionCoordinador == 4:
            print("---ASIGNAR TRAINER---")
            print("\n Los Trainers disponibles son:\n Pedro Perez \n Jholver Garcia \n Stiven Carvajal")
            GeneralData = abrirArchivo()
            for i in GeneralData[3]["Estudiantes"]:
                print("\nIdetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])
            
            TrainerElegido = int(input("\nIngrese el identificador del Camper que desea escoger: "))
            #Falta hacer que escoja al camper
            TrainerConfirmado = str(input("Ingrese el nombre del Trainer que desea asignar: "))
            GeneralData[3]["Estudiantes"][TrainerElegido-1]["Trainer"] = TrainerConfirmado
            guardarArchivo(GeneralData)
            break


        #===DEFINIR SALON===        
        if eleccionCoordinador == 5:
            print("---ASIGNAR SALON---")
            print("\nLos salones a usar son:\n Sputnik\n Apolo\n Artemis")
            GeneralData = abrirArchivo()
            for i in GeneralData[3]["Estudiantes"]:
                print("\nIdetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])
            
            SalonPorElegir = int(input("Ingrese el identificador del Camper que desea escoger: "))
            #Falta hacer que escoja al camper
            SalonAsignado = str(input("Ingrese el nombre del salon que le desea asignar: "))
            GeneralData[3]["Estudiantes"][SalonPorElegir-1]["Salon"] = SalonAsignado
            guardarArchivo(GeneralData)
            break


        #===DEFINIR HORARIO===        
        if eleccionCoordinador == 6:
            print("---ASIGNAR HORARIO DEL CAMPER---")
            print("\nLos horarios son:\n 6am-10am\n 10am-2pm\n 2pm-6pm\n 6pm-10pm")
            GeneralData = abrirArchivo()
            for i in GeneralData[3]["Estudiantes"]:
                print("\nIdetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])
            
            Horario = int(input("Ingrese el identificador del Camper que desea escoger: "))
            #Falta hacer que escoja al camper
            HorarioAsignado = str(input("Ingrese el horario a asignar: "))
            GeneralData[3]["Estudiantes"][Horario-1]["Horario"] = HorarioAsignado
            guardarArchivo(GeneralData)
            break

