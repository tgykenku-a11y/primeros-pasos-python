# 1. Definimos los datos de nuestro producto en la base de datos
modelo_audifonos = "JBL Tune 770NC"
precio_pesos = 1499
unidades_en_bodega = 0

# 2. El motor de decisiones (Condicional if/else)
# Preguntamos: ¿Las unidades son mayores a cero?
if unidades_en_bodega > 0:
    estado_boton = "Habilitado - Agregar al carrito"
    mensaje_cliente = "¡Disponible para envío inmediato!"
else:
    estado_boton = "Deshabilitado"
    mensaje_cliente = "Agotado temporalmente."

# 3. Mostramos cómo se vería la pantalla final del cliente
print("--- Detalle del Producto ---")
print("Modelo:", modelo_audifonos)
print("Precio: $", precio_pesos)
print("Estado del botón:", estado_boton)
print("Mensaje:", mensaje_cliente)