# disenoRaspberry

# Ejercicio No. 1

Este ejercicio implementa una simulación básica de un semáforo vehicular utilizando tres salidas GPIO de la **Raspberry Pi** controladas desde Python mediante la librería `gpiozero`. El programa configura cada pin como salida digital y ejecuta una secuencia cíclica donde los LEDs verde, amarillo y rojo se activan durante intervalos de tiempo definidos, empleando retardos por software con la función `sleep()`. El objetivo es introducir los fundamentos del control digital en sistemas embebidos basados en Linux, comprendiendo la relación entre nivel lógico (3.3 V / 0 V), temporización secuencial y ejecución continua dentro de un bucle infinito (`while True`), equivalente conceptual al modelo `loop()` en microcontroladores.
