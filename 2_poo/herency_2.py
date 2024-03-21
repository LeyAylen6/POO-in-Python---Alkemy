class Person:

    def __init__(self, name, age, dni):
        self.name = name
        self.age = age
        self.dni = dni

    def __str__(self):
        return F"Person's name is {self.name} with DNI {self.dni}"

class Company:

    def getOwner(self): 
        return "TESLA"

    def getSalary(self): 
        return 5_000_000


class Employee(Person, Company): ## Tiene prioridad el primero en caso de que tengan props con nombres iguales.
    def __init__(self, name, age, dni, file, healthCoverage ):
        super().__init__(name, age, dni)
        self.file = file
        self.healtCoverage = healthCoverage

    def __str__(self): ## Si no se declara trae el del padre.
        return F"File {self.file} corresponds to {self.name}"

firstEmployee = Employee("Pepe", 55, 32225566, 1, "OSDE")

print(type(firstEmployee))
print("name:", firstEmployee.name)
print("age:", firstEmployee.age)
print("dni:", firstEmployee.dni)
print("owner:", firstEmployee.getOwner())
print(firstEmployee.getSalary())
