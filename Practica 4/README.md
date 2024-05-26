# Tutorial de Prolog

## Información del la Práctica
**Nombre:** Teresa Rivas Gómez  
**Matrícula:** 372565  
**Materia:** Paradigmas de la Programación  
**Programa:** Práctica 4 
**Fecha de Inicio:** 25/05/2024  
**Fecha de Final:** 25/05/2024  

## - Introducción -
**Prolog** = Forma abreviada de *Programación Lógica*.

### ¿Qué es?
La programación lógica es **uno de los paradigmas de programación informática**, en el que las declaraciones del programa expresan los hechos y reglas sobre diferentes problemas dentro de un sistema de lógica formal. 

### Lenguajes que lo implementan:
1. ALF (lenguaje de programación funcional de lógica algebraica).
2. ASP (Programación del conjunto de respuestas)
3. ciclo
4. Registro de datos
5. FuzzyCLIPS
6. Jano
7. Parlogar
8. Prólogo
9. Prólogo++
10. ROPA

### Diferencias entre la programación lógica y los lenguajes de programación funcionales

![Diferencias](https://www.tutorialspoint.com/prolog/images/logic_functional_programming.jpg)
"En programación funcional, tenemos que mencionar cómo se puede resolver un problema, pero en programación lógica tenemos que especificar para qué problema realmente queremos la solución."

### Programación funcional VS Programación lógica
**Programación funcional:**
1. La programación funcional sigue la arquitectura de Von-Neumann o utiliza pasos secuenciales.
2. La sintaxis es en realidad la secuencia de declaraciones como (a, s, I).
3. El cálculo se realiza ejecutando las declaraciones de forma secuencial.
4. La lógica y los controles se mezclan.

**Programación lógica:**
1. La programación lógica utiliza modelos abstractos o trata con objetos y sus relaciones.
2. La sintaxis es básicamente la fórmula lógica (Cláusulas de Horn).
3. Se calcula restando las cláusulas.
4. La lógica y los controles se pueden separar.

### Prólogo
**Prógolo** = La gramática Prolog o *PRO en LOG ics* es un lenguaje de programación lógico y declarativo.

## - Configuración del entorno -
### Página web oficial
Este es el sitio web oficial de GNU Prolog donde podemos ver todos los detalles necesarios sobre GNU Prolog y también obtener el enlace de descarga.
http://www.gprolog.org/
### Enlace de descarga directa
A continuación se muestran los enlaces de descarga directa de GNU Prolog para Windows. Para otros sistemas operativos como Mac o Linux, puede obtener los enlaces de descarga visitando el sitio web oficial (el enlace se proporciona arriba):
http://www.gprolog.org/#download (sistema de 32 bits)
### Guía de instalación
https://www.tutorialspoint.com/prolog/prolog_environment_setup.htm

## - Hola mundo -
Después de ejecutar el prólogo de GNU, **podemos escribir el programa hola mundo directamente desde la consola**. Para hacerlo, debemos escribir el comando de la siguiente manera:
`write('Hello World').`
Y el resultado se mostraría así: ![Hola Mundo](https://www.tutorialspoint.com/prolog/images/hello_world.jpg)

## - Conceptos básicos -
**Base de conocimientos** = Una de las partes fundamentales de la programación lógica.

**Hechos, reglas y consultas** = Componentes básicos de la programación lógica.

**Hechos** = Relación explícita entre objetos y las propiedades que estos objetos podrían tener.

**Normas** = Podemos definir la regla como una relación implícita entre objetos.

**Consultas** = Algunas preguntas sobre las relaciones entre objetos y propiedades de los objetos.

### Base de conocimientos en programación lógica
Hay tres componentes principales en la programación lógica: hechos, reglas y consultas . Entre estos tres, si recopilamos los hechos y las reglas en su conjunto, se forma una base de conocimientos . Entonces podemos decir que la base de conocimientos es una colección de hechos y reglas .

**Base de conocimientos 1**:

Supongamos que tenemos algún conocimiento de que Teresa, Andrea y Laura son tres niñas, y entre ellas, Priya sabe cocinar. Intentemos escribir estos hechos de una manera más genérica como se muestra a continuación:
`girl(teresa).`
`girl(andrea).`
`girl(laura).`
`can_cook(teresa).`

**Producción**:

GNU Prolog 1.4.5 (64 bits)
Compiled Jul 14 2018, 13:19:42 with x86_64-w64-mingw32-gcc
By Daniel Diaz
Copyright (C) 1999-2018 Daniel Diaz
| ?- change_directory('D:/TP Prolog/Sample_Codes').

yes
| ?- [kb1]
.
compiling D:/TP Prolog/Sample_Codes/kb1.pl for byte code...
D:/TP Prolog/Sample_Codes/kb1.pl compiled, 3 lines read - 489 bytes written, 10 ms

yes
| ?- girl(teresa)
.

yes
| ?- girl(andrea).

no
| ?- can_cook(teresa).

yes
| ?- can_cook(laura).

no
| ?-

## - Relaciones -
**Relación** = Es una de las características principales que debemos mencionar adecuadamente en Prolog. Estas relaciones pueden expresarse como hechos y reglas.

Hay varios tipos de relaciones, algunas de las cuales también pueden ser reglas. Una regla puede descubrir una relación incluso si la relación no está definida explícitamente como un hecho.

**Relación Familiar**

![Relacion Familiar](https://www.tutorialspoint.com/prolog/images/family_relationship.jpg)

**Predicados:**

padre (pam, bob).

padre (tom, bob).

padre (tom, liz).

padre (bob, ann).

padre (bob, palmadita).

padre (pat, jim).

padre (bob, peter).

padre (peter, jim).

Algunos datos **se pueden escribir de dos maneras diferentes, como el sexo de los miembros de la familia**, que se puede escribir en cualquiera de las formas:

mujer (pam).

macho(tom).

macho (bobo).

mujer (liz).

hembra(palmadita).

mujer (ana).

hombre(jim).

**O en el siguiente formulario:**

sexo( pam, femenino).

sexo( tom, masculino).

sexo( bob, masculino).

… etcétera.

## - Objeto de Datos -
![Objeto de datos](https://www.tutorialspoint.com/prolog/images/data_objects.jpg)

### Átomos y variables en Prolog
**Átomos** = Son una variación de las constantes.

azahar

b59

b_59

b_59AB

b_x25

antara_sarkar

<--->

=======>

...

.:.

::=

'Rubai'

'Arindam_Chatterjee'

'Sumit Mitra'

### Variables anónimas en Prolog
Las variables anónimas no tienen nombre. **Las variables anónimas en el prólogo se escriben con un único carácter de subrayado '_'**. Y una cosa importante es que cada variable anónima individual se trata como diferente . No son iguales.

## - Operadores -
Los ***operadores de comparación*** se utilizan para comparar dos ecuaciones o estados. A continuación se muestran diferentes operadores de comparación:

**Operador**
X > Y	

X<Y	

X >= Y	

X=<Y	

X =:= Y	

X =\= Y	


**Significado**

X es mayor que Y

X es menor que Y

X es mayor o igual que Y

X es menor o igual que Y

los valores de X e Y son iguales

los valores de X e Y no son iguales

Los ***operadores aritméticos*** se utilizan para realizar operaciones aritméticas. Existen algunos tipos diferentes de operadores aritméticos de la siguiente manera:

**Operador**	

"+"

"-"

"*"

"/"	

"**"	

"//"	

modificación	


**Significado**

Suma

Sustracción

Multiplicación

División

Fuerza

División entera

Módulo

## - Bucle y toma de decisiones -
**Declaraciones de Bucle** = Se utilizan para ejecutar el bloque de código varias veces.

**Programa**

count_to_10(10) :- write(10),nl.

count_to_10(X) :-

   write(X),nl,

   Y is X + 1,

   count_to_10(Y).


**Producción**

| ?- [loop].

compiling D:/TP Prolog/Sample_Codes/loop.pl for byte code...
D:/TP Prolog/Sample_Codes/loop.pl compiled, 4 lines read - 751 bytes written, 16 ms

(16 ms) yes

| ?- count_to_10(3).

3

4

5

6

7

8

9

10


true ?

yes

| ?-

Ahora crea un bucle que tome los valores más bajo y más alto. Entonces, podemos usar Between() para simular bucles.

**Toma de decisiones** = Las declaraciones de decisión son declaraciones **If-Then-Else**. Entonces, cuando intentamos cumplir alguna condición y realizar alguna tarea, utilizamos las declaraciones de toma de decisiones.

`If <condition> is true, Then <do this>, Else`

**Programa**

% If-Then-Else statement

gt(X,Y) :- X >= Y,write('X is greater or equal').

gt(X,Y) :- X < Y,write('X is smaller').


% If-Elif-Else statement

gte(X,Y) :- X > Y,write('X is greater').

gte(X,Y) :- X =:= Y,write('X and Y are same').

gte(X,Y) :- X < Y,write('X is smaller').

**Producción**

| ?- [test].

compiling D:/TP Prolog/Sample_Codes/test.pl for byte code...
D:/TP Prolog/Sample_Codes/test.pl compiled, 3 lines read - 529 bytes written, 15 ms

yes

| ?- gt(10,100).

X is smaller

yes

| ?- gt(150,100).

X is greater or equal

true ?

yes

| ?- gte(10,20).

X is smaller

(15 ms) yes

| ?- gte(100,20).

X is greater

true ?

yes

| ?- gte(100,100).

X and Y are same

true ?

yes

| ?-