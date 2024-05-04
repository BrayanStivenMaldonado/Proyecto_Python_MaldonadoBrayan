if RutaElegida == "NetCore":
                GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = "NetCore"
                GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Jholver Garcia"
                GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T1"
                GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Apolo"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "06am-10am"
                guardarArchivo(GeneralData)


            elif RutaElegida == "Java":
                GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = "Java"
                GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Miguel Sanchez"
                GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T2"
                GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Apolo"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "10am-2pm"
                guardarArchivo(GeneralData)


            elif RutaElegida == "NodeJS":
                GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = "NodeJS"
                GeneralData[3]["Estudiantes"][Camper-1]["Grupo"] = "T3"
                GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Pedro Gomez"
                GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Apolo"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = "2pm-6pm"
                guardarArchivo(GeneralData)

            print("Cambios Realizados!")
            input("Presione ENTER para continuar")
            system("cls")

            AgregarGrupoT1 = {}
            AgregarGrupoT2 = {}
            AgregarGrupoT3 = {}

            GeneralData = abrirArchivo()
            for i in range (0,(len(GeneralData[3]["Estudiantes"]))):
                if GeneralData[3]["Estudiantes"][i]["Ruta"] == "NetCore":
                    AgregarGrupoT1 = GeneralData[3]["Estudiantes"][i]
                    GeneralData[6]["Grupos"][0]["GrupoT1"].append(AgregarGrupoT1)
                    del GeneralData[3]["Estudiantes"][i]
                    guardarArchivo(GeneralData)
                    break

            GeneralData = abrirArchivo()
            for i in range (0,(len(GeneralData[3]["Estudiantes"]))):
                if GeneralData[3]["Estudiantes"][i]["Ruta"] == "Java":
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
                
            print(AgregarGrupoT1)
            print(AgregarGrupoT2)
            print(AgregarGrupoT3)
