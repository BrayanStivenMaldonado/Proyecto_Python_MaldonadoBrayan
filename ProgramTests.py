#Imprimir los datos que se tienen de los estudiantes 1
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
#====================================================

GeneralData = abrirArchivo() #Se guarda la información que se tiene dentro del archivo .json dentro de una variable para depués usarla dentro del programa
GuardarArchivo(GeneralData) #Guardar los cambios que se hagan al archivo.json