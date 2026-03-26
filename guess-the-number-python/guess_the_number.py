# ==========================================
# Autor: Luis Chaparro Mejías
# Fecha: 25 de marzo de 2026
# Proyecto: Guess the Number Game
# ==========================================
import random

# Mensaje de bienvenida al usuario
print("Bienvenid@ al juego de adivinar el número")

ordenador = random.randint(1, 10)

while True:
    # Solicitud de entrada de datos con formato profesional
    numero = int(input("Introduce un número para adivinar (entre 1 y 10): "))
    
    if numero > ordenador:
        print("El número ingresado es superior. Inténtalo de nuevo.")       
    elif numero < ordenador:
        print("El número ingresado es inferior. Inténtalo de nuevo.")
    else:
        # Mensaje de éxito al coincidir los valores
        print(f"¡Felicidades! Has acertado, el número era: {ordenador}")
        break 