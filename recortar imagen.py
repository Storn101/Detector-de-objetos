import cv2
import os

ruta_entrada = r'C:\Escritorio'

ruta_salida = os.path.join(ruta_entrada, 'recortadas_38x46')
os.makedirs(ruta_salida, exist_ok=True)

ancho, alto = 38, 46

for archivo in os.listdir(ruta_entrada):
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        ruta_img = os.path.join(ruta_entrada, archivo)
        imagen = cv2.imread(ruta_img)

        if imagen is None:
            print(f"No se pudo leer la imagen: {archivo}")
            continue

        imagen_redimensionada = cv2.resize(imagen, (ancho, alto))

        ruta_guardado = os.path.join(ruta_salida, archivo)
        cv2.imwrite(ruta_guardado, imagen_redimensionada)
        print(f"Guardada: {ruta_guardado}")

print("Proceso completado.")
