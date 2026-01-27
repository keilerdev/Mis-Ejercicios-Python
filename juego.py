import random

print("🎲" * 20)
print("¡ADIVINA EL NÚMERO SECRETO!".center(40))
print("Estoy pensando en un número del 1 al 100...".center(40))
print("🎲" * 20)

# 1. La computadora elige el número secreto
numero_secreto = random.randint(1, 100)
intentos = 0

# 2. Empezamos el bucle infinito (El juego)
while True:
    try:
        # Pedimos el número al usuario
        jugador = int(input("\n🔢 ¿Cuál es tu número?: "))
        intentos += 1  # Sumamos un intento

        # 3. La lógica de comparación
        if jugador < numero_secreto:
            print("❌ Muy BAJO... ¡Sube más! ⬆️")
        
        elif jugador > numero_secreto:
            print("❌ Muy ALTO... ¡Baja un poco! ⬇️")
        
        else:
            # Si no es alto ni bajo, ¡es el correcto!
            print("\n" + "🎉" * 15)
            print(f"¡FELICIDADES! ¡ADIVINASTE! 🏆".center(30))
            print(f"El número era {numero_secreto}".center(30))
            print(f"Lo lograste en {intentos} intentos.".center(30))
            print("🎉" * 15)
            break  # <- Salimos del bucle

    except ValueError:
        # Por si el usuario escribe letras en vez de números
        print("⚠️ Error: Por favor, ingresa solo números.")

print("\nGracias por jugar. ¡Hasta la próxima!")