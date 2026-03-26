# ==========================================
# Autor: Luis Chaparro Mejías
# Fecha: 25/26 de marzo de 2026 
# Proyecto: Calculadora Básica de Python
# ==========================================

print("Bienvenid@ a mi calculadora básica de Python")

# Captura de datos
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
operacion = str(input("Elige la operación (Suma, Resta, Multiplicación, División): ")).capitalize()

numero = 0

# Lógica con control de errores
if operacion == "Suma":
    numero = numero1 + numero2
elif operacion == "Resta":
    numero = numero1 - numero2
elif operacion == "División" or operacion == "Division":
    if numero2 == 0:
        print("Error: No se puede dividir entre cero.")
        exit()
    else:
        numero = numero1 / numero2
elif operacion == "Multiplicación" or operacion == "Multiplicacion":
    numero = numero1 * numero2
else:
    print("Error: Por favor, escribe la operación adecuada.")
    exit() 

# Salida del resultado final (solo si no hubo errores antes)
print(f"La solución de hacer {numero1} {operacion} {numero2} es {numero}")