# 1. Define tu función. 
# Debe llamarse aplicar_membresia y recibir dos parámetros: (precio_base, nivel_cliente)
def aplicar_membresia(precio_base, nivel_cliente):
    if nivel_cliente == "Oro":
        precio_descuento = precio_base * 0.80
    elif nivel_cliente == "Plata":
        precio_descuento = precio_base * 0.90
    else:
        precio_descuento = precio_base
    
    return precio_descuento

    # 2. Escribe un 'if' para revisar si el nivel_cliente es exactamente igual a "Oro"
    # Si lo es, crea una variable con el precio_base multiplicado por 0.80
    
    
    # 3. Escribe un 'elif' para revisar si es "Plata"
    # Si lo es, multiplica el precio_base por 0.90
    
    
    # 4. Escribe un 'else' para cualquier otro caso
    # El precio final se queda igual al precio base
    
    
    # 5. Afuera del if/else (pero aún dentro de la función), usa 'return' para devolver el precio final calculado.
    

# ==========================================
# CÓDIGO DE PRUEBA 
print("--- CAJA REGISTRADORA VIP ---")

# Simulamos que tres clientes diferentes compran un monitor de $5000
pago_carlos = aplicar_membresia(5000, "Oro")
pago_ana = aplicar_membresia(5000, "Plata")
pago_luis = aplicar_membresia(5000, "Bronce")

print("Carlos (Oro) debe pagar: $", pago_carlos)
print("Ana (Plata) debe pagar: $", pago_ana)
print("Luis (Bronce) debe pagar: $", pago_luis)