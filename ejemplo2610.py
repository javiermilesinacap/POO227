import abc
class Vehiculo(abc.ABC):
    def __init__(self):
        self.ruedas=0
        self.__color=(255,0,0)
        self.velocidad=0
        self.motor=""
        print("Hola, soy un Vehiculo")
        pass
    def getColor(self):
        print("Soy de color: ",self.__color)
class Aereo(Vehiculo):
    def __init__(self, motor="Turbina", velocidad=100):
        super().__init__()
        alas=0
        print("Ahora soy un avión", self.getColor())
class Anfibio(Vehiculo):
        profundidadMax=0
class Terrestre(Vehiculo):
    pass
vehiculo = Aereo(motor="Reaccion")
#vehiculoA = Vehiculo()
#vehiculo.__color="Blanco"
print(vehiculo.getColor())
