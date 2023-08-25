import pyautogui
import time

# Obtener la posición actual del mouse
posicion_actual = pyautogui.position()
print("Posición actual del mouse:", posicion_actual)

# Mover el mouse a una posición específica
nueva_posicion = (100, 100)
pyautogui.moveTo(nueva_posicion[0], nueva_posicion[1], duration=2)

# Esperar un momento
time.sleep(1)

# Regresar el mouse a la posición original
pyautogui.moveTo(posicion_actual[0], posicion_actual[1], duration=2)

print("Movimiento del mouse completado.")
