def number_pattern(n):
    # Validación 1: Verificar si es entero
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    
    # Validación 2: Verificar si es mayor que 0
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    # Generar el patrón
    result = ''
    for i in range(1, n + 1):
        result += str(i)
        if i < n:  # Agregar espacio excepto después del último número
            result += ' '
    
    return result

# Tests
print(number_pattern(4))      # '1 2 3 4'
print(number_pattern(1))      # '1'
print(number_pattern(10))     # '1 2 3 4 5 6 7 8 9 10'
print(number_pattern('5'))    # 'Argument must be an integer value.'
print(number_pattern(0))      # 'Argument must be an integer greater than 0.'
print(number_pattern(-3))     # 'Argument must be an integer greater than 0.'
