import time


class Rettangolo():

    def __init__(self):

        self.area = 0
        self.base = 0
        self.altezza = 0

    def calcola_area(self):
        
        self.area = self.base*self.altezza

class Cerchio():

    def __init__(self):

        self.raggio = 0.0
        area = 0.0

    def calcola_area_cerchio(self):
        
        self.area = (self.raggio) * (self.raggio) * 3.14



class Triangolo():

    def __init__(self):
        
        self.base = 0.0
        self.altezza = 0.0
        area = 0.0

    def calcola_area_triangolo(self):
        
        self.area = (self.base*self.altezza)/2

               
