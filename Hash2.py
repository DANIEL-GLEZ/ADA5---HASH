class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
    
    def hash_func(self, clave):
        return hash(clave) % self.tamaño
    
    def agregar(self, nombre, telefono):
        índice = self.hash_func(nombre)
        for i, (n, t) in enumerate(self.tabla[índice]):
            if n == nombre:
                self.tabla[índice][i] = (nombre, telefono)
                return
        self.tabla[índice].append((nombre, telefono))
    
    def buscar(self, nombre):
        índice = self.hash_func(nombre)
        for n, t in self.tabla[índice]:
            if n == nombre:
                return t
        return None
    
    def eliminar(self, nombre):
        índice = self.hash_func(nombre)
        for i, (n, t) in enumerate(self.tabla[índice]):
            if n == nombre:
                del self.tabla[índice][i]
                return True
        return False

    def listar_todos(self):
        contactos = []
        for lista in self.tabla:
            contactos.extend(lista)
        return contactos

def mostrar_menu():
    tabla_contactos = TablaHash(10)
    while True:
        print("\nMenú de Contactos:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Listar todos los contactos")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre: ")
            telefono = input("Introduce el número de teléfono: ")
            tabla_contactos.agregar(nombre, telefono)
            print(f"Contacto añadido: {nombre} -> {telefono}")
        
        elif opcion == "2":
            nombre = input("Introduce el nombre a buscar: ")
            resultado = tabla_contactos.buscar(nombre)
            if resultado:
                print(f"Contacto encontrado: {nombre} -> {resultado}")
            else:
                print("Contacto no encontrado.")
        
        elif opcion == "3":
            nombre = input("Introduce el nombre a eliminar: ")
            if tabla_contactos.eliminar(nombre):
                print(f"Contacto eliminado: {nombre}")
            else:
                print("Contacto no encontrado para eliminar.")
        
        elif opcion == "4":
            contactos = tabla_contactos.listar_todos()
            if contactos:
                print("\nLista de todos los contactos:")
                for nombre, telefono in contactos:
                    print(f"{nombre} -> {telefono}")
            else:
                print("No hay contactos en la lista.")
        
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

mostrar_menu()
