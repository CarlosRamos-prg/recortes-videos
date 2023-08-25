import cv2
import numpy as np
import pyautogui
import time

# Cargar la imagen que deseas buscar
imagen_a_buscar = cv2.imread('imagen_objetivo.JPG')

contador=0

while True:

    contador=contador+1
    # Capturar una captura de pantalla
    captura = pyautogui.screenshot()

    # Convertir la captura de pantalla a un arreglo NumPy
    captura_np = np.array(captura)

    # Buscar la imagen en la captura de pantalla
    resultado = cv2.matchTemplate(captura_np, imagen_a_buscar, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)

    # Obtener las coordenadas del punto más cercano de coincidencia
    altura, ancho, _ = imagen_a_buscar.shape
    top_left = max_loc
    bottom_right = (top_left[0] + ancho, top_left[1] + altura)

    # Dibujar un rectángulo alrededor del objeto encontrado
    cv2.rectangle(captura_np, top_left, bottom_right, (0, 255, 0), 2)

    # Mostrar la captura con el rectángulo dibujado (ventana más pequeña)
    ventana_pequeña = cv2.resize(captura_np, (800, 600))

    if(contador==1 or contador==2):
        # Mostrar la captura con el rectángulo dibujado
        cv2.imshow('Resultado', ventana_pequeña)

    print("Esperando 3 segundos...")
    time.sleep(3)  # Espera durante 3 segundos
    print("¡Han pasado 3 segundos!")

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
