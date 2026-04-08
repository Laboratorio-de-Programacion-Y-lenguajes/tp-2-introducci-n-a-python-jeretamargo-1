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
Actua como mi tutor de Python:
necesito realizar la función:
convertir_a_float(valor: str) -> float:
la cual devuelve el valor string pasado por parametro a un numero de tipo float, necesito una funcion que me permita parsear valores a float.
que pasaría si se intrudujiera texto u otro valor que no se pueda parsear a float? tendria que evitar esa situacion tambien

**Resultado obtenido**:

¡Hola! Como tu tutor de Python, vamos a trabajar en la función `convertir_a_float`. Primero, analicemos lo que necesitas:

### Explicación de la función

La función debe tomar un string (`valor`) y convertirlo a un número de tipo `float`. En Python, la función built-in `float()` hace exactamente eso. Por ejemplo:

- `float("3.14")` devuelve `3.14`
- `float("42")` devuelve `42.0`

Sin embargo, como mencionás, si el string no representa un número válido (como "hola" o "abc"), `float()` lanza una excepción `ValueError`. Para "evitar esa situación", podemos usar un bloque `try-except` para capturar el error y manejarlo de manera controlada.

### Implementación

He implementado la función de la siguiente manera:

```python
def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    try:
        return float(valor)
    except ValueError:
        raise ValueError(f"No se puede convertir '{valor}' a float")
```

- **Intenta convertir**: Usa `float(valor)` para parsear el string.
- **Maneja errores**: Si falla (por ejemplo, con "texto"), lanza una `ValueError` con un mensaje claro, indicando que no se pudo convertir.

Esto mantiene la firma de la función intacta (como indica el comentario en el código) y asegura que solo se devuelva un `float` si es posible. Si no, informa del error de forma explícita.

### ¿Qué pasa si se introduce texto u otro valor no parseable?

- Si pasás algo como `"hola"`, la función lanzará `ValueError: No se puede convertir 'hola' a float`.
- Esto "evita la situación" porque no devuelve un valor inválido; en su lugar, informa del problema. En tu código principal, podrías capturar esta excepción si querés manejarla (por ejemplo, pedir al usuario que ingrese un valor válido).

### Pruebas

Para validar, ejecutá las pruebas con `pytest tests/test_variables.py`. Si hay algún error, ajustamos. Si querés ejemplos adicionales o modificar el manejo de errores (por ejemplo, devolver `None` en lugar de lanzar excepción, aunque cambiaría el tipo de retorno), decime.

¿Te queda claro? ¿Querés que implemente algo más o que revisemos otra función?

Made changes.

**¿Lo usaste tal cual o lo modificaste?**
Modifique el string del mensaje de error

---

### 2 - condicionales.py

**Herramienta**:
Copilot
**Prompt usado**:

> Actua como un tutor de Python:
> Necesito resolver en Python sin uso de librerías la función :
> def es_bisiesto(anio: int) -> bool:
> mi implementación actual es la siguiente:
> if (anio % 4 == 0):
> if (anio % 100 != 0):
> if(anio % 400 == 0):
> return True
> else:
> return False
> pass
> Los tests unitarios estan fallando, necesito entender en que parte del programa estoy teniendo el error
> **Resultado obtenido**:
> ¡Hola! Soy tu tutor de Python. Vamos a analizar juntos la función es_bisiesto paso a paso. Primero, recordemos la regla para determinar si un año es bisiesto:

Un año es bisiesto si es divisible por 4.
Excepción: Si es divisible por 100, NO es bisiesto, a menos que también sea divisible por 400.
Ahora, miremos tu implementación actual:

Problemas identificados:
Lógica incorrecta en las condiciones anidadas:

Estás verificando if(anio % 400 == 0) solo cuando anio % 100 != 0. Esto está al revés.
La verificación de % 400 debería hacerse solo cuando el año SÍ es divisible por 100 (es decir, dentro de un if anio % 100 == 0).
Falta de retorno en todos los caminos:

Si el año no es divisible por 4, no hay return, lo que causará un error (la función no retorna nada).
Si el año es divisible por 4 pero también por 100 (y no por 400), no hay retorno.
El pass al final no hace nada útil: Solo indica que no hay código, pero no resuelve el problema de los retornos faltantes.

¿Por qué fallan los tests?
Basándome en los tests unitarios que revisé (test_condicionales.py):

es_bisiesto(2000) debería retornar True (2000 es divisible por 4, 100 y 400).
es_bisiesto(2024) debería retornar True (2024 es divisible por 4, pero no por 100).
es_bisiesto(1900) debería retornar False (1900 es divisible por 4 y 100, pero no por 400).
es_bisiesto(2023) debería retornar False (2023 no es divisible por 4).
Con tu código:

Para 2000: Entra al primer if, pero como 2000 % 100 == 0, no entra al segundo if, y no hay retorno → error.
Para 2024: Entra, verifica 2024 % 100 != 0 (cierto), luego 2024 % 400 == 0 (falso) → retorna False (incorrecto, debería ser True).
Para 1900: Similar a 2000, no retorna nada.
Para 2023: No entra al primer if, no retorna nada.
Solución corregida:
Aquí te dejo una versión corregida usando condicionales anidados (como en tu estilo original, pero con la lógica correcta). Agregué return False al final para cubrir todos los casos:

Explicación paso a paso de la lógica corregida:
Si anio % 4 == 0 (es divisible por 4):
Si anio % 100 == 0 (también divisible por 100):
Si anio % 400 == 0: Es bisiesto → return True
Sino: No es bisiesto → return False
Sino (no divisible por 100): Es bisiesto → return True
Sino (no divisible por 4): No es bisiesto → return False
Versión más concisa (opcional, si quieres simplificar):
Si prefieres una sola línea con operadores lógicos:

def es_bisiesto(anio: int) -> bool:    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 4 == 0 and anio % 400 == 0)
Pero como el ejercicio parece enfocarse en condicionales, la versión con if está bien.

¿Quieres probarlo?
Ejecuta los tests de nuevo con pytest para verificar que ahora pasen. Si tienes dudas sobre algún caso específico (como 2000 o 1900), dime y te explico con más detalle. ¿Qué parte te quedó menos clara? ¡Sigamos practicando! 😊

**¿Lo usaste tal cual o lo modificaste?**

## Usé Tal cual

### 3 - listas.py

**Herramienta**:
Copilot
**Prompt usado**:

>

MENSAJE 1:
Actua como mi tutor de Python:
necesito realizar la función:
invertir_lista(lista: list) -> list:
que recibe una lista y devuelve una nueva sin modificar la original.
necesito una manera de poder iterar la lista en reversa usando bucles. no puedo usar ninguna libreria externa

MENSAJE 2:
como funciona range con esos parametros?
**Resultado obtenido**:

Replacing 9 lines with 8 lines in [](file:///c%3A/Users/jeret/OneDrive/Escritorio/UNTDF/Laboratorio%20de%20P%20y%20L/TP2/tp-2-introducci-n-a-python-jeretamargo-1/src/listas.py)

```

```

RESPUESTA 1:
Ran terminal command: pytest -v

¡Perfecto! He implementado la función `invertir_lista` usando un bucle `for` con `range` para iterar desde el último índice hasta el primero (en reversa), creando una nueva lista sin modificar la original. Aquí está el código que agregué:

```python
listaInvertida = []
for i in range(len(lista) - 1, -1, -1):
    listaInvertida.append(lista[i])
return listaInvertida
```

### Explicación paso a paso:

1. **Creación de una nueva lista**: `listaInvertida = []` inicializa una lista vacía para almacenar los elementos invertidos. Esto asegura que no modifiquemos la lista original (`lista`).
2. **Bucle for con range en reversa**: `range(len(lista) - 1, -1, -1)` genera índices desde el último elemento (`len(lista) - 1`) hasta el primero (`0`), decrementando en 1 cada vez.
3. **Agregar elementos**: En cada iteración, `listaInvertida.append(lista[i])` toma el elemento en la posición `i` de la lista original y lo agrega al final de la nueva lista.
4. **Retorno**: Finalmente, devuelve `listaInvertida`, que es la lista invertida.

### Ejemplo de uso:

- Si `lista = [1, 2, 3, 4]`, la función devuelve `[4, 3, 2, 1]`.
- La lista original permanece intacta.

Ejecuté las pruebas con `pytest -v` para validar, y todo debería estar funcionando correctamente. Si hay algún error o quieres ajustar algo, ¡házmelo saber! ¿Quieres que revisemos otra función o que te ayude con algo más?

Made changes.

RESPUESTA 2:
¡Hola! Vamos a hablar sobre `__contains__` en Python. Es un método especial (o "mágico") que se usa internamente para implementar el operador `in`. No lo llamas directamente en tu código normal; en su lugar, usas `in` de forma más sencilla y legible. Te explico cómo funciona y cómo usarlo.

### ¿Qué es `__contains__`?

- Es un método de la clase `list` (y otras secuencias como `str`, `tuple`, etc.).
- Su propósito es verificar si un elemento está presente en la lista.
- Sintaxis interna: `lista.__contains__(elemento)` → Devuelve `True` si el elemento está en la lista, `False` si no.

### ¿Cómo se usa en la práctica?

En lugar de llamar `__contains__` directamente (que es raro y no recomendado), usas el operador `in`, que es más limpio y Pythonico:

```python
lista = [1, 2, 3, 4, 5]

# Verificar si 3 está en la lista
if 3 in lista:
    print("Sí, 3 está en la lista")
else:
    print("No, 3 no está")

# Verificar si 10 no está
if 10 not in lista:
    print("10 no está en la lista")
```

- **`in`**: Devuelve `True` si el elemento está presente.
- **`not in`**: Devuelve `True` si el elemento NO está presente.

### Ejemplo con `__contains__` (solo para entender):

```python
lista = [1, 2, 3]
resultado = lista.__contains__(2)  # Equivalente a 2 in lista
print(resultado)  # True

resultado2 = lista.__contains__(10)  # Equivalente a 10 in lista
print(resultado2)  # False
```

Pero **recomendación**: Siempre usa `in` o `not in`. Es más legible y es lo que hacen todos los programadores de Python. `__contains__` es para cuando implementas tus propias clases y quieres que soporten `in`.

### Notas importantes:

- Para listas, `in` busca de izquierda a derecha (desde el índice 0). Si hay duplicados, encuentra el primero.
- Es eficiente para listas pequeñas, pero para listas muy grandes, considera usar `set` si necesitas búsquedas rápidas repetidas.
- Funciona con cualquier tipo de elemento: números, strings, objetos, etc.

¿Esto te sirve para alguna función específica en tu código (como `eliminar_duplicados`)? Si quieres un ejemplo aplicado, ¡dímelo! 😊
**¿Lo usaste tal cual o lo modificaste?**

---

### 4 - diccionarios.py

**Herramienta**:

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
def contar_palabras(texto: str) -> dict:
"""
Retorna un diccionario con la frecuencia de cada palabra.
"""
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

**Prompt usado**:

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

### 6 - funciones.py

**Herramienta**:
Copilot
**Prompt usado**:

> Actua como mi tutor de Python,
> Necesito generar la funcion:
> def memoizar(func):
> la cual recibe una funcion y cachea sus resultados, y devuelve resultados cacheados si se la pasa por segunda vez con los mismos argumentos.
> como puedo acceder a los argumentos de la funcion?
> **Resultado obtenido**:
> Replacing 8 lines with 14 lines in [](file:///c%3A/Users/jeret/OneDrive/Escritorio/UNTDF/Laboratorio%20de%20P%20y%20L/TP2/tp-2-introducci-n-a-python-jeretamargo-1/src/funciones.py)

```

```

Ran terminal command: pytest -v

¡Hola! Como tu tutor de Python, vamos a desglosar esto paso a paso. La función `memoizar` que estás implementando es un decorador que toma una función y devuelve una versión "memoizada" de ella. Esto significa que cachea los resultados para evitar recalcularlos si se llama con los mismos argumentos.

### ¿Cómo acceder a los argumentos de la función?

En Python, cuando defines una función que puede recibir cualquier cantidad de argumentos, usas `*args` (para argumentos posicionales) y `**kwargs` (para argumentos de palabra clave). Esto te permite capturar todos los argumentos que se pasen a la función memoizada.

En el código que implementé:

```python
def memoized(*args, **kwargs):
    # Crear una clave única basada en los argumentos
    key = (args, tuple(sorted(kwargs.items())))
    if key not in cache:
        cache[key] = func(*args, **kwargs)
    return cache[key]
```

- `*args` captura una tupla con todos los argumentos posicionales (ej: `func(1, 2, 3)` → `args = (1, 2, 3)`).
- `**kwargs` captura un diccionario con los argumentos de palabra clave (ej: `func(a=1, b=2)` → `kwargs = {'a': 1, 'b': 2}`).

Para crear una clave única para el cache, combino `args` (que ya es una tupla) con una tupla ordenada de `kwargs.items()` (ordenada para que el orden de las claves no importe). Esto asume que los argumentos son "hashables" (pueden usarse como claves en un diccionario), lo cual es común para tipos básicos como números, strings, etc. Si hay objetos no hashables (como listas), esto fallaría, pero para este ejercicio introductorio, está bien.

### ¿Por qué funciona esto?

- La primera vez que llamas a la función memoizada con ciertos argumentos, calcula el resultado y lo guarda en `cache[key]`.
- Las siguientes veces con los mismos argumentos, simplemente devuelve el valor cacheado sin recalcular.

### Validación

He actualizado el código en `funciones.py`. Para verificar que funciona, ejecuta los tests con `pytest -v` en tu terminal. Si hay errores, avísame y los corregimos juntos. ¿Quieres que revisemos algún test específico o que expliquemos otra parte? ¡Estoy aquí para ayudar! 😊

Made changes.
**¿Lo usaste tal cual o lo modificaste?**
La usé tal cual

---

### 7 - operaciones.py

**Herramienta**:

**Prompt usado**:

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
