class Father: 

    def __init__(self):
        print("I'm father instance")

    def message(self):
        print("I'm father class")

    def eyes_color(self):
        print("ligthBlue")

class Children(Father):

    def __init__(self):
        print("I'm children instance")

    def message(self): ## Si este mensaje no existe lo busca en el padre automaticamente.
        print("I'm children class")

    def eyes_color(self):
        super().eyes_color()

fatherOne = Father()
childrenOne = Children()

fatherOne.message()
childrenOne.message()
childrenOne.eyes_color()