class Dot:

    def __init__ (self, x, y):
        self.__x = x
        self.__y = y
    
    def __add__(self, other):
        return Dot(self.__x + other.__x, self.__y + other.__y)
    
    def __sub__ (self, other):
        return Dot(self.__x - other.__x, self.__y - other.__y)
    
    def __str__ (self):
        return F"({self.__x}, {self.__y})"
    
dot1 = Dot(5, 9)
dot2 = Dot(1, 1)

print(dot1 + dot2)
print(dot1 - dot2)