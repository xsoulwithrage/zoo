class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.vida = 50
        self.felicidad = 50
        
    def información(self):
        print(f"{self.nombre}: Vida - {self.vida}, Felicidad - {self.felicidad}")
        
    def alimentar(self):
        self.vida += 10
        self.felicidad += 10
        

class León(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.melenas = 2 
        self.vida = 60    
        self.felicidad = 40
        
    def alimentar(self):
        self.vida += 15   
        self.felicidad += 5


class Tigre(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.rayas = 100
        self.vida = 70
        self.felicidad = 30
        
    def alimentar(self):
        self.vida += 20
        self.felicidad += 0


class Oso(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.hibernando = False
        self.vida = 80
        self.felicidad = 20
        
    def alimentar(self):
        self.vida += 5
        self.felicidad += 15

León = León("Simba", 5)
Tigre = Tigre("Tony", 3)
Oso = Oso("Yogi", 8)

León.información()
Tigre.información()
Oso.información()

León.alimentar()
Tigre.alimentar()
Oso.alimentar()

León.información()
Tigre.información()
Oso.información()
