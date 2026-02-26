"""
=====================================================================================
 Bienvenidos a Sys On Chip
=====================================================================================
 Ejercicio No. 2 – Implementación de un semáforo mediante Máquina de Estados (FSM)

 Descripción general:
 Este programa implementa el control de un semáforo vehicular utilizando
 una Máquina de Estados Finitos (Finite State Machine - FSM).

 A diferencia del Ejercicio No. 1, aquí no se utiliza sleep() para bloquear
 el flujo del programa durante largos periodos de tiempo. En su lugar,
 se emplea temporización no bloqueante basada en la función time().

 Objetivos de aprendizaje:

  1) Introducir el concepto formal de estado en sistemas embebidos.
  2) Implementar transiciones controladas por tiempo.
  3) Separar lógica de control y temporización.
  4) Evitar bloqueos prolongados del sistema.

 Estados definidos:

      - ESTADO_VERDE
      - ESTADO_AMARILLO
      - ESTADO_ROJO

 El sistema evalúa continuamente el tiempo transcurrido y realiza
 transiciones cuando se cumple el intervalo configurado.

 Nota técnica importante:
 Este enfoque es más profesional que el uso directo de sleep(),
 ya que permite que el sistema pueda ampliarse fácilmente para
 responder a eventos externos (botones, sensores, comunicación, etc.).
=====================================================================================
 Plataforma: Raspberry Pi
 Lenguaje: Python 3
 Librería: gpiozero
=====================================================================================
"""

# ==============================
# Importación de librerías
# ==============================

from gpiozero import LED      # Control de salidas digitales
from time import sleep, time  # Temporización no bloqueante


# ==============================
# Configuración de hardware
# ==============================
# Numeración BCM del SoC Broadcom

GPIO_VERDE = 17
GPIO_AMARILLO = 27
GPIO_ROJO = 22


# ==============================
# Inicialización de dispositivos
# ==============================

led_verde = LED(GPIO_VERDE)
led_amarillo = LED(GPIO_AMARILLO)
led_rojo = LED(GPIO_ROJO)


# ==============================
# Parámetros temporales (segundos)
# ==============================

TIEMPO_VERDE = 5
TIEMPO_AMARILLO = 1
TIEMPO_ROJO = 5


# ==============================
# Definición de estados (FSM)
# ==============================
# Cada estado representa una condición estable del sistema.

ESTADO_VERDE = 0
ESTADO_AMARILLO = 1
ESTADO_ROJO = 2


# Estado inicial del sistema
estado_actual = ESTADO_VERDE

# Variable para almacenar el instante en que ocurrió
# la última transición de estado
tiempo_referencia = time()


# ==============================
# Bucle principal
# ==============================
# Evaluación continua del sistema (firmware en ejecución)

while True:

    # Captura del tiempo actual
    tiempo_actual = time()

    # ==========================
    # ESTADO VERDE
    # ==========================
    if estado_actual == ESTADO_VERDE:

        led_verde.on()
        led_amarillo.off()
        led_rojo.off()

        # Condición de transición
        if tiempo_actual - tiempo_referencia >= TIEMPO_VERDE:
            tiempo_referencia = tiempo_actual
            estado_actual = ESTADO_AMARILLO

    # ==========================
    # ESTADO AMARILLO
    # ==========================
    elif estado_actual == ESTADO_AMARILLO:

        led_verde.off()
        led_amarillo.on()
        led_rojo.off()

        if tiempo_actual - tiempo_referencia >= TIEMPO_AMARILLO:
            tiempo_referencia = tiempo_actual
            estado_actual = ESTADO_ROJO

    # ==========================
    # ESTADO ROJO
    # ==========================
    elif estado_actual == ESTADO_ROJO:

        led_verde.off()
        led_amarillo.off()
        led_rojo.on()

        if tiempo_actual - tiempo_referencia >= TIEMPO_ROJO:
            tiempo_referencia = tiempo_actual
            estado_actual = ESTADO_VERDE

    # Pequeña pausa para evitar consumo excesivo de CPU
    sleep(0.01)
