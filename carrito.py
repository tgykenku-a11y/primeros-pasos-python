# 1. Definimos una Lista con los productos que eligió el cliente
productos_cliente = ["Monitor Asus", "Mouse Inalámbrico", "Cable HDMI","teclado","tablet"]

print("--- Procesando orden de compra ---")

# 2. El Ciclo For (La automatización)
# 'articulo' es una variable temporal que tomará el valor de cada producto, uno por uno.
for articulo in productos_cliente:
    print("Empacando el producto:", articulo)

# Esta línea está fuera del ciclo (no tiene espacio/sangría)
print("¡Orden procesada con éxito!")