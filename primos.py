def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos(n:int) -> list[int]:
    return [i for i in range(2, n) if es_primo(i)]

def test_primos():
    # Optimizar para que el bucle en es_primo se detenga en la raíz cuadrada de n
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Probar es_primo() con varios números
print("=== Probando es_primo() ===")
# Números primos (deberían dar True)
print("Primos:", 2, es_primo(2), 3, es_primo(3), 5, es_primo(5), 7, es_primo(7), 11, es_primo(11))
# Números no primos (deberían dar False)  
print("No primos:", 1, es_primo(1), 4, es_primo(4), 6, es_primo(6), 9, es_primo(9))

# Probar primos()
print("\n=== Probando primos() ===")
print("primos(20) =", primos(20))