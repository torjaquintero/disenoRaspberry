"""
=====================================================================================
 Bienvenidos a Sys On Chip
=====================================================================================
 Ejercicio No. 3 – Semáforo con botón robusto (Raspberry Pi)

 Versión avanzada:
  - Evento aceptado únicamente en estado VERDE
  - Debounce explícito por software
  - Protección ante condiciones de carrera (thread-safe)
  - Arquitectura FSM con evento asincrónico

 Descripción técnica:

 Este ejercicio implementa una Máquina de Estados Finitos (FSM) que
 integra un evento externo (botón de peatón) gestionado mediante
 callbacks en un entorno Linux.

 A diferencia de un microcontrolador como Arduino, donde las
 interrupciones son gestionadas directamente por hardware
 (ISR con latencia determinística), en Raspberry Pi los eventos
 GPIO son administrados por el kernel de Linux y ejecutados
 en hilos separados.

 Esto introduce un problema potencial:
      Condiciones de carrera (race conditions)

 Por ello se utiliza un Lock (threading.Lock) para proteger
 las variables compartidas entre el hilo principal y el
 callback del botón.

 Este diseño se aproxima más a arquitecturas profesionales
 utilizadas en sistemas embebidos de mayor complejidad.

=====================================================================================
 Plataforma: Raspberry Pi
 Lenguaje: Python 3
 Librería: gpiozero
=====================================================================================
"""

# ==============================
# Importación de librerías
# ==============================

from gpiozero import LED, Button
from time import time, sleep
from threading import Lock


# ==============================
# Configuración de hardware (BCM)
# ==============================

GPIO_VERDE = 17
GPIO_AMARILLO = 27
GPIO_ROJO = 22
GPIO_BOTON = 23


# ==============================
# Inicialización de dispositivos
# ==============================

led_verde = LED(GPIO_VERDE)
led_amarillo = LED(GPIO_AMARILLO)
led_rojo = LED(GPIO_ROJO)

# Debounce de 200 ms para eliminar rebotes mecánicos
boton = Button(GPIO_BOTON, pull_up=True, bounce_time=0.2)


# ==============================
# Parámetros temporales
# ==============================

TIEMPO_VERDE = 5
TIEMPO_AMARILLO = 1
TIEMPO_ROJO = 5


# ==============================
# Definición de estados (FSM)
# ==============================

ESTADO_VERDE = 0
ESTADO_AMARILLO = 1
ESTADO_ROJO = 2

estado_actual = ESTADO_VERDE
tiempo_referencia = time()

# Bandera de solicitud peatonal
solicitud_peaton = False

# Lock para proteger acceso concurrente
lock = Lock()


# ==============================
# Callback del botón (evento asincrónico)
# ==============================

def evento_boton():
    global solicitud_peaton, estado_actual

    # Protección de sección crítica
    with lock:
        # Aceptar evento solo si el sistema está en VERDE
        if estado_actual == ESTADO_VERDE:
            solicitud_peaton = True


# Asociar el evento al botón
boton.when_pressed = evento_boton


# ==============================
# Bucle principal (FSM)
# ==============================

while True:

    tiempo_actual = time()

    # Copia protegida de variables compartidas
    with lock:
        estado = estado_actual
        solicitud = solicitud_peaton

    # ==========================
    # ESTADO VERDE
    # ==========================
    if estado == ESTADO_VERDE:

        led_verde.on()
        led_amarillo.off()
        led_rojo.off()

        if solicitud:
            with lock:
                solicitud_peaton = False
                estado_actual = ESTADO_AMARILLO
            tiempo_referencia = tiempo_actual

        elif tiempo_actual - tiempo_referencia >= TIEMPO_VERDE:
            with lock:
                estado_actual = ESTADO_AMARILLO
            tiempo_referencia = tiempo_actual


    # ==========================
    # ESTADO AMARILLO
    # ==========================
    elif estado == ESTADO_AMARILLO:

        led_verde.off()
        led_amarillo.on()
        led_rojo.off()

        if tiempo_actual - tiempo_referencia >= TIEMPO_AMARILLO:
            with lock:
                estado_actual = ESTADO_ROJO
            tiempo_referencia = tiempo_actual


    # ==========================
    # ESTADO ROJO
    # ==========================
    elif estado == ESTADO_ROJO:

        led_verde.off()
        led_amarillo.off()
        led_rojo.on()

        if tiempo_actual - tiempo_referencia >= TIEMPO_ROJO:
            with lock:
                estado_actual = ESTADO_VERDE
            tiempo_referencia = tiempo_actual


    # Pequeña pausa para reducir uso de CPU
    sleep(0.01)
