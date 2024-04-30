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
