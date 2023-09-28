estudiantes = {}

prom =  lambda n1, n2, n3:(n1 + n2 + n3) / 3
  
def guardarInfo(id, nombre, n1, n2, n3):
    notas = [n1, n2, n3]       
    estudiantes[id] = {"nombre": nombre, "notas": notas}
    return estudiantes

def actualizarNotas(id, n1, n2, n3):
    if id in estudiantes:
        estudiantes[id]["notas"] = [n1, n2, n3]
        print(f"Notas actualizadas para el estudiante con ID {id}.")
    else:
        print(f"El estudiante con ID {id} no existe en la lista.")

while True:
    print("Opciones:")
    print("1. Guardar")
    print("2. Mostrar")
    print("3. Mostrar todos")
    print("4. actualizar")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":        
        id = input("Ingrese identificación: ")
        nombre = input("Ingrese nombre del estudiante: ")
        n1 = float(input("Ingrese nota uno: "))
        n2 = float(input("Ingrese nota dos: "))
        n3 = float(input("Ingrese nota tres: "))
        guardarInfo(id, nombre, n1, n2, n3)
        print("Estudiante guardado.")

    elif opcion == "2":
        id_buscar = input("Ingrese el ID del estudiante que desea buscar: ")
        estudiante = estudiantes.get(id_buscar)
        if estudiante:
            nombre_estudiante = estudiante["nombre"]
            notas_estudiante = estudiante["notas"]
            promedio_estudiante = prom(*notas_estudiante)
            print(f"Nombre: {nombre_estudiante}")
            print(f"Notas: {notas_estudiante}")
            print(f"Promedio: {promedio_estudiante}")
        else:
            print("El estudiante no se encuentra en la lista.")
    elif opcion == "3":
        print("lista de estuadiantes: \n")
        for clave, valor in estudiantes.items():
            print(f'{clave}:{valor}')  
    elif opcion == "4":        
        id_actualizar = input("Ingrese el ID del estudiante al que desea actualizar las notas: ")
        n1 = float(input("Ingrese la nueva nota uno: "))
        n2 = float(input("Ingrese la nueva nota dos: "))
        n3 = float(input("Ingrese la nueva nota tres: "))
        actualizarNotas(id_actualizar, n1, n2, n3)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

print(estudiantes)        
