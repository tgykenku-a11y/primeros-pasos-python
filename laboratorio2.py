# Base de datos en tiempo real de nuestros servidores
servidores = [
    {"nombre": "Servidor Web", "uso_cpu": 40, "estado": "Activo"},
    {"nombre": "Base de Datos", "uso_cpu": 92, "estado": "Activo"},
    {"nombre": "Servidor de Pruebas", "uso_cpu": 5, "estado": "Inactivo"}
]

print("--- DIAGNÓSTICO DE SISTEMAS ---")

for sistem in servidores:
    if sistem["estado"] == "Inactivo":
        print("Nombre: ", sistem["nombre"], " apagado por mantenimeinto")
    elif sistem["uso_cpu"] >= 85:
        print("Nombre: ", sistem["nombre"], "¡ALERTA! CPU Crítico")
    else:
        print("Nombre: ", sistem["nombre"], "Operando normal")

# 1. Inicia tu ciclo for para recorrer la lista 'servidores'. 
# (Ponle el nombre que quieras a tu variable temporal)


    # 2. Primer escenario (if): Revisa si la llave "estado" es exactamente igual a "Inactivo"
    # (Recuerda usar == para comparar textos)


        # Imprime el nombre del servidor y un mensaje de "Apagado por mantenimiento".


    # 3. Segundo escenario (elif): Revisa si la llave "uso_cpu" es mayor o igual a 85


        # Imprime el nombre del servidor y un mensaje de "¡ALERTA! CPU Crítico".


    # 4. Escenario por defecto (else): Si no está inactivo y no pasa de 85 de CPU


        # Imprime el nombre del servidor y un mensaje de "Operando normal".