from datetime import datetime as dt, timedelta, UTC
import random

print("🤖" * 15)
print("!HOLA! SOY PYBOT".center(33))
print("🤖TU ASISTENTE VIRTUAL🤖".center(30))
print("🤖" * 15)
print("")
print("👋Hola! un gusto en saludarte, me llamo PYBOT,")

name = input("Me podrías decir cual es tu nombre?: ")
name = name.capitalize()
print(f"\n!Encantado de conocerte, {name}! 🌟")
print("\nAhora te daré la información del día:")
print("\n📅INFORMACIÓN DEL DÍA: ")
print("_" * 30)



#Evalua la fecha actual en Venezuela y la hora!
hora_utc = dt.now(UTC)
diferencia_VNZL = timedelta(hours=4)
hora_venezuela = hora_utc - diferencia_VNZL

#Evalua el día de la semana en Venezuela
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_de_la_semana = dias_semana[hora_venezuela.weekday()]

#Formato de la fecha hora y el día en venezuela
print(f"{"• 📅Fecha:".ljust(10)} {hora_venezuela.day:02d}-{hora_venezuela.month:02d}-{hora_venezuela.year}")
print(f"{"• ⌚Hora:".ljust(10)} {hora_venezuela.strftime("%I:%M:%S %p")}")
print(f"{"• ⏳Día de la semana:".ljust(10)} {dia_de_la_semana}")
print("")

print(f"Ya que estamos aqui {name}, te \nvoy a pedir unos datos para darte \nun detalle importante para ti 😊🚀")
dia = int(input("\nDime el número del día que naciste: "))
mes = int(input("Dime el número del mes en el que naciste: "))
year = int(input("Dime el año en el que naciste: "))
print("")


#Condición para sacar la edad actual del usuario
nacimiento = dt(year, mes, dia)
hoy_venezuela = hora_venezuela
edad = hoy_venezuela.year - nacimiento.year

#ajustamos la edad si no ha cumplido este año
if (hoy_venezuela.month, hoy_venezuela.day) < (nacimiento.month, nacimiento.day):
	edad -= 1

#hacemos el calculo del los dias faltantes, cambiamos la zona horaria de venezuela a Naive
hoy_solo_fecha = hoy_venezuela.replace(tzinfo=None)
proximo_cumple = dt(hoy_venezuela.year, nacimiento.month, nacimiento.day)

if proximo_cumple < hoy_solo_fecha:
    proximo_cumple = dt(hoy_venezuela.year + 1, nacimiento.month, nacimiento.day)

dias_faltantes = (proximo_cumple - hoy_solo_fecha).days + 1



#CUMPLEAñOS
print("🎂 TU CUMPLEAÑOS:")
print("_" * 30)
print(f"• Naciste el {dia:02d}-{mes:02d}-{year}")
print(f"• Tu edad es {edad} años")
print(f"• Te faltan {dias_faltantes} días para cumplir años")
print("")

print("🐍 DATO CURIOSO DE PYTHON:")
print("_" * 30)
print("")

dichos_python = [
    "¿Sabías que Python se llama así por Monty Python, \nno por la serpiente? 🎬",
    "Python fue creado por Guido van Rossum como un \nproyecto de hobby en 1989 🧑‍💻",
    "La filosofía de Python incluye 'Lo simple es \nmejor que lo complejo' 🎯",
    "Python tiene una comunidad tan grande que \nse llama 'Pythonistas' 👥",
    "El logo de Python representa dos serpientes \nentrelazadas, no una sola 🐍",
    "Python es el lenguaje más popular para Ciencia \nde Datos y Machine Learning 📊",
    "El 'Zen de Python' son 19 principios de \ndiseño del lenguaje (import this) 🧘"
]

dicho_seleccionado = random.choice(dichos_python)
print(dicho_seleccionado)
print("")

print("💪 MENSAJE MOTIVACIONAL:")
print("_" * 30)


mensajes_principiantes = [
    "“Tu primer programa 'Hola Mundo' es tan importante como \ncualquier otro. ¡Celebra cada logro! 🎉",
    "“Cada experto fue una vez un principiante que \nno se rindió. ¡Tú puedes! 💫",
    "“Los errores no son fracasos, son lecciones disfrazadas. \n¡Debuggear te hace más fuerte! 🐛➡️🦋",
    "“No tienes que ser genio para programar, solo \ntener curiosidad y persistencia. 🧩",
    "“La programación es como un superpoder: \npuedes crear algo de la nada. ✨",
    "“Hoy escribiste una línea de código, \nmañana podrías cambiar el mundo. 🌍",
    "“La paciencia es tu mejor aliada. Los \nprogramas no se construyen en un día. ⏳",
    "“Cometer errores es la forma más rápida de \naprender. ¡Abraza los errores! 🤗",
    "“Cada línea de código que escribes te \nhace un mejor programador. 📈",
    "“Recuerda: Google es el mejor amigo de \ntodo programador. No lo olvides. 🔍"
]

mensaje_seleccionado = random.choice(mensajes_principiantes)
print(mensaje_seleccionado)
print("")

print(f"🚀 ¡Sigue programando, {name} \nEl futuro te espera la disciplina tarde o \ntemprano vencerá al talento 🐍✨")

print("🤖" * 15)


#Primer asistente virtual creado en Python!
