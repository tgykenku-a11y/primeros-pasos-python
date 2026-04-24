# 1. CREAMOS EL MOLDE (La Clase). Siempre inicia con mayúscula.
class Audifonos:
    
    # 2. EL CONSTRUCTOR (La fábrica que arma el objeto cuando nace)
    # Siempre lleva 'self' como primer parámetro.
    def __init__(self, marca_ingresada, modelo_ingresado):
        # Aquí guardamos los datos dentro del objeto ("mis datos = datos ingresados")
        self.marca = marca_ingresada
        self.modelo = modelo_ingresado
        self.bateria = 100  # Todos nacen con 100% de batería por defecto
        self.encendido = False

    # 3. LOS MÉTODOS (Las acciones que puede hacer este objeto)
    def prender(self):
        self.encendido = True
        print("\n¡" + self.marca + " encendidos y listos para conectar!\n")
        
    def usar(self):
        if self.encendido == True:
            self.bateria = self.bateria - 10
            print("Escuchando música. Batería al", self.bateria, "%\n")
        else:
            print("No puedes escuchar música, están apagados.")

# Construimos dos objetos distintos usando el mismo molde
mis_auriculares = Audifonos("JBL", "Tune 770NC")
auriculares_hermano = Audifonos("Sony", "WH-1000XM4")

# Usamos las acciones (métodos) de MIS auriculares
mis_auriculares.prender()
mis_auriculares.usar()

# Los de mi hermano siguen apagados y con 100% de batería porque son otro objeto
auriculares_hermano.usar()