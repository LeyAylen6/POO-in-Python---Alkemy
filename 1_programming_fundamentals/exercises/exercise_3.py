# 3. Crea una función llamada verificar_calificacion(check_score) que reciba tres parámetros: 
        # - nota1(firsNote) 
        # - nota2(secondNote) 
        # - nota3(thirdNote)
    # ↪ Dentro de la función calcular el promedio de notas
    # ↪ Si el promedio es mayor o igual a 6, entonces la función debe retornar un mensaje “Aprobado”, 
    # en caso contrario “Reprobado”

def check_score(firsNote, secondNote, thirdNote):
    average = (firsNote + secondNote + thirdNote) / 3

    if average >= 6: return "Aprobado"
    else: return "Reprobado"