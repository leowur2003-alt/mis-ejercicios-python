import re

while True:
    entrada = input("Escribe la operación (ej. 10 + 5) o Salir: ").strip()
    if entrada.lower() == "salir":
        print("Adiós!")
        break

    partes = entrada.split()
    if len(partes) == 3:
        num1_str, op, num2_str = partes
    else:
        # Intentar separar usando regex, por ejemplo, 10+5 o 12*4
        coincidencia = re.match(r'\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*', entrada)
        if coincidencia:
            num1_str, op, num2_str = coincidencia.groups()
        else:
            print("Operación no reconocida. Usa el formato: 10 + 5, 7*8, etc.")
            continue
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Por favor, introduce números válidos.")
        continue

    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        try:
            resultado = num1 / num2
        except ZeroDivisionError:
            print("No se puede dividir por cero.")
            continue
    else:
        print("Operador no válido. Usa +, -, *, o /.")
        continue

    print("Resultado:", resultado)