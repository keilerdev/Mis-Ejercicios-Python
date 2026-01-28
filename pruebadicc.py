orden_compra = {"id": 550,
                "clientes": "keiler",
                "productos": [{"nombre": "Laptop",
                               "precio": 1000,
                               "cantidad": 1},
                              
                              {"nombre": "Mouse",
                               "precio": 20, 
                               "cantidad": 2}]
                }

print(orden_compra["productos"][1]["precio"])
print(orden_compra["productos"][0]["precio"])
print("")

total_a_pagar = 0

for item in orden_compra["productos"]:

    subtotal = item["precio"] * item["cantidad"]

    total_a_pagar += subtotal

print(f"El total de la factura es ${total_a_pagar}")
#Probando el usos de los diccionarios, ficheros JSON y listas en Python.
#Orgulloso de mi avanze.