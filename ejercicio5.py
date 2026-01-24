print("=" * 30)
print("SISTEMA DE NOTAS".center(29))
print("=" * 30)

matematicas = float(input("Matematicas: "))
ciencias = float(input("Ciencias: "))
historia = float(input("Historia: "))
ingles = float(input("Ingles: "))

print("-" * 28)

promedio = (matematicas + ciencias + historia + ingles) / 4
print(f"PROMEDIO: {promedio:.2f}")

mayor_nota = max(matematicas, ciencias, historia, ingles)
print(f"NOTA MÁS ALTA: {mayor_nota}")

menor_nota = min(matematicas, ciencias, historia, ingles)
print(f"NOTA MÁS BAJA: {menor_nota}")

diferencia = mayor_nota - menor_nota
print(f"DIFERENCIA: {diferencia:.0f} puntos")

print("=" * 30)

if promedio == 100:
    print("EXCELENTE!")
elif promedio >= 90:
    print("Excelente desempeño!")
elif promedio >= 70:
    print("Pasaste")
else:
    print("Reprobado")