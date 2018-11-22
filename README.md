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

Para la definición de la función objetivo, se establecerá una cantidad de porcentaje de acuerdo a la cantidad de elementos del mismo color que posea la secuencia.
- Cruce: Proceso por el cual se cruzan 2 individuos, con el fin de mejorar las características o genes de los mismos, y así adquirir un mejor valoor objetivo.

Para este proyecto se utilizará el método de cruce simple de un sólo punto, en este caso, haciendo el corte en la mitad de los arreglos o individuos padres.

- Mutación: Proceso por el cual se cambia un atributo del individuo, lo cual le da variabilidad en su valor objetivo.
Para este método se cambiará de forma aleatoria un atributo del individuo. Al final se retornará una población con indivuos mutados.
- Selección: Método en el que se seleccionan a los individuos que posean un valor de función objetivo elevado.
Para la selección del algoritmo se elegirá una la cantidad de 7 individuos que tengan el mayor objetivo de fitness function, para que pasen a formar parte de la siguiente generación

## 5. Algoritmo de detección de situaciones de gane


## 6. Algoritmo genético para optimizar parámetros de estrategia


## 7. Interfaz Interactiva de Juego Interactivo con Humano y Máquina 


## Referencias Bibliográficas


# Apéndice


## Manual de Instalación