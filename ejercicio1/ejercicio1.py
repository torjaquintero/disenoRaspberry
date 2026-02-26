"""
=====================================================================================
 Bienvenidos a Sys On Chip
=====================================================================================
 Ejercicio No. 1 – Simulación básica de un semáforo con Raspberry Pi

 Descripción general:
 Este programa implementa la simulación del funcionamiento de un semáforo
 vehicular utilizando tres LEDs conectados a pines GPIO de la Raspberry Pi.

 El objetivo es introducir los fundamentos del control de salidas digitales
 en sistemas embebidos basados en Linux:

  1) Configuración de pines GPIO como salidas digitales.
  2) Escritura de niveles lógicos HIGH (3.3V) y LOW (0V).
  3) Control temporal mediante retardos por software usando sleep().

 Secuencia de funcionamiento:

      - LED Verde    → encendido durante 5 segundos.
      - LED Amarillo → encendido durante 1 segundo.
      - LED Rojo     → encendido durante 5 segundos.

 Esta secuencia se repite indefinidamente dentro de un bucle while True,
 simulando el comportamiento continuo de un sistema embebido.

 Nota técnica importante:
 La función sleep() bloquea la ejecución del programa durante el tiempo
 especificado. Este enfoque es adecuado para un ejercicio introductorio,
 pero no es apropiado para sistemas que requieran multitarea o respuesta
 a eventos externos en tiempo real.
=====================================================================================
 Plataforma: Raspberry Pi
 Lenguaje: Python 3
 Librería: gpiozero
=====================================================================================
"""

# ==============================
# Importación de librerías
# ==============================

from gpiozero import LED      # Permite controlar pines GPIO como salidas digitales
from time import sleep        # Función para generar retardos en segundos


# ==============================
# Definición de pines GPIO (BCM)
# ==============================
# Se usa numeración BCM (SoC Broadcom), no numeración física del conector.

GPIO_VERDE = 17
GPIO_AMARILLO = 27
GPIO_ROJO = 22


# ==============================
# Creación de objetos LED
# ==============================
# Cada objeto LED configura automáticamente el pin como salida.

led_verde = LED(GPIO_VERDE)
led_amarillo = LED(GPIO_AMARILLO)
led_rojo = LED(GPIO_ROJO)


# ==============================
# Tiempos del sistema (segundos)
# ==============================

TIEMPO_VERDE = 5
TIEMPO_AMARILLO = 1
TIEMPO_ROJO = 5


# ==============================
# Bucle principal
# ==============================
# En sistemas embebidos, este bucle representa
# el firmware ejecutándose de manera continua.

while True:

    # ===== ESTADO VERDE =====
    led_verde.on()        # Nivel lógico alto → 3.3V
    led_amarillo.off()    # Nivel lógico bajo → 0V
    led_rojo.off()
    sleep(TIEMPO_VERDE)

    # ===== ESTADO AMARILLO =====
    led_verde.off()
    led_amarillo.on()
    led_rojo.off()
    sleep(TIEMPO_AMARILLO)

    # ===== ESTADO ROJO =====
    led_verde.off()
    led_amarillo.off()
    led_rojo.on()
    sleep(TIEMPO_ROJO)
