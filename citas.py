citas = {}
users = []
passwords = []
descripcions = []


def registrar(usuario, cont1, cont2):
  users.append(usuario)
  if cont2 == cont1:
    passwords.append(cont1)
    print("usuiario registrado")
  while cont2 != cont1:
    print("contraseñas no coinciden")
    cont1 = input("ingrese contraseña: ")
    cont2 = input("confirme contraseña: ")
    if cont2 == cont1:
      passwords.append(cont1)
      print("usuiario registrado")

logoin =  lambda usuario, cont: print(f"bienvenido {usuario}")if usuario in users and cont in passwords else print(f"{usuario} no aparece registrado")
    
def guardar(usuario, desc, tipo):
  descripcion = [tipo, desc]
  descripcions.append(descripcion)
  if usuario in users:
   citas["cliente"] = {"usuario": usuario, "descripcion": desc}     
   print("cita guardada")


if __name__ == "__main__":
   while True:
     print("-----menu")
     print(" 1 ingresar \n 2 registrarse \n 3 salir")
     opcion = input("digite opcion: \n")
     if opcion == "1":
       user = input("ingrese su usuario: ")
       password= input("ingrese su contraseña: ")
       logoin(user, password)
       while True:
        print("-----opciones: ")
        print(" 1 guardar cita \n 2 ver citas \n 3 ver usuarios \n 4 salir")
        op = input("ingrese opcion? \n")
        if op == "1":         
         tipo = input("ingrese tipo de cita: ")
         desc = input("ingrese descripcion: ")
         guardar(user, desc, tipo )
        elif op == "2":
          if citas == None:
            print("no hay citas aun")
          else:
           print("Citas: ")           
           for clave, valor in citas.items():
            print(f"{clave}:{valor}") 
        elif op == "3":
          print("Usuarios: ")
          i = 1
          for us in users:
            i+=1
            print(f"usuario {i}: {us}")  
        elif op == "4":
          break   
     elif opcion == "2":
       user = input("ingrese su usuario: ")
       cont1 = input("ingrese su contraseña: ")
       cont2 = input("confirme su contraseña: ")
       registrar(user, cont1, cont2)
     elif opcion == "3": 
       break
    
       

     
                    


