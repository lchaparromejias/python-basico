# ==========================================
# Autor: Luis Chaparro Mejías
# Fecha: 25 de marzo de 2026
# Proyecto: Calculadora Básica de Python
# ==========================================

# Mensaje de bienvenida
print("Bienvenid@ a mi calculadora básica de Python")

# Captura de datos del usuario
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Captura y normalización de la operación (evita errores por mayúsculas)
operacion = str(input("Elige la operación (Suma, Resta, Multiplicación, División): ")).capitalize()

# Lógica principal de la calculadora
numero = 0

if operacion == "Suma":
    numero = numero1 + numero2
elif operacion == "Resta":
    numero = numero1 - numero2
elif operacion == "División" or operacion == "Division":
    numero = numero1 / numero2
elif operacion == "Multiplicación" or operacion == "Multiplicacion":
    numero = numero1 * numero2
else:
    print("Por favor, escribe la operación adecuada.")

# Salida del resultado final
print(f"La solución de hacer {numero1} {operacion} {numero2} es {numero}")