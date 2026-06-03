from datetime import datetime as dt, timedelta, UTC
import random


def mostrar_bienvenida():
    """Muestra el banner de bienvenida de PyBot."""
    print("🤖" * 15)
    print("!HOLA! SOY PYBOT".center(33))
    print("🤖TU ASISTENTE VIRTUAL🤖".center(30))
    print("🤖" * 15)
    print("")
    print("👋Hola! un gusto en saludarte, me llamo PYBOT,")


def obtener_hora_venezuela():
    """Obtiene la fecha y hora actual en Venezuela (UTC-4)."""
    hora_utc = dt.now(UTC)
    diferencia_VNZL = timedelta(hours=4)
    return hora_utc - diferencia_VNZL


def mostrar_fecha_hora(hora_venezuela):
    """Muestra la fecha, hora y día de la semana en Venezuela."""
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_de_la_semana = dias_semana[hora_venezuela.weekday()]

    print("\n📅 INFORMACIÓN DEL DÍA:")
    print("_" * 30)
    print(f"  📅 Fecha: {hora_venezuela.day:02d}-{hora_venezuela.month:02d}-{hora_venezuela.year}")
    print(f"  ⌚ Hora: {hora_venezuela.strftime('%I:%M:%S %p')}")
    print(f"  ⏳ Día: {dia_de_la_semana}")
    print("")


def pedir_fecha_nacimiento():
    """Pide la fecha de nacimiento al usuario con validación."""
    while True:
        try:
            dia = int(input("\nDime el número del día que naciste: "))
            mes = int(input("Dime el número del mes en el que naciste: "))
            year = int(input("Dime el año en el que naciste: "))
            nacimiento = dt(year, mes, dia)
            return nacimiento
        except ValueError:
            print("⚠️ Fecha inválida. Por favor, ingresa una fecha correcta.")


def calcular_edad(nacimiento, hora_venezuela):
    """Calcula la edad actual y los días faltantes para el próximo cumpleaños."""
    edad = hora_venezuela.year - nacimiento.year

    if (hora_venezuela.month, hora_venezuela.day) < (nacimiento.month, nacimiento.day):
        edad -= 1

    hoy_solo_fecha = hora_venezuela.replace(tzinfo=None)
    proximo_cumple = dt(hora_venezuela.year, nacimiento.month, nacimiento.day)

    if proximo_cumple < hoy_solo_fecha:
        proximo_cumple = dt(hora_venezuela.year + 1, nacimiento.month, nacimiento.day)

    dias_faltantes = (proximo_cumple - hoy_solo_fecha).days + 1

    return edad, dias_faltantes


def mostrar_cumpleanos(nacimiento, edad, dias_faltantes):
    """Muestra la información del cumpleaños del usuario."""
    print("🎂 TU CUMPLEAÑOS:")
    print("_" * 30)
    print(f"  Naciste el {nacimiento.day:02d}-{nacimiento.month:02d}-{nacimiento.year}")
    print(f"  Tu edad es {edad} años")
    print(f"  Te faltan {dias_faltantes} días para cumplir años")
    print("")


def mostrar_dato_curioso():
    """Muestra un dato curioso aleatorio sobre Python."""
    dichos_python = [
        "¿Sabías que Python se llama así por Monty Python, no por la serpiente? 🎬",
        "Python fue creado por Guido van Rossum como un proyecto de hobby en 1989 🧑‍💻",
        "La filosofía de Python incluye 'Lo simple es mejor que lo complejo' 🎯",
        "Python tiene una comunidad tan grande que se llama 'Pythonistas' 👥",
        "El logo de Python representa dos serpientes entrelazadas, no una sola 🐍",
        "Python es el lenguaje más popular para Ciencia de Datos y Machine Learning 📊",
        "El 'Zen de Python' son 19 principios de diseño del lenguaje (import this) 🧘"
    ]

    print("🐍 DATO CURIOSO DE PYTHON:")
    print("_" * 30)
    print(f"  {random.choice(dichos_python)}")
    print("")


def mostrar_mensaje_motivacional():
    """Muestra un mensaje motivacional aleatorio."""
    mensajes_principiantes = [
        "Tu primer programa 'Hola Mundo' es tan importante como cualquier otro. ¡Celebra cada logro! 🎉",
        "Cada experto fue una vez un principiante que no se rindió. ¡Tú puedes! 💫",
        "Los errores no son fracasos, son lecciones disfrazadas. ¡Debuggear te hace más fuerte! 🐛➡️🦋",
        "No tienes que ser genio para programar, solo tener curiosidad y persistencia. 🧩",
        "La programación es como un superpoder: puedes crear algo de la nada. ✨",
        "Hoy escribiste una línea de código, mañana podrías cambiar el mundo. 🌍",
        "La paciencia es tu mejor aliada. Los programas no se construyen en un día. ⏳",
        "Cometer errores es la forma más rápida de aprender. ¡Abraza los errores! 🤗",
        "Cada línea de código que escribes te hace un mejor programador. 📈",
        "Recuerda: Google es el mejor amigo de todo programador. No lo olvides. 🔍"
    ]

    print("💪 MENSAJE MOTIVACIONAL:")
    print("_" * 30)
    print(f"  {random.choice(mensajes_principiantes)}")
    print("")


def mostrar_menu():
    """Muestra el menú interactivo de opciones."""
    print("\n📋 ¿Qué te gustaría ver?")
    print("_" * 30)
    print("  1. 📅 Fecha y hora actual")
    print("  2. 🎂 Info de tu cumpleaños")
    print("  3. 🐍 Dato curioso de Python")
    print("  4. 💪 Mensaje motivacional")
    print("  5. 🔄 Ver todo de nuevo")
    print("  6. 👋 Salir")
    print("_" * 30)


def main():
    mostrar_bienvenida()

    name = input("Me podrías decir cual es tu nombre?: ")
    name = name.capitalize()
    print(f"\n¡Encantado de conocerte, {name}! 🌟")

    hora_venezuela = obtener_hora_venezuela()
    mostrar_fecha_hora(hora_venezuela)

    print(f"Ya que estamos aquí {name}, te voy a pedir")
    print("unos datos para darte un detalle importante para ti 😊🚀")

    nacimiento = pedir_fecha_nacimiento()
    edad, dias_faltantes = calcular_edad(nacimiento, hora_venezuela)
    print("")

    mostrar_cumpleanos(nacimiento, edad, dias_faltantes)
    mostrar_dato_curioso()
    mostrar_mensaje_motivacional()

    print(f"🚀 ¡Sigue programando, {name}! El futuro te espera.")
    print("La disciplina tarde o temprano vencerá al talento 🐍✨")
    print("🤖" * 15)

    # Menú interactivo
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            hora_venezuela = obtener_hora_venezuela()
            mostrar_fecha_hora(hora_venezuela)
        elif opcion == "2":
            edad, dias_faltantes = calcular_edad(nacimiento, hora_venezuela)
            mostrar_cumpleanos(nacimiento, edad, dias_faltantes)
        elif opcion == "3":
            mostrar_dato_curioso()
        elif opcion == "4":
            mostrar_mensaje_motivacional()
        elif opcion == "5":
            hora_venezuela = obtener_hora_venezuela()
            mostrar_fecha_hora(hora_venezuela)
            edad, dias_faltantes = calcular_edad(nacimiento, hora_venezuela)
            mostrar_cumpleanos(nacimiento, edad, dias_faltantes)
            mostrar_dato_curioso()
            mostrar_mensaje_motivacional()
        elif opcion == "6":
            print(f"\n👋 ¡Hasta luego, {name}! Fue un gusto ayudarte. 🤖✨")
            break
        else:
            print("⚠️ Opción no válida. Elige un número del 1 al 6.")

    print("\n🤖" * 15)


# Primer asistente virtual creado en Python!
if __name__ == "__main__":
    main()
