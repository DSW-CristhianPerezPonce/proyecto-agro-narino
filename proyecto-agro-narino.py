import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
#creando csv
with open('weather_data.csv', 'w') as f:
    f.write('day,temp,condition\n')
    f.write('Monday,12,Sunny\n')
    f.write('Tuesday,14,Rain\n')
    f.write('Wednesday,15,Rain\n')
    f.write('Thursday,14,Cloudy\n')
    f.write('Friday,21,Sunny\n')
    f.write('Saturday,22,Sunny\n')
    f.write('Sunday,24,Sunny\n')
# Cargar datos desde el archivo CSV
# Usando la librería CSV para leer el archivo
import csv
with open('weather_data.csv') as data_file:
    # Se recorre el archivo y se crea un iterable en data
    data = csv.reader(data_file)
    print("Contenido del CSV usando librería CSV:")
    for row in data:
        print(row)
# Usando la librería pandas para leer el archivo
print("\nContenido del CSV usando Pandas:")
df_weather = pd.read_csv('weather_data.csv')
print(df_weather) 
# con pandas queda mejor visualizado
print("\nCreando una Serie básica:")
s = pd.Series(['Mark', 'Justin', 'John', 'Vicky'], dtype='string')
print(s)
# Creando un indicides personalizados

# Creando una Serie con índices personalizados
print("\nCreando una Serie con índices personalizados:")
s = pd.Series(['Mark', 'Justin', 'John', 'Vicky'], index=[222, 333, 444, 555], dtype='string')
print(s)
# Creando una Serie con un indices estudiantes
print("\nEjemplo de Serie con notas de estudiantes:")
notas = [5.7, 8.5, 9.1, 5.5, 8.2, 9.0, 10, 7.0, 7.7, 9.9]
estudiantes = ["Juan", "Jennifer", "David", "Pablo", "Armando", "Magdalena", "Francesca", "Rosmery", "Vicente", "Martin"]
calificaciones = pd.Series(notas, index=estudiantes)
print(calificaciones)
# Creando Series desde un diccionario
print("\nCreando Series desde un diccionario:")
new_dict = {
    "Matemáticas": 8.0,
    "Programación": 7.7,
    "Inglés": 8.2
}
s_dict = pd.Series(new_dict)
print(s_dict)

# Usando range
print("\nCreando Series desde range():")
s_range = pd.Series(range(10,), index=range(1, 11))
print(s_range)

