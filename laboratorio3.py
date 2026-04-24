# 1. Define tu función aquí usando 'def'. 
# Debe llamarse calcular_envio y recibir el parámetro 'peso_kilos'
def calcular_envio(peso_kilos):

    costo_total = 50 + (peso_kilos * 15)

    return costo_total


    # 2. Haz la matemática: 50 + (peso_kilos * 15) y guárdalo en una variable como 'costo_total'
    

    # 3. Usa 'return' para devolver esa variable hacia afuera
    

# ==========================================
# CÓDIGO DE PRUEBA (Esto va sin sangría, pegado a la izquierda)
# No modifiques esto, solo úsalo para probar si tu máquina funciona.

print("--- COTIZADOR DE ENVÍOS ---")

costo_paquete_ligero = calcular_envio(2) 
costo_paquete_mediano = calcular_envio(5) 
costo_paquete_pesado = calcular_envio(10) 

print("El envío de 2kg cuesta: $", costo_paquete_ligero)
print("El envío de 5kg cuesta: $", costo_paquete_mediano)
print("El envío de 10kg cuesta: $", costo_paquete_pesado)