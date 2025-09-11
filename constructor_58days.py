# contructor
#format hai yeh __INit krke 
class Person:
    def __init__(self,name , occpation):
        self.name=name
        self.occupation=occpation

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a=Person("Swarupa","dev")
a.info()