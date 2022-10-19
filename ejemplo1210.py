import pygame

class Vehiculo:
    patente = ""
    color=""
    chassis =""
    puertas=0
    __velocidad=0
    latitud=0.0
    longitud=0.0
    distancia=0
    def acelerar(self):
        self.__velocidad += 10 #velodcidad = velocidad + 10
        self.avanzar()
    def frenar(self):
        self.__velocidad -= 10 #velodcidad = velocidad + 10
        self.retroceder()
    def setVelocidad(self,cuanto) -> None:
        self.__velocidad = cuanto
    def getVelocidad(self) -> int:
        return self.__velocidad
    def avanzar(self):
        self.latitud += (self.__velocidad/5 + 10) 
    def retroceder(self):
        self.latitud -= (self.__velocidad/5 - 10) 
    def __init__(self, velocidad=0, marca="",latitud=0, longitud=0) -> None:
        self.__velocidad = velocidad
        self.latitud = latitud
        self.longitud = longitud
        self.marca = marca
        pass
class Camion(Vehiculo):
        pass
camion = Camion(50,"Volvo")
camion.getVelocidad()
objeto = Vehiculo(100,"Mazda")
pygame.init()
ventana = pygame.display.set_mode((800,600))
autito = pygame.image.load('./autito.png').convert_alpha()
#objeto.__velocidad = 1000
#objeto.setVelocidad(123)
print(objeto.getVelocidad())
while(True):
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_w):
            objeto.acelerar() 
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            objeto.frenar()
    pygame.display.update()
    ventana.blit(autito,(objeto.latitud,100)) 
    print(f'El vehículo va a {objeto.getVelocidad()}')


#################### EXPLICACION
'''
    print(' 1 para acelerar
    2 para frenar
    0 salir')
    opcion = int(input())
    if(opcion==1):
        objeto.acelerar()
    if(opcion==2):
        objeto.frenar()
    if(opcion==0):
        break
    print(f'El vehículo va a {objeto.getVelocidad()}')
'''







############################### EXPLICACION DE GLOBAL ###########################
'''
velocidad = 0
def acelerar(cuanto):
    global velocidad
    velocidad +=cuanto
    return velocidad

print(acelerar())
'''