# disenoRaspberry

# Ejercicio No. 1

Este ejercicio implementa una simulación básica de un semáforo vehicular utilizando tres salidas GPIO de la **Raspberry Pi** controladas desde Python mediante la librería `gpiozero`. El programa configura cada pin como salida digital y ejecuta una secuencia cíclica donde los LEDs verde, amarillo y rojo se activan durante intervalos de tiempo definidos, empleando retardos por software con la función `sleep()`. El objetivo es introducir los fundamentos del control digital en sistemas embebidos basados en Linux, comprendiendo la relación entre nivel lógico (3.3 V / 0 V), temporización secuencial y ejecución continua dentro de un bucle infinito (`while True`), equivalente conceptual al modelo `loop()` en microcontroladores.

# Ejercicio No. 2

Este ejercicio implementa un semáforo vehicular utilizando el modelo de **Máquina de Estados Finitos (FSM)** sobre la Raspberry Pi, elevando el nivel respecto al enfoque secuencial del ejercicio anterior. El programa define estados explícitos (verde, amarillo y rojo) y gestiona las transiciones mediante temporización no bloqueante usando la función `time()`, evitando retardos prolongados que detengan completamente la ejecución. Esta arquitectura permite separar claramente la lógica de control del mecanismo de temporización, haciendo el sistema más escalable y profesional, y preparándolo para futuras extensiones como manejo de botones, sensores o comunicación externa sin comprometer la capacidad de respuesta del sistema.
