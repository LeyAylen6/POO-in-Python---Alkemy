diccionario_persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# -----------------------------------------------------------------------------
## _name = para que sea oculto

class Test:

    # Los tipados son solo sugerencia, no te obliga a cumplirlos.
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def __str__(self) -> str:
        return F"-> name: {self.name}, age: {self.age}"

    @property ## Getter
    def name(self):
        return self._name
    
    @name.setter ## Setter
    def name(self, name): ## Sobrecarga del getter.
        if (type(name) == str):
            self._name = name
        else:
            self.name = ""
            print("-> Incorrect value for name")

    @property 
    def age(self):
        return self._age
    
    @age.setter 
    def age(self, age): 
        if (type(age) == int):
            self._age = age
        else:
            self.age = 0
            print("-> Incorrect value for Age")

invalidObject= Test(1, "hola")
correctObject = Test("Leila", 23)

print("I'm correct correctObject.__name: ", correctObject.__name)
print("I'm correct object: ", correctObject)
print("I'm invalid object: ", invalidObject)

# -----------------------------------------------------------------------------

class Martian: ## Marciano
    quantity = 0

    @classmethod
    def born(cls): ## cls -> referencia a la clase
        cls.quantity += 1

    @classmethod
    def die(cls):
        cls.quantity -= 1
        
    def __init__ (self, name):
        self.name = name
        Martian.born()
        print(F"{self.name} born")

    def __del__ (self): 
        Martian.die()
        print(F"{self.name} died")

nachin = Martian("Nachin")
ley = Martian("Ley")
other = Martian("Otro")

print(Martian.quantity)
del(other)
print(Martian.quantity)