import math as mate
far = int(input("Ingresa la unidad en Fahrenheit: "))
cel = float((far - 32) * 5/9)

mil = int(input("Ingresa la unidad en millas: "))
km = float(mil * 1.60934)

feet = int(input("Ingresa la unidad en pies: "))
mt = float(feet * 0.3048)




print("\n")
print("=" * 25)
print("CONVERSOR DE UNIDADES".center(25))
print("=" * 25)

print(f"\n{far}°F = {mate.ceil(cel)}°C")
print(f"\n{mil} millas = {mate.floor(km)} km")
print(f"\n{feet} pies = {mate.ceil(mt)} metros")
print("=" * 25)