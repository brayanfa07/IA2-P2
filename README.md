# Proyecto 2 - Connect 4 Genético


# IC6200 Inteligencia Artificial

Enlace de GitHub: https://github.com/brayanfa07/IA2-P2

## Integrantes

- Brayan Fajardo Alvarado - 201157035
- Fabricio Castillo Alvarado - 2014062977
- Gerald Mora Mora - 2014064955

### II Semestre 2018

Elaboración del proyecto "Connect 4 Genético", creado con algoritmos genéticos

---

## 1. Introducción


## 2. Connect 4 Genético

En este proyecto los estudiantes desarrollaran un agente que sepa jugar Connect 4 ( https://en.wikipedia.org/wiki/Connect_Four ) utilizando una combinación de técnicas de búsqueda.

Los algoritmos utilizados se encargaran de resolver diferentes aspectos del juego. Se espera que los estudiantes logren entrenar agentes que puedan jugar Connect 4 interactivamente con un humano, con la mayor inteligencia posible. Una vez entrenados los agentes deberá ser
posible establecer una sesión de juego humano vs máquina o máquina vs máquina, con una interfaz de consola sencilla.

### Consideraciones generales de juego

Cuando un humano juega Connect 4 intuitivamente trata de formar, filas, columnas y diagonales, un movimiento a la vez. Sin embargo, la pregunta de búsqueda detrás de este juego es, cuál es la secuencia de pasos que se deben efectuar para llegar a ganar?

Por ejemplo, uno de los elementos más importantes es evitar que el oponente gane. Identificar cuál es el movimiento que se debe ejecutar para bloquear ese gane, de ser posible, es clave.

De manera análoga, si el agente nada más necesita un movimiento más para ganar, debería detectarlo.
Aparte de las situaciones claras de bloqueo o gane, cómo sabe un agente qué movimiento ejecutar que, idealmente, lo acerque a un estado que sea más cercano a tener 4 fichas en fila?

Debería siempre tratar de hacer columnas? Siempre filas? Debería tratar de dejar espacios vacíos para engañar al oponente?



## 3. Algoritmo General de Juego

![Tablero imagen](/images/tablero.png)



## 4. Estructura del Algoritmo Genético


El algoritmo genético es el tipo de algoritmo de búsqueda y optimización para encontrar una solución a un problema utilizando los siguientes componentes:

- Secuencia: Se define como secuencia a la fila de fichas compuesta por 4 elementos, ya sean de un mismo símbolo, u otro distinto.

- Definición de población: Para crear la población se va a definir a los individuos,los cuales cada uno representa una solución potencial al problema.
Cada individuo va estar conformado por *4 fichas*, que pueden representar una secuencia en línea que puede determinar un ganador al problema.
Cada individuo se creará de forma aleatoria, según las fichas que se encuentren en el tablero.
En caso de no haber fichas sufientes en el tablero para completar un individuo o no existir fichas del todo, se procede a crear potenciales soluciones para el juego, y que después serán evaluadas para determinar su fitness function.

- Función objetivo (Fitness Function): Es la función que va a evaluar o devolver un valor objetivo que determina que tán óptimo es un individuo para una solución.

Para la definición de la función objetivo, se establecerá una cantidad de porcentaje de acuerdo a la cantidad de fichas deun símbolo establecido para dentro de la secuencia.
En caso de que no se hayan fichas en el tablero, se asignará un porcentaje de 100%, lo cual indica que se podrá insertar una ficha en cualquier columna.
- Cruce: Proceso por el cual se cruzan 2 individuos, con el fin de mejorar las características o genes de los mismos, y así adquirir un mejor valoor objetivo.

Para este proyecto se utilizará el método de cruce simple de un sólo punto, en este caso, haciendo el corte en la mitad de los arreglos o individuos padres.

- Mutación: Proceso por el cual se cambia un atributo del individuo, lo cual le da variabilidad en su valor objetivo.
Para este método se cambiará de forma aleatoria un atributo del individuo. Al final se retornará una población con individuos mutados.
- Selección: Método en el que se seleccionan a los individuos que posean un valor de función objetivo elevado.
Para la selección del algoritmo se elegirá una la cantidad de 7 individuos que tengan el mayor objetivo de fitness function, para que pasen a formar parte de la siguiente generación

## 5. Algoritmo de detección de situaciones de gane




## 6. Algoritmo genético para optimizar parámetros de estrategia


## 7. Interfaz Interactiva de Juego Interactivo con Humano y Máquina 


## Referencias Bibliográficas

- Algoritmos Genéticos en Python - YouTube. (s. f.). Recuperado 22 de noviembre de 2018, de https://www.youtube.com/watch?v=yAqq-IuDbrQ

- Kordsmeier, D. A. (s. f.). Using Genetic Learning in Weight-Based Game AI, 25.

- Morrow-DeBell-Final-4-15-2010.pdf. (s. f.). Recuperado de https://www.wittenberg.edu/sites/default/files/media/computer_science/forms/Morrow-DeBell-Final-4-15-2010.pdf?fbclid=IwAR3a_CsmDLvbpAMpfRwa4dv4yV5oH47ToYwuBCE-d6400UOWdyjVGjSPcGc



# Apéndice


## Manual de Instalación