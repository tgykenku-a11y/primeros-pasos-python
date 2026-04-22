# Base de datos actual (Una lista que contiene tres diccionarios)
inventario = [
    {"equipo": "Lenovo ThinkCentre", "precio": 12000, "stock": 5},
    {"equipo": "Asus TUF F15", "precio": 18500, "stock": 0},
    {"equipo": "Auriculares JBL Tune 770NC", "precio": 1499, "stock": 10}
]

print("--- REPORTE DE INVENTARIO ---")

for lab in inventario:
    # Le preguntamos el stock a 'lab'
    if lab["stock"] > 0:
        # Le pedimos el precio a 'lab' y lo multiplicamos
        desprecio = lab["precio"] * 0.90
        print("Equipo: ", lab["equipo"], "--> $", desprecio)
    else:
        print("Equipo: ", lab["equipo"], "Agotado")


# 1. Escribe aquí tu ciclo for para recorrer la lista 'inventario'
# (Recuerda los dos puntos al final)


    # 2. Dentro del ciclo, escribe un if para comprobar si el "stock" del producto es mayor a 0
    # (Recuerda la indentación y extraer el dato del diccionario usando sus corchetes y comillas)
    

        # 3. Si sí hay stock:
        # Crea una variable para calcular el precio final aplicándole un 10% de descuento.
        # Imprime el nombre del equipo, un mensaje de "Disponible" y su precio con descuento.


    # 4. Escribe el else (Si el stock es 0)
    
        
        # 5. Imprime el nombre del equipo y un mensaje de "Agotado".