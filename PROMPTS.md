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
P1: ¿Cómo puedo saber el tipo de un dato en Python?

P2: ¿Qué devuelve la función type()?

P3: ¿Cómo convierto ese tipo a string para retornarlo?

P4: Mostrame una implementación de tipo_de_dato(valor) -> str que devuelva el tipo como texto.

**Resultado obtenido**:
def tipo_de_dato(valor) -> str:

    return type(valor).__name__

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
P1: ¿Cómo aplico una función a cada elemento de una lista en Python?

P2: ¿Cuál es la forma más simple de hacerlo para un TP?

P3: ¿Conviene usar for, comprensión de listas o map() en este caso?

P4: Mostrame una implementación de aplicar_funcion(lista: list, func) -> list usando un enfoque simple y claro.

**Resultado obtenido**:
nuevaLista: list = []
for el in lista:
nuevaLista.append(func(el))  
 return nuevaLista
**¿Lo usaste tal cual o lo modificaste?**
La usé tal cual

---

### 7 - operaciones.py

**Herramienta**:
Chat GPT
**Prompt usado**:

>

1. Convertir el texto a minúsculas
2. Eliminar los espacios
3. Invertir el texto
4. Comparar el texto original con el invertido

Resultado esperado:

"Anita lava la tina" → True
"Hola mundo" → False
Resultado obtenido:

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
