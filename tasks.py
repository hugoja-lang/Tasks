class Tasks:

    def __init__(self):
        self.libro = [] #Definimos el libro donde vamos a poner todas las tareas


    def agregarTareas(self):
        try: 
            numTareas = int(input("\033[33m" + "Cuantas tareas deseas agregar?: " + "\033[0m")) #Pregunta cuantas tareas desea agregar
            if numTareas > 0: #Si el numero de tareas es mayor a 0
                    for i in range(numTareas): 
                        nuevaTarea = input("\033[33m" + "Cual es la tarea?: " + "\033[0m")
                        if not nuevaTarea in self.libro: #Si no hay tareas dentro del libro
                            print("\033[33m" + "Tarea agregada satisfactoriamente!" + "\033[0m")
                            self.libro.append(nuevaTarea) #Agregamos tareas al libro                    
            else:
                print("\033[33m" + "No se pueden agregar cero tareas!" + "\033[0m")   #Si es menor a 0 o igual a 0, le manda un msj
        except ValueError:
             print("\033[33m" + "No puedes agregar texto!" +"\033[0m") #Si el usuario no agrega numeros en el numerodetareas a agregar, entonces le manda msj


    def verTareas(self):
        if not self.libro: #Si no hay nada en el libro
             print("\033[33m" +"No tienes tareas pendientes!" + "\033[0m")
        else:
            print("Aqui estan tus tareas: ")
            for indice, tarea in enumerate(self.libro): #Por cada indice(el numero de tarea) y la tarea enumeralos
                print(f"\033[33m {indice + 1}.{tarea} \033[0m") #El numero de tareas empieza desde el numero 1

    def eliminarTareas(self):
            self.verTareas() #Le muestro las tareas
            try:
                tarea_a_eliminar = int(input("\033[33m" + "Que tarea deseas eliminar?:" + "\033[0m"))
                indice = tarea_a_eliminar - 1 #El pc empieza desde el cero, y aqui empezaremos desde el uno, entonces es uno - uno cero, que es donde empieza el pc
                if indice < 0 or indice >= len(self.libro): #Si las tareas que quieres eliminar son mayores, o son negativas entonces no elimina nada
                    print("El numero no es valido") #Y manda msj
                else:
                    print("Tarea eliminada satisfactoriamente!") #Si no manda msj de que la elimino
                    self.libro.pop(indice) #Y la elimina
            except ValueError:
                print("No puedes ingresar letras") #Aqui si no ingresa int , le manda msj para evitar que se rompa
                
    def banner(self):
        print("+---------------------------------------------------+")
        print("| ████████╗ █████╗  ███████╗██╗  ██╗███████╗         |")
        print("| ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝         |")
        print("|    ██║   ███████║███████╗█████╔╝ ███████╗         |")
        print("|    ██║   ██╔══██║╚════██║██╔═██╗ ╚════██║         |")
        print("|    ██║   ██║  ██║███████║██║  ██╗███████║         |")
        print("|    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝         |")
        print("|Hecho por @hugoja-lang                             |")
        print("+---------------------------------------------------+")
        print("\033[32m" + "Bienvenido geni@!" + "\033[0m")
        print("------------------------------------------------------")
        print("AVISO: No se guardan las tareas al momento de cerrar")
        print("-------------------------------------------------------")
    
    def menu(self):
        opciones = (
        "1. Agregar tareas\n"
        "2. Eliminar tareas\n"
        "3. Ver tareas\n"
        "4. Salir\n"
        "Elige una opción: "
         )
        try:
            return int(input(opciones)) #Ve que si sea int
        except ValueError:
            print("No ingresaste numeros") #Si no manda msj
            return 0 #Retornamos numeros
if __name__=="__main__":
    task = Tasks()
    task.banner()
    
    while True:       
            usuario = task.menu()
            if usuario == 1:
                task.agregarTareas()
            elif usuario == 2:
                task.eliminarTareas()
            elif usuario == 3:
                task.verTareas()
            elif usuario == 4:
                break
            else:
                print("Esa opcion no existe!")

              
              
