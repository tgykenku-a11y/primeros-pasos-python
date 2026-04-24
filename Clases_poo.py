class CuentaBancaria:
    
    # 1. EL CONSTRUCTOR: ¿Qué pasa en el segundo exacto en que se abre la cuenta?
    def __init__(self, nombre_cliente, deposito_inicial):
        # 'self' significa "MI cuenta". 
        # Aquí guardamos los datos iniciales.
        self.titular = nombre_cliente
        self.saldo = deposito_inicial
        self.activa = True

    # 2. MÉTODO 1 (Acción): Depositar dinero
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Depósito exitoso. El nuevo saldo de", self.titular, "es $", self.saldo)

    # 3. MÉTODO 2 (Acción): Retirar dinero
    def retirar(self, cantidad):
        # El objeto es inteligente, puede tomar decisiones lógicas por sí mismo
        if cantidad > self.saldo:
            print("Error: Fondos insuficientes en la cuenta de", self.titular)
        else:
            self.saldo = self.saldo - cantidad
            print("Retiro exitoso. Saldo restante de", self.titular, "es $", self.saldo)

# 1. Nacen los objetos. Abrimos dos cuentas distintas.
# Al escribir esto, se ejecuta automáticamente el __init__
cuenta_osmar = CuentaBancaria("Osmar", 1000)
cuenta_ana = CuentaBancaria("Ana", 500)

# 2. Interactuamos con la cuenta de Osmar
cuenta_osmar.depositar(200)   # Osmar ahora tiene 1200
cuenta_osmar.retirar(5000)    # Lanzará error: fondos insuficientes

# 3. Interactuamos con la cuenta de Ana
cuenta_ana.retirar(100)       # Ana ahora tiene 400

print("--- REPORTE FINAL ---")
print("Saldo final de Osmar:", cuenta_osmar.saldo)
print("Saldo final de Ana:", cuenta_ana.saldo)