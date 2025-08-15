# Selvin Arias Lara, Mariana Mora Guzmán

def multiplo_2(base, multiplo):
    # Validar que los parámetros sean enteros y positivos
    if not isinstance(base, int) or not isinstance(multiplo, int):
        return -400, None

    if base < 0 or multiplo < 0:
        return -400, None

    # Validar que el valor del múltiplo esté en el rango permitido
    if multiplo not in (1, 2, 4, 8, 16):
        return -500, None

    # Mapa de desplazamientos para la multiplicación por bits
    shift_map = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4}

    # Multiplicación usando desplazamiento de bits
    resultado = base << shift_map[multiplo]

    return 0, resultado


def count_char(cadena, caracter):

    # Validar que la cadena sea un string
    if not isinstance(cadena, str):
        return -100, None

    # Validar que la cadena solo contenga letras y números
    if not cadena.isalnum():
        return -200, None

    # Validar que el caracter sea un string de 1 solo caracter
    if not isinstance(caracter, str) or len(caracter) != 1:
        return -300, None

    if not caracter.isalnum():
        return -300, None

    # Contar ocurrencias
    cantidad = cadena.count(caracter)

    return 0, cantidad
