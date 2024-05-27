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

## - Conjunciones y disyunciones -
**Conjunción** = Se puede implementar utilizando el operador coma (,). Entonces, dos predicados separados por coma se unen con la declaración AND.

**Ejemplo:**
Supongamos que tenemos un predicado, parent(jhon, bob) , que significa "Jhon es padre de Bob", y otro predicado, male(jhon) , que significa "Jhon es hombre". Entonces podemos hacer otro predicado que sea padre (jhon,bob) , que significa "Jhon es padre de Bob". Podemos definir el predicado padre cuando es padre Y es hombre.

**Disyunción** = Se puede implementar utilizando el operador de punto y coma (;). Entonces, dos predicados separados por punto y coma se unen con una declaración OR. 

**Ejemplo:**
upongamos que tenemos un predicado, padre(jhon, bob) . Este dice que “Jhon es padre de Bob”, y otro predicado, madre(lili,bob) , este dice que “lili es madre de bob”. Si creamos otro predicado como child() , esto será cierto cuando padre(jhon, bob) sea verdadero O madre(lili,bob) sea verdadero.

**Programa**

parent(jhon,bob).

parent(lili,bob).

male(jhon).

female(lili).

% Conjunction Logic

father(X,Y) :- parent(X,Y),male(X).

mother(X,Y) :- parent(X,Y),female(X).

% Disjunction Logic

child_of(X,Y) :- father(X,Y);mother(X,Y).


**Producción**
| ?- [conj_disj].

compiling D:/TP Prolog/Sample_Codes/conj_disj.pl for byte code...
D:/TP Prolog/Sample_Codes/conj_disj.pl compiled, 11 lines read - 1513 bytes written, 24 ms

yes

| ?- father(jhon,bob).

yes

| ?- child_of(jhon,bob).

true ?

yes

| ?- child_of(lili,bob).

yes

| ?-

## - Listas -
**Listas** = Es una**estructura de datos simple que se usa ampliamente en programación no numérica.** La lista consta de cualquier número de elementos, por ejemplo, rojo, verde, azul, blanco y oscuro. Se representará como [rojo, verde, azul, blanco, oscuro]. La lista de elementos irá entre corchetes. Una lista puede estar vacía o no vacía.

### Operaciones básicas en listas
**Operaciones	y su Definición:**
1. Comprobación de membresía: *Durante esta operación, podemos verificar si un elemento eterminado es miembro de una lista especificada o no.*
2. Cálculo de longitud: *Con esta operación podemos encontrar la longitud de una lista.*
3. Concatenación: *La concatenación es una operación que se utiliza para unir/agregar dos listas.*
4. Eliminar objetos: *Esta operación elimina el elemento especificado de una lista.*
5. Agregar elementos: *La operación de agregar agrega una lista a otra (como un elemento).*
6. Insertar elementos: *Esta operación inserta un elemento determinado en una lista.*

**Operaciones de reposicionamiento y su Definición:**
1. Permutación: *Esta operación cambiará las posiciones de los elementos de la lista y generará todos los resultados posibles.*
2. Artículos inversos: *Esta operación organiza los elementos de una lista en orden inverso.*
3. Elementos de turno: *Esta operación desplazará un elemento de una lista hacia la izquierda de forma rotatoria.*
4. Encargar artículos: *Esta operación verifica si la lista dada está ordenada o no.*

**Operaciones varias	Definición:**
1. Hallazgo de longitudes pares e impares: *Verifica si la lista tiene un número par o impar de elementos.*
2. Dividir: *Divide una lista en dos listas, y estas listas tienen aproximadamente la misma longitud.*
3. máx.: *Recupera el elemento con valor máximo de la lista dada.*
4. Suma: *Devuelve la suma de elementos de la lista dada.*
5. Combinar ordenar: *Organiza los elementos de una lista determinada en orden (utilizando el algoritmo Merge Sort).*

## - Recursión y Estructuras -
**Recursividad** = Es una técnica en la que un predicado se utiliza a sí mismo (puede ser con otros predicados) para encontrar el valor de verdad.

**Estructuras** = Son objetos de datos que contienen múltiples componentes.

**Coincidencia** = Se utiliza para comprobar si dos términos dados son iguales (idénticos) o si las variables en ambos términos pueden tener los mismos objetos después de crear una instancia.

## - Retroceso -
**Retroceso** = Es un procedimiento en el que el prólogo busca el valor de verdad de diferentes predicados comprobando si son correctos o no. El término retroceso es bastante común en el diseño de algoritmos y en diferentes entornos de programación.

### ¿Cómo funciona el retroceso?
**Nota** : mientras ejecutamos algún código de prólogo, durante el retroceso puede haber varias respuestas, podemos presionar punto y coma (;) para obtener las siguientes respuestas una por una, lo que ayuda a retroceder. De lo contrario, cuando obtengamos un resultado, se detendrá.

### Prevenir el retroceso
A veces escribimos los mismos predicados más de una vez cuando nuestro programa lo exige, por ejemplo para escribir reglas recursivas o para realizar algunos sistemas de toma de decisiones. En tales casos, el retroceso incontrolado puede causar ineficiencia en un programa. Para resolver esto, se usa `cut` en Prolog.

## - Diferente o no -
El predicado diferente comprobará si dos argumentos dados son iguales o no. **Si son iguales, devolverá falso**; de lo contrario, devolverá verdadero. El predicado `not` se usa para negar alguna afirmación, lo que significa que, **cuando una afirmación es verdadera, entonces not(declaración) será falsa**; de lo contrario, si la afirmación es falsa, entonces not(declaración) será verdadera.

La relación not es muy útil en diferentes casos. También en nuestros lenguajes de programación tradicionales utilizamos la operación lógica not para negar alguna declaración. Entonces **significa que cuando una afirmación es verdadera, entonces no (declaración) será falsa; de lo contrario, si la afirmación es falsa, entonces no (declaración) será verdadera**.

## - Entradas y Salidas -
### El predicado write()
Para escribir la salida podemos usar el predicado `write()`. Este predicado **toma el parámetro como entrada y escribe el contenido en la consola de forma predeterminada**. `write()` también puede escribir en archivos. 

**Programa**

| ?- write(56).

56

yes

| ?- write('hello').

hello

yes

| ?- write('hello'),nl,write('world').

hello

world

yes

| ?- write("ABCDE")

.

[65,66,67,68,69]

yes

### El predicado read()
El predicado `read()` se utiliza para leer desde la consola. El usuario puede escribir algo en la consola, que puede tomarse como entrada y procesarlo. `read()` **se usa generalmente para leer desde la consola, pero también se puede usar para leer desde archivos**.

**Programa**
cube :-

   write('Write a number: '),

   read(Number),

   process(Number).

process(stop) :- !.

process(Number) :-

   C is Number * Number * Number,

   write('Cube of '),write(Number),write(': '),write(C),nl, cube.

### El predicado tab()
El `tab()` es un **predicado adicional que se puede usar para poner algunos espacios en blanco mientras escribimos algo**. Entonces toma un número como argumento e imprime esa cantidad de espacios en blanco.

**Programa**

| ?- write('hello'),tab(15),write('world').

hello          world

yes

| ?- write('We'),tab(5),write('will'),tab(5),write('use'),tab(5),write('tabs').

We    will  use   tabs

yes

| ?-

### El predicado tell()
Este predicado `tell()` **toma el nombre del archivo como argumento**. Si ese archivo no está presente, cree un archivo nuevo y escriba en él. Ese archivo se abrirá hasta que escribamos el comando dicho . Podemos abrir más de un archivo usando `tell()`. Cuando se llame, se cerrarán todos los archivos.

### El predicado see()
**Cuando queremos leer desde un archivo, no desde el teclado, tenemos que cambiar el flujo de entrada actual**. Entonces podemos usar el predicado `see()`. Esto tomará el nombre del archivo como entrada. Cuando se complete la operación de lectura, usaremos el comando visto. 

**Producción**

| ?- see('sample_predicate.txt'),

read(X),

read(Y),

seen,

read(Z).

the_end.

X = end_of_file

Y = end_of_file

Z = the_end

yes

| ?-

### Los predicados put(C) y put_char(C)
Podemos usar `put(C)` **para escribir un carácter a la vez en el flujo de salida actual**. El flujo de salida puede ser un archivo o la consola. Esta C puede ser un carácter o un código ASCII en otra versión de Prolog como SWI prolog, pero en GNU prolog solo admite el valor ASCII. Para usar el carácter en lugar de ASCII, podemos usar `put_char(C)`.

### Los predicados get_char(C) y get_code(C)
Para leer un solo carácter del flujo de entrada actual, podemos usar el predicado `get_char(C)`. Esto tomará el personaje. si queremos el código ASCII, podemos usar `get_code(C)`.

## - Predicados integrados -
Hay tres tipos de predicados integrados, como se indica a continuación:
1. Identificar términos
2. Estructuras en descomposición
3. Recopilando todas las soluciones

### Identificar términos
**Predicado y su Descripción:**
var(X): *tiene éxito si X es actualmente una variable sin instancias.*
nueva(X): *tiene éxito si X no es una variable o ya se ha creado una instancia.*
átomo(X): *es cierto si X actualmente representa un átomo.*
número(X): *es cierto si X actualmente representa un número.*
entero(X): *es cierto si X actualmente representa un número entero.*
flotador(X): *es cierto si X actualmente representa un número real.*
atómico(X): *es cierto si X actualmente representa un número o un átomo.*
compuesto(X): *es cierto si X actualmente representa una estructura.*
tierra(X): *tiene éxito si X no contiene ninguna variable no instanciada.*

### Predicados matemáticos
**Predicado y su Descripción:**
aleatorio(L,H,X): *Obtener valor aleatorio entre L y H.*
entre(L,H,X): *Obtener todos los valores entre L y H.*
éxito(X,Y): *Suma 1 y asígnalo a X.*
abs(X): *Obtener el valor absoluto de X.*
máx(X,Y): *Obtener el valor más grande entre X e Y.*
mín(X,Y): *Obtener el valor más pequeño entre X e Y.*
redondo(X): *Redondear un valor cercano a X.*
truncar(X): *Convierta flotante a entero, elimine la parte fraccionaria.*
piso(X): *Redondear a la baja.*
techo(X): *Redondeo.*
raíz cuadrada (X): *Raíz cuadrada.*

## - Estructura de datos de árbol (estudio de caso) -
Supongamos que tenemos un árbol como se muestra a continuación:
![Arbol](https://www.tutorialspoint.com/prolog/images/tree_data_structure.jpg)

Tenemos que implementar este árbol usando prolog. Tenemos algunas operaciones de la siguiente manera:

- op(500, xfx, 'is_parent').
- op(500, xfx, 'es_hermano_de').
- op(500, xfx, 'está_en_el_mismo_nivel').
- Y otro predicado es leaf_node(Node)

En estos operadores, ha visto algunos parámetros como `(500, xfx, <nombre_operador>)`. El primer argumento (aquí 500) es la prioridad de ese operador. 'xfx' indica que se trata de un operador binario y `<operator_name>` es el nombre del operador.

Estos operadores se pueden utilizar para definir la base de datos del árbol. Podemos usar estos operadores de la siguiente manera:

- **a `es_parent b`, o `is_parent(a, b)`**. Entonces esto indica que el nodo a es el padre del nodo b.
- **X `es_hermano_de Y` o `es_hermano_de(X,Y)`**. Esto indica que X es hermano del nodo Y. Entonces, la regla es que si otro nodo Z es padre de X y Z también es padre de Y y X e Y son diferentes, entonces X e Y son hermanos.
- **`leaf_node(Nodo)`**. Se dice que un nodo (Nodo) es un nodo hoja cuando un nodo no tiene hijos.
- **`X está_en_el_mismo_nivel Y`, o `está_en_el_mismo_nivel(X,Y)`**. Esto comprobará si X e Y están al mismo nivel o no. Entonces, la condición es que cuando X e Y son iguales, entonces devuelve verdadero; de lo contrario, W es el padre de X, Z es el padre de Y y W y Z están en el mismo nivel.

**Programa**

/* The tree database */

:- op(500,xfx,'is_parent').

a is_parent b. c is_parent g. f is_parent l. j is_parent q.

a is_parent c. c is_parent h. f is_parent m. j is_parent r.

a is_parent d. c is_parent i. h is_parent n. j is_parent s.

b is_parent e. d is_parent j. i is_parent o. m is_parent t.

b is_parent f. e is_parent k. i is_parent p. n is_parent u.

n 
is_parent v.

/* X and Y are siblings i.e. child from the same parent */

:- op(500,xfx,'is_sibling_of').

X is_sibling_of Y :- Z is_parent X,

                     Z is_parent Y,

                     X \== Y.

leaf_node(Node) :- \+ is_parent(Node,Child). % Node grounded

/* X and Y are on the same level in the tree. */

:-op(500,xfx,'is_at_same_level').

X is_at_same_level X .

X is_at_same_level Y :- W is_parent X,

                        Z is_parent Y,

                        W is_at_same_level Z.