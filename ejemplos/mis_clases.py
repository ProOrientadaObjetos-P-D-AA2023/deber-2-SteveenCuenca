"""

"""


# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Celulares:

    def __init__(self, marca, modelo, color, origen):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.origen = origen

    def __str__(self):
        return (f"\nLa informacion del celulas es: \n"
                f"Marca del celular: {self.marca}\n"
                f"Modelo del celular: {self.modelo}\n"
                f"Color del celular: {self.color}\n"
                f"Importado desde: {self.origen}")


# clase 02
class Subcentro:
    def __init__(self, nombre, numDoctores, numCamas, presupuesto):
        self.nombre = nombre
        self.numDoctores = numDoctores
        self.numCamas = numCamas
        self.presupuesto = presupuesto

    def __str__(self):
        return (f"\nDatos del subcentro \"{self.nombre}\":\n"
                f"Cuenta con {self.numDoctores} doctores\n"
                f"Cuenta con {self.numCamas} camas\n"
                f"Tiene un presupuesto de ${self.presupuesto} dolares")
