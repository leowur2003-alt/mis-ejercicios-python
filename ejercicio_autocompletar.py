# crear un lista con los cuadrados de los n primeros numeros naturales
def cuadrados(n:int) -> list[int]:
    return [i**2 for i in range(1, n+1)]

# crear una funcion que devuelva la suma de los cuadrados de los n primeros numeros naturales
def suma_cuadrados(n:int) -> int:
    return sum(cuadrados(n + 1))

# crear una funcion que devuelva la suma de los cuadrados de los n primeros numeros naturales
def suma_cuadrados(n:int) -> int:
    return sum(cuadrados(n))

# crear una funcion que devuelva la suma de los cuadrados de los n primeros numeros naturales