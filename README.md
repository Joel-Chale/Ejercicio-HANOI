Chalé Matu Joel de Jesús 3SA

La Torre de Hanoi es un problema matemático que consiste en mover una torre de discos de una varilla de origen a una varilla de destino, utilizando una varilla auxiliar y respetando las siguientes reglas:
- Solo se puede mover un disco a la vez.
- Únicamente se puede mover el disco que se encuentra en la parte superior de una torre.
- Nunca se puede colocar un disco grande encima de uno más pequeño.
El objetivo es resolver el problema utilizando recursividad y medir el tiempo que tarda el programa en calcular la solución para diferentes cantidades de discos: 5, 10, 30 y 64.

los métodos utilizados son los siguientes:

torre_hanoi()	Resuelve el problema recursivamente, indicando los movimientos de los discos.
contar_movimientos()	Calcula el número mínimo de movimientos con la fórmula \(2^n-1\).
medir_tiempo()	Mide cuánto tarda el cálculo mediante time.perf_counter().
main()	Ejecuta las mediciones para las cuatro cantidades de discos.


El tiempo que tardo fue

Discos: 5
Movimientos necesarios: 31
Tiempo de cálculo: 0.00000090 segundos

Discos: 10
Movimientos necesarios: 1,023
Tiempo de cálculo: 0.00000270 segundos

Discos: 30
Movimientos necesarios: 1,073,741,823
Tiempo de cálculo: 57.07958 segundos

Discos: 64
Movimientos necesarios: 18,446,744,073,709,551,615
Tiempo de cálculo: no termino


- Conclusión:
La Torre de Hanoi es un ejemplo de algoritmo recursivo que permite comprender cómo un problema puede dividirse en problemas más pequeños hasta alcanzar un caso base.
La cantidad de movimientos crece exponencialmente conforme aumenta el número de discos. Por ejemplo, pasar de 30 a 64 discos incrementa la cantidad de movimientos de poco más de mil millones a más de 18 trillones en la escala larga del español.
Esto demuestra que un algoritmo puede ser sencillo de implementar, pero muy costoso de ejecutar cuando aumenta el tamaño del problema. La recursividad facilita la organización del código, pero no elimina el crecimiento exponencial del trabajo necesario.