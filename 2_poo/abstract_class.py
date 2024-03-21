from abc import ABCMeta, abstractmethod 
# ABC = Abstact base class
# Podes importar solo ABC en lugar de ABCMeta y que MyAbstractClass sea class MyAbstractClass(ABC): 

class MyAbstractClass(metaclass=ABCMeta):
    
    @abstractmethod # @abstractmethod hace que funcione como una interfaz y te obligue a tenerlo en su hijo.
    def first_ABC_method(self):
        pass

    @abstractmethod
    def second_ABC_method(self):
        pass

class myClass(MyAbstractClass): 
    
    def first_ABC_method(self):
        print("I'm a first ABC method")

    def second_ABC_method(self):
         print("I'm a first ABC method")

firstABC = myClass()
print(firstABC)