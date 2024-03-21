
import random
import string

# ------ Ejercicio 1:
# Escriba una función convertToFahrenheit() con un parámetro degreesCelsius. 
# Esta función devuelve el número de esta temperatura en grados Fahrenheit. 
# - Fahrenheit = Celsius × (9 / 5) + 32

def convertToFahrenheit(degreesCelsius: int) -> int:
    return degreesCelsius * (9 / 5) + 32

# Luego escribe una función llamada convertToCelsius() con un parámetro degreesFahrenheit y 
# devuelve el número de esta temperatura en grados Celsius.
# - Celsius = (Fahrenheit - 32) × (5 / 9)

def convertToCelsius(degreesFahrenheit: int) -> int:
    return (degreesFahrenheit - 32) * (5 / 9)

# ------ Ejercicio 2:
# Escriba una función getHoursMinutesSeconds() que tenga un parámetro totalSeconds. 
# El argumento de este parámetro será el número de segundos a traducir en el número de horas, minutos y segundos. 
# Si la cantidad de horas, minutos o segundos es cero, no lo muestre: 
# la función debe devolver '10m' en lugar de '0h 10m 0s'. La única excepción es que getHoursMinutesSeconds(0) 
# debería devolver '0s'. 

def getHoursMinutesSeconds(totalSeconds: int) -> int:
    seconds = totalSeconds % 60
    min = round(totalSeconds / 60)
    hours = 0
    finalSchedule = ""

    while(min >= 60):
        hours += 1
        min = min -60

    if (hours > 0): finalSchedule += F"{str(hours)}h"
    if (min > 0): finalSchedule += F" {str(min)}m"
    finalSchedule += F" {str(seconds)}s"

    return finalSchedule

# print(getHoursMinutesSeconds(6000000))


# ------ Ejercicio 3:
# Escribe una función generatePassword() que tenga un parámetro length. El parámetro length es un entero 
# de cuántos caracteres debe tener la contraseña generada.
# Por razones de seguridad si length es menor que 12, la función la establece forzosamente a 12 caracteres.     
# La cadena de contraseña devuelta por la función debe tener al menos:
#    minuscula
#    mayuscula
#    numero
#    caracter especial 
# Los caracteres especiales para este ejercicio son ~!@#$%^&*()_

def generatePassword(length: int) -> str:
    specialCharacters = ["~","!","@","#","$","%","^","&","*","(",")","_"]
    password = ""

    if (length < 12): length = 12
   
    while(length > 0):
        aleatorySpecialCharacters = random.choice(specialCharacters)
        aleatoryLowercaseWord = random.choice(string.ascii_lowercase)
        aleatoryUppercaseWord = random.choice(string.ascii_uppercase)
        aleatoryDigit = random.choice(string.digits)
    
        functionsToCreatePassword = [aleatoryLowercaseWord, aleatoryUppercaseWord, aleatoryDigit, aleatorySpecialCharacters]
        random.shuffle(functionsToCreatePassword) ## Hace un random entre las func del array

        password += "".join(functionsToCreatePassword)
        
        length -= 4

    return password

print("PASSWORD: ", generatePassword(2))

# print(random.choice(string.ascii_letters + string.digits + string.punctuation))


