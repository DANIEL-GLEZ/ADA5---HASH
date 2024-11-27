class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
    
    def hash_func(self, clave):
        return hash(clave) % self.tamaño
    
    def agregar(self, clave, valor):
        índice = self.hash_func(clave)
        for i, (k, v) in enumerate(self.tabla[índice]):
            if k == clave:
                self.tabla[índice][i] = (clave, valor)
                return
        self.tabla[índice].append((clave, valor))
    
    def buscar(self, clave):
        índice = self.hash_func(clave)
        for k, v in self.tabla[índice]:
            if k == clave:
                return v
        return None
    
    def eliminar(self, clave):
        índice = self.hash_func(clave)
        for i, (k, v) in enumerate(self.tabla[índice]):
            if k == clave:
                del self.tabla[índice][i]
                return True
        return False

def mostrar_menu():
    tabla_hash = TablaHash(10)
    while True:
        print("\nMenú:")
        print("1. Agregar elemento")
        print("2. Buscar elemento")
        print("3. Eliminar elemento")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            clave = input("Introduce la clave: ")
            valor = input("Introduce el valor: ")
            tabla_hash.agregar(clave, valor)
            print(f"Elemento añadido: {clave} -> {valor}")
        
        elif opcion == "2":
            clave = input("Introduce la clave a buscar: ")
            resultado = tabla_hash.buscar(clave)
            if resultado:
                print(f"Elemento encontrado: {clave} -> {resultado}")
            else:
                print("Elemento no encontrado.")
        
        elif opcion == "3":
            clave = input("Introduce la clave a eliminar: ")
            if tabla_hash.eliminar(clave):
                print(f"Elemento eliminado: {clave}")
            else:
                print("Elemento no encontrado para eliminar.")
        
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

mostrar_menu()
