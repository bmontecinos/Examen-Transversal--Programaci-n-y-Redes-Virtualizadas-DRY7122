def calcular_duracion(distancia):
    velocidad_promedio = 80  # km/h
    duracion_en_horas = distancia / velocidad_promedio
    duracion_en_minutos = duracion_en_horas * 60
    duracion_en_segundos = duracion_en_minutos * 60
    return duracion_en_horas, duracion_en_minutos, duracion_en_segundos

def calcular_combustible(distancia):
    rendimiento_vehiculo = 12  # km/l
    combustible = distancia / rendimiento_vehiculo
    return round(combustible, 1)

# Datos de entrada
print ("Se realizara el calculo de distancia entre la ciudad de Santiago, Chile. Hasta una de las ciudades de Buenos Aires(Argentina), Lima(Peru), y Caracas (Venezuela)")
ciudad_origen = "Santiago"
ciudad_destino = input("Seleccione la ciudad de destino (Buenos Aires, Lima, Caracas): ")

# Calcular la distancia
distancia = 0  # Valor predeterminado para mostrar en caso de que no se encuentre una ciudad de destino válida

#Distancia en Km desde Santiago a otras ciudades
if ciudad_destino.lower() == "buenos aires":
    distancia = 1406
elif ciudad_destino.lower() == "lima":
    distancia = 3276
elif ciudad_destino.lower() == "caracas":
    distancia = 7293

if distancia == 0:
    print("Ciudad de destino inválida. Por favor, elige una de las siguientes opciones: Buenos Aires, Lima, Caracas.")
else:
    # Calcular la duración y el combustible
    duracion_en_horas, duracion_en_minutos, duracion_en_segundos = calcular_duracion(distancia)
    combustible = calcular_combustible(distancia)

    # Mostrar resultados
    print("Ciudad de Origen:", ciudad_origen)
    print("Ciudad de Destino:", ciudad_destino)
    print("Distancia:", distancia, "km")
    print("Duración del viaje:", duracion_en_horas, "horas,", duracion_en_minutos, "minutos,", duracion_en_segundos, "segundos")
    print("Combustible requerido:", combustible, "litros")

    # Salida adicional
    print("S")
 
