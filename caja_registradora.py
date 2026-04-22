# 1. Una Lista que adentro contiene Diccionarios (Un carrito real)
carrito_compras = [
    {"articulo": "Laptop Lenovo ThinkPad", "precio": 25000},
    {"articulo": "Audífonos JBL Tune 770NC", "precio": 1499},
    {"articulo": "Mouse Inalámbrico", "precio": 350},
    {"articulo": "Teclado mecanico", "precio": 1000}
]

# 2. Variable para ir sumando el dinero (inicia en cero)
total_a_pagar = 0

print("--- TICKET DE COMPRA ---")

# 3. El ciclo For lee cada diccionario de la lista
for item in carrito_compras:
    # Imprimimos el nombre y el precio sacándolos del diccionario
    print("Cobrando:", item["articulo"], "-> $", item["precio"])
    
    # 4. Matemáticas: Al total actual, le sumamos el precio de este artículo
    total_a_pagar = total_a_pagar + item["precio"]

print("------------------------")
print("TOTAL FINAL: $", total_a_pagar)