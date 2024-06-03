class vehicle:
    def __init__(self, brand, model,year,speed):
        print("values are assigned ")
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=speed
    
    def accelerate(self):
        pass
    def brake(self):
        pass
    def honk(self):
        pass
        
class car(vehicle):
    def accelerator(self):
       pass
    def brake(self):
        pass
    def honk(self):
        pass
    
    def details(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)
        

obj1=vehicle("tata","XUV","2017","210KMPH")
obj2=car("audi","speedcar","2023","420KMPH")
obj2.accelerator()
obj2.details()
obj2.details()