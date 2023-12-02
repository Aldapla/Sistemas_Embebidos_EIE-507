# Recibir información del Arduino y tomar deciciones con respecto a la grabación en stream de Motion
# By Daniel Alvarez Placencia


# bibliotecas
import serial
import subprocess
import time

// Variables
SERIAL_PORT = '/dev/ttyACM0'  # Puerto serie del Arduino
BAUD_RATE = 9600  # Comunicación
DISTANCE_THRESHOLD = 10  # Umbral de distancia en cm
WAIT_TIME_SECONDS = 300  # Tiempo de espera después de detener la grabación

# puerto serie
puerto_serie = serial.Serial(SERIAL_PORT, BAUD_RATE)


# Función para iniciar la grabación cuando se detecta un intruso
def iniciar_grabacion():
    print("Intruso Detectado a {} cm !!! Grabando...".format(distancia))
    subprocess.run(["sudo", "service", "motion", "start"])

# Función para detener la grabación cuando no se detecta nada anormal
def detener_grabacion():
    print("No se detecta nada anormal... Dejando de Grabar...")
    subprocess.run(["sudo", "service", "motion", "stop"])


# Variable bool para rastrear el estado de la grabación
grabacion_activa = False

try:
    while True:
        # Leer desde el puerto serie y decodificar la lectura
        lectura_serial = puerto_serie.readline().decode('utf-8').strip()

        # convertir la lectura a un número
        try:
            distancia = int(lectura_serial)
        except ValueError:
            continue

        # Lógica para iniciar o detener la grabación basada en la distancia
        if distancia < DISTANCE_THRESHOLD and not grabacion_activa:
            iniciar_grabacion()
            grabacion_activa = True
        elif distancia >= DISTANCE_THRESHOLD and grabacion_activa:
            detener_grabacion()
            grabacion_activa = False
            time.sleep(WAIT_TIME_SECONDS)

except KeyboardInterrupt:
    # Cerrar el puerto serie al salir
    puerto_serie.close()

