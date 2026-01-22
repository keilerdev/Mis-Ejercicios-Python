print("=== INGRESO DE PRODUCTOS ===")
print("")

manzanas_precio = float(input("Precio de la manzana: "))
manzanas_cantidad = int(input("Cantidad de manzanas: "))

leche_precio = float(input("Precio de la leche: "))
leche_cantidad = int(input("Cantidad de leches "))

pan_precio = float(input("Precio del pan: "))
pan_cantidad = int(input("Cantidad de panes: "))

print("")

print("=" * 31)
print("FACTURA DE COMPRA".center(30))
print("=" * 31)


precio_total_de_manzanas = manzanas_cantidad * manzanas_precio
precio_total_de_leche = leche_cantidad * leche_precio
precio_total_de_pan = pan_cantidad * pan_precio

subtotal = float(precio_total_de_manzanas + precio_total_de_leche + precio_total_de_pan)



print(f"{"Manzanas".ljust(15)} {manzanas_cantidad} x ${manzanas_precio:.2f} = ${precio_total_de_manzanas:.2f}")
print(f"{"Leche".ljust(15)} {leche_cantidad} x ${leche_precio:.2f} = ${precio_total_de_leche:.2f}")
print(f"{"Pan".ljust(15)} {pan_cantidad} x ${pan_precio:.2f} = ${precio_total_de_pan:.2f}")
print("-" * 31)


subtotal = float(precio_total_de_manzanas + precio_total_de_leche + precio_total_de_pan)
iva = float(subtotal * 0.16)
total = float(subtotal + iva)

print(f"{"Subtotal:".ljust(15)} ${subtotal:.2f}")
print(f"{"IVA (16%):".ljust(15)} ${iva:.2f}")
print("-" * 31)

print(f"{"TOTAL A PAGAR:".ljust(15)} ${total:.2f}")
print("=" * 31)