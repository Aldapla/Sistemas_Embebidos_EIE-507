# Sistema de Vigilancia Inteligente controlado por Raspberry Pi

A continución se explica la metodología de cómo fue realizada la experiencia, considerar que el proyecto se lleva a cabo a través de una VM, en la cual mediante una conexión SSH se controla la 
RaspberryPi , se hace uso de la Interfaz web de motion para poder ver el video en tiempo real, se usa Putty para poder almacenar los videos en la máquina local y luego se usa Matlab para realizar
la detección de Objetos.

Considerar que se pueden encontrar tan solo los pasos globales, me reservo configuraciones y pasos específicos

Daniel Alvarez PLacencia

### Software y Hardware usado

- Máquina virtual con Ubuntu Desktop instalado
- Máquina Fisica local con Windows 11
- Raspberry Pi
- Arduino UNO
- LEDs
- Buzzers
- Cámara web EyeToy


## Configuración del Entorno

1. Conexion SSH:
   ```bash
   ssh usuario@ipraspberry.local
     
2. Actualizar el sistema:
   ```bash
   sudo apt update
   sudo apt upgrade
   
### Instalación de Motion

1. Actualizar el sistema:
   ```bash
   sudo apt update
   sudo apt upgrade
   
2. Instalar Motion:
   ```bash
    sudo apt-get install motion
   
3. Configurar .conf de Motion:
   ```bash
   sudo nano /etc/motion/motion.conf

4. Verificar Status:
   ```bash
   sudo service motion status

### Creación y Ejecución Programa

1. NANO:
   ```bash
   nano Recibir_info_RasoberryPi.py
  
2. Ejecutar:
   ```bash
   python3 Recibir_info_RaspberryPi.py



### Ver la transmición con URL tipo: IP_raspberry:Puerto

### Resultados


   

