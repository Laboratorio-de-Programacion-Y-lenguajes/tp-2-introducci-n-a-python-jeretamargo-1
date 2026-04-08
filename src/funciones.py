# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    nuevaLista: list = []
    for el in lista:
      nuevaLista.append(func(el))  
    return nuevaLista
    pass


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    def componer2(x):
        x = g(x)
        x = f(x)
        return x

    return componer2
    pass


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}
    def memorizado(*args, **kwargs):
        # Crear una clave única basada en los argumentos
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memorizado
    pass


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
    pass