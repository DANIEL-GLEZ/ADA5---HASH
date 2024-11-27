# ADA5---HASH
Tarea 
El primer ejercicio consiste en gestionar una tabla hash donde el usuario puede agregar, buscar y eliminar elementos utilizando un menú interactivo. El programa ofrece las siguientes opciones:
1.	Agregar elemento: Permite al usuario añadir un par clave-valor.
2.	Buscar elemento: Permite al usuario buscar un elemento por su clave.
3.	Eliminar elemento: Permite al usuario eliminar un elemento por su clave.
4.	Salir: Permite al usuario salir del programa.
Motivo de Uso del Método de Búsqueda Hash
Este ejercicio utiliza el método de búsqueda hash debido a sus características de eficiencia y rapidez. La búsqueda hash permite acceder a los elementos en tiempo constante promedio (O(1)), lo que significa que el tiempo de búsqueda, inserción y eliminación no depende del tamaño de la tabla. Esto es especialmente útil cuando se manejan grandes volúmenes de datos y se necesita acceder a ellos rápidamente.
El segundo ejercicio consiste en gestionar una lista de contactos telefónicos utilizando una tabla hash. El programa ofrece las siguientes opciones:
1.	Agregar contacto: Permite al usuario añadir un contacto con nombre y número de teléfono.
2.	Buscar contacto: Permite al usuario buscar un contacto por su nombre.
3.	Eliminar contacto: Permite al usuario eliminar un contacto por su nombre.
4.	Listar todos los contactos: Permite al usuario listar todos los contactos almacenados en la tabla hash.
5.	Salir: Permite al usuario salir del programa.
Motivo de Uso del Método de Búsqueda Hash
El ejercicio utiliza el método de búsqueda hash debido a sus ventajas de eficiencia en términos de tiempo. La búsqueda hash es ideal para gestionar una lista de contactos telefónicos porque permite añadir, buscar y eliminar contactos de manera rápida y eficiente. Además, al utilizar una función hash adecuada, se minimizan las colisiones y se optimiza el acceso a los datos, lo que es crucial para mantener un rendimiento alto en la gestión de contactos.



Mejorar con Otro Método de Búsqueda
En algunos casos, se pueden considerar otros métodos de búsqueda que podrían ser más adecuados o eficientes según el contexto y las necesidades específicas. Aquí hay algunos ejemplos:
1.	Árboles Binarios de Búsqueda (BST):
o	Ventajas: Mantienen los elementos ordenados y pueden ofrecer tiempos de búsqueda, inserción y eliminación eficientes (O(log⁡n)O(\log n)) si el árbol está equilibrado.
o	Desventajas: En el peor de los casos, si el árbol está desbalanceado, las operaciones pueden degradarse a O(n)O(n).
2.	Árboles B (B-Trees):
o	Ventajas: Son eficientes para operaciones de búsqueda, inserción y eliminación en estructuras de datos almacenadas en discos, lo que los hace ideales para bases de datos y sistemas de archivos.
o	Desventajas: Pueden ser más complejos de implementar y gestionar en comparación con las tablas hash.
3.	Listas Enlazadas:
o	Ventajas: Son simples de implementar y útiles para estructuras de datos dinámicas donde la inserción y eliminación son frecuentes.
o	Desventajas: La búsqueda en listas enlazadas es O(n)O(n), lo que es menos eficiente que las tablas hash y árboles en grandes conjuntos de datos.
Conclusión Final
Los métodos de búsqueda hash ofrecen un excelente rendimiento en términos de velocidad y eficiencia, especialmente cuando se trabaja con grandes volúmenes de datos. Los ejercicios demostraron cómo las tablas hash pueden ser utilizadas para gestionar datos de manera eficiente, permitiendo operaciones rápidas de búsqueda, inserción y eliminación.
