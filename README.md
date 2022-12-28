# Yathzee

## **Indice**

- [**Yathzee**](#yathzee)
- [**Antes de empezar**](#antes-de-empezar)
  - [**Yatzy Refactoring Kata**](#yatzy-refactoring-kata)
  - [**Kata Description**](#kata-description)
- [**Normas, requisitos y puntuación**](#normas-requisitos-y-puntuación)
  - [**¿Qué hace falta?**](#¿qué-hace-falta)
  - [**Normas**](#normas)
  - [**Puntuación**](#puntuación)

## Antes de empezar

El codigo original no es de mi propiedad. Todos los derechos se otorgan a [**Emily Bache**](https://github.com/emilybache). Por favor, hagan click en el nombre para acceder a su perfil de Github.

Además, este es el repositorio original, el cual tiene varios ficheros para distintos lenguajes. Se recomienda informarse desde [aquí](https://github.com/emilybache/Yatzy-Refactoring-Kata).

Por último, esto es solo una refactorización del código original. Dicho código se accede desde el fichero originalCode.

### Yatzy Refactoring Kata

This Refactoring Kata was designed by Jon Jagger and is available in his Cyber-Dojo. See [his blog post](http://jonjagger.blogspot.co.uk/2012/05/yahtzee-cyber-dojo-refactoring-in-java.html)

I have changed it a little, so that the rules more closely match the original game.

If you like this Kata, you may be interested in [my books](https://leanpub.com/u/emilybache) and website [SammanCoaching.org](https://sammancoaching.org)

#### Kata Description

The problem that this code is designed to solve is explained here: [Yatzy](https://sammancoaching.org/kata_descriptions/yatzy.html)

## **Normas, requisitos y puntuación**

### ¿Qué hace falta?

- 5 dados
- Un tablero Yatzhee para anotar la puntuación obtenida

### Normas

Por turnos, cada jugador tira hasta 5 dados. De esos 5 dados, el jugador que tenga el turno decide cuantos dados quedarse. Los dados que el jugador bloquee o se quede no se vuelven a lanzar. Cada uno tiene hasta 3 tiradas como máximo.

El objetivo es buscar ciertas combinaciones de dados para ir sumando los puntos que vienen determinados en el apartado siguiente.

Además, el jugador no está obligado a gastar sus 3 tiradas. Si un jugador obtiene una combinación en su primera tirada, puede decidir si puntuar o no.

Por último, las puntuaciones solo pueden ser apuntadas una sola vez. Si el jugador saca una combinación ya bloqueada, si no le queda mas remedio, puede utilizar la casilla Chance.

### Puntuación

El tablero Yatzhee se divide en 2 secciones:

1. Upper Section

   - Aces: Suma todos los **ases** (1) que el jugador haya obtenido en sus tiradas
   - Twos: Suma todos los **doses** que el jugador haya sacado en sus tiradas
   - Threes: Suma todos los **treses** que el jugador haya obtenido en sus tiradas
   - Fours: Suma todos los **cuatros** que el jugador haya obtenido en sus tiradas
   - Fives: Suma todos los **cincos** que el jugador haya obtenido en sus tiradas
   - Sixes: Suma todos los **seis** que el jugador haya sacado en sus tiradas.
   - Total Score: Suma de las combinaciones de la parte superior
   - Bonus: Si el jugador ha obtenido una suma superior o igual a 63, se le sumará 35 puntos extras y se completará con un tick. En caso contrario, se omite el paso y se tacha
   - Total: Suma total del Upper Section, incluyendo el bonus

2. Lower Section
   - Pairs: Suma los numeros que componen la **pareja**
   - Double Pairs: Suma los numeros que compongan **las parejas**
   - 3 of a kind: Suma los numeros que componen el **trio** de dados
   - 4 of a kind: Suma los numeros que compongan el **cuarteto** de dados
   - Full House: Suma todos los dados si hay un **trio** y una **pareja**
   - Small Straight: Si hay una **secuencia consecutiva de 4 numeros**, se suman todos los dados obtenidos
   - Large Straight: Si hay una **secuencia consecutiva de 5 numeros**, se suman todos los dados obtenidos
   - YAHTZEE: Se suman 50 puntos si salen **5 dados con el mismo numero** _(4,4,4,4,4)_.
   - Chance: Se suman los dados **si no hay más oportunidad de poder puntuar las combinaciones que aparezcan**.
   - YAHTZEE BONUS: Si se obtiene un YAHTZEE, se añade un tick. Por cada tick, son 100 puntos extras
   - Total of Lower Section: Puntuación total de la parte inferior
   - Total of Upper Section: Puntuación total de la parte superior
   - Grand Total: Suma de todas las partes
