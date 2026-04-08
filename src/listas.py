# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma

    pass


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    pares : list = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares
    pass


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    listaInvertida = []
    for i in range(len(lista) - 1, -1, -1):
        listaInvertida.append(lista[i])
    return listaInvertida


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    sinDuplicados : list = []

    for el in lista:
        if(sinDuplicados.__contains__(el)):
            continue
        sinDuplicados.append(el)
    
    return sinDuplicados
    pass


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    listaAplanada : list = []

    for listaActual in lista:
        for valor in listaActual:
            listaAplanada.append(valor)
    
    return listaAplanada
    pass
