elif ListarAprobados == 7:
            if len(GeneralData[6]["Grupos"][6]["GrupoT7"]) == 0:
                input("Este Grupo está vacio, Presione ENTER para continuar")
                system("cls")
            else: 
                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        ModuloVer = int(input("\n1. Fundamentos de programación\n2. Programación web\n3. Programación formal\n4. Bases de datos\n5. Backend\¿Qué modulo desea revisar?: "))
                        system("cls")
                        break
                    except ValueError:
                        input("Debe ingresar un valor numerico, presione ENTER para continuar")
                        system("cls")
                boolTryCatch = True
                while boolTryCatch == True:
                    try:
                        AproDesapro = int(input("Desea ver\n1. Aprobados\n2. Desaprobados\n¿Qué deesea ver?: "))
                        system("cls")
                        break
                    except ValueError:
                        input("Debe ingresar un valor entero, presione ENTER para continuar")
                        system("cls")

                if ModuloVer == 1:
                    if AproDesapro == 1:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoFundamentos"] == "Aprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                                print("")
                                input("\nPresione ENTER para continuar")
                                system("cls")
                            else: 
                                "No hay ningun Camper para mostrar"
                    elif AproDesapro == 2:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoFundamentos"] == "Reprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                            else:
                                "No hay ningun Camper para mostrar"
                
                elif ModuloVer == 2:
                    if AproDesapro == 1:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoProWeb"] == "Aprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                                print("")
                                input("\nPresione ENTER para continuar")
                                system("cls")
                            else: 
                                "No hay ningun Camper para mostrar"
                    elif AproDesapro == 2:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoProweb"] == "Reprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                            else:
                                "No hay ningun Camper para mostrar"

                elif ModuloVer == 3:
                    if AproDesapro == 1:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoProFormal"] == "Aprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                                print("")
                                input("\nPresione ENTER para continuar")
                                system("cls")
                            else: 
                                "No hay ningun Camper para mostrar"
                    elif AproDesapro == 2:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoProFormal"] == "Reprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                            else:
                                "No hay ningun Camper para mostrar"

                elif ModuloVer == 4:
                    if AproDesapro == 1:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoBasesDatos"] == "Aprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                                print("")
                                input("\nPresione ENTER para continuar")
                                system("cls")
                            else: 
                                "No hay ningun Camper para mostrar"
                    elif AproDesapro == 2:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoBasesDatos"] == "Reprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                            else:
                                "No hay ningun Camper para mostrar"
                
                elif ModuloVer == 5:
                    if AproDesapro == 1:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoBackend"] == "Aprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                                print("")
                                input("\nPresione ENTER para continuar")
                                system("cls")
                            else: 
                                "No hay ningun Camper para mostrar"
                    elif AproDesapro == 2:
                        for i in GeneralData[6]["Grupos"][6]["GrupoT7"]:
                            if i["EstadoBackend"] == "Reprobado":
                                print(i["Nombres"])
                                print(i["Apellidos"])
                                print(i["Grupo"])
                            else:
                                "No hay ningun Camper para mostrar"