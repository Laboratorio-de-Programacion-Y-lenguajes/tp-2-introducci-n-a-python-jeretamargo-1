# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**:
Copilot
**Prompt usado**:
P1: Como puedo crear un saludo personalizado en Python
P2: Como concateno string en Python?
P3: Mostrame una implementacion de una funcion crear*saludo(nombre: str) -> str que devuelva el string "Hola, \_nombre*!"

**Resultado obtenido**:
def crear_saludo(nombre: str) -> str:

    return f"Hola, {nombre}!"

**¿Lo usaste tal cual o lo modificaste?**
Modifique el string del mensaje de error

---

### 2 - condicionales.py

**Herramienta**:
Chat GPT
**Prompt usado**:
P1: ¿Cómo se determina si un año es bisiesto?

P2: ¿Qué condiciones matemáticas se deben cumplir (divisible por 4, 100 y 400)?

P3: ¿Cómo implemento esas condiciones en Python usando if?

P4: Mostrame una implementación de es_bisiesto(anio: int) -> bool siguiendo esas reglas.

> **Resultado obtenido**:
> def es_bisiesto(anio: int) -> bool:

    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 4 == 0 and anio % 400 == 0)

## **¿Lo usaste tal cual o lo modificaste?**

Usé Tal cual

### 3 - listas.py

**Herramienta**:
Copilot
**Prompt usado**:

> P1: ¿Cómo puedo invertir una lista en Python?

P2: ¿Qué opciones existen para hacerlo (slicing, reverse(), loop)?

P3: ¿Cuál es la forma más simple y clara para un TP?

P4: Mostrame una implementación de invertir_lista(lista: list) -> list usando un método simple.

**Resultado obtenido**:
def invertir_lista(lista: list) -> list:

    listaInvertida = []
    for i in range(len(lista) - 1, -1, -1):
        listaInvertida.append(lista[i])
    return listaInvertida

**¿Lo usaste tal cual o lo modificaste?**
use tal cual

---

### 4 - diccionarios.py

**Herramienta**:
Chat GPT
**Prompt usado**:

> Generá ejemplos de textos y contá la frecuencia de palabras ignorando mayúsculas.
> Mostrá el texto y el diccionario resultante.
> Luego extraé una regla general.

Generá ejemplos de textos y contá la frecuencia de palabras ignorando mayúsculas.
Mostrá el texto y el diccionario resultante.
Luego extraé una regla general.

Ejemplos:

"hola mundo hola" → {"hola": 2, "mundo": 1}  
"Python python PYTHON" → {"python": 3}

Regla general:

- Convertir a minúsculas
- Separar palabras
- Recorrerlas
- Contarlas en un diccionario

**Resultado obtenido**:

resultado = {}
palabras = texto.lower().split()

    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1

    return resultado

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual

---

### 5 - loops.py

**Herramienta**:
Chat GPT
**Prompt usado**:

> P1: ¿Cómo genero una lista de números del 1 al n en Python?
> P2: ¿Cómo hago para incluir el n en el resultado?
> P3: ¿Qué debería devolver si n es 0 o negativo?
> P4: Mostrame una implementación de contar_hasta(n: int) -> list que devuelva [] si n <= 0.
> **Resultado obtenido**:
> if n <= 0:

        return []

    resultado = []
    for i in range(1, n + 1):
        resultado.append(i)

    return resultado

**¿Lo usaste tal cual o lo modificaste?**
use tal cual

---

### 6 - funciones.py

**Herramienta**:
Copilot
**Prompt usado**:
P1: ¿Para que sirve la funcion functools.reduce?
P2: ¿Como puedo aplicar una funcion acumulativamente a una lista?
P3: Para que me sirve la variable inicial en una funcion de reduccion de listas?
P4: Mostrame una implementacion del metodo def reducir(lista: list, func, inicial): , que aplica func acumulativamente a los elementos de lista,
comenzando con inicial.
Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
SIN USAR functools.reduce

**Resultado obtenido**:
def reducir(lista: list, func, inicial):

    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
    pass

**¿Lo usaste tal cual o lo modificaste?**
La usé tal cual

---

### 7 - operaciones.py

**Herramienta**:
Chat GPT
**Prompt usado**:

>

P1: ¿Que es el cifrado Cesar?
P2:¿Cual es la manera en la que el cifrado Cesar funciona?
P3:Hay un limite en el valor de despalzamiento pasado por parametro en una funcion que cifre en Cesar?
P4: Mostrame una implementacion del cifrado cesar en Python def caesar_cipher(texto: str, desplazamiento: int) -> str: que solo desplace caracteres (a-z, A-Z), los demás caracteres no cambian. no utilices ninguna libreria externa

**Resultado obtenido**:
def caesar_cipher(texto: str, desplazamiento: int) -> str:

    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            nueva = (ord(char) - base + desplazamiento) % 26
            resultado += chr(base + nueva)
        else:
            resultado += char

    return resultado

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
  Para realizar un correcto prompting hay que brindarle una buena base de fundamentos y contexto a la IA sobre tu problema a resolver
- ¿En qué casos la IA fue útil y en cuáles no?
  Mediante un buen prompting pude resolver muchos de los ejercicios, aunque en algunos no pude hayar la solucion junto a la ia, tal vez por falta de entendimiento del ejercicio.
- ¿Qué harías diferente la próxima vez?
  Investigaria más acerca de los ejercicios a realizar para entender bien cual es y como es el se consigue resultado que debo obtener
