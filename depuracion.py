def calcular_promedio(calificaciones):
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion
    promedio = suma / 5
    return promedio

notas = [90, 85, 100, 95]
resultado = calcular_promedio(notas)
print('Promedio:', resultado)
