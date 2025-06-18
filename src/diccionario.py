# Diccionario de Sensores
sensor_lluvia = {
    "modelo": "DF Robot",
    "voltaje": 3.3,
    "numero_puerto": 4,
    "funcionamiento": "Normal",
    "estado_activacion": True
}

#Impresion de las carcateristicas del sensor

print(f"\nSensor de Lluvia: {sensor_lluvia}")
print(f"\nEl modelo del modelo es: {sensor_lluvia ['modelo']}")

#Cambiar valores 

sensor_lluvia["modelo"] = "Siemens"
print(f"\nEl nuevo modelo es: {sensor_lluvia['modelo']}"  )