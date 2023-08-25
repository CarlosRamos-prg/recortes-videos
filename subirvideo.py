import cv2
import numpy as np
import pyautogui

# Cargar la imagen que deseas buscar
imagen_a_buscar = cv2.imread('imagen_objetivo.JPG')

while True:
    # Capturar una captura de pantalla
    captura = pyautogui.screenshot()

    # Convertir la captura de pantalla a un arreglo NumPy
    captura_np = np.array(captura)

    # Buscar la imagen en la captura de pantalla
    resultado = cv2.matchTemplate(captura_np, imagen_a_buscar, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    # Establecer un umbral de confianza
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Imagen encontrada
        altura, ancho, _ = imagen_a_buscar.shape
        top_left = max_loc
        bottom_right = (top_left[0] + ancho, top_left[1] + altura)
        cv2.rectangle(captura_np, top_left, bottom_right, (0, 255, 0), 2)
        ventana_pequeña = cv2.resize(captura_np, (800, 600))
        cv2.imshow('Resultado', ventana_pequeña)
        print("Imagen encontrada.")
    else:
        print("Imagen no encontrada.")

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
