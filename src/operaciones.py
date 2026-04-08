# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split()
    resultado = []

    for palabra in palabras:
        resultado.append(palabra.capitalize())

    return " ".join(resultado)
    pass


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    texto = texto.lower()
    vocales = "aeiou"
    contador = 0

    for letra in texto:
        if letra in vocales:
            contador += 1

    return contador
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            nueva = (ord(char) - base + desplazamiento) % 26
            resultado += chr(base + nueva)
        else:
            resultado += char
    pass
