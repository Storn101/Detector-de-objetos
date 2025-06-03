import cv2

kirbyClassif = cv2.CascadeClassifier(r'C:cascade.xml')

ancho = 800
alto = 600

print("Selecciona la cámara que deseas usar:")
print("1 - Cámara del celular (IP)")
print("2 - Webcam local")
opcion = input("Ingresa 1 o 2: ")

if opcion == "1":
    url = 'http://192/video'
    cap = cv2.VideoCapture(url)
    fuente = "Celular (IP)"
elif opcion == "2":
    cap = cv2.VideoCapture(0)
    fuente = "Webcam local"
else:
    print("Opción no válida. Saliendo.")
    exit()

ret, frame = cap.read()
if not ret:
    print(f"No se pudo acceder a la camara seleccionada: {fuente}")
    cap.release()
    cv2.destroyAllWindows()
    exit()

print(f"Usando camara: {fuente}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se puede leer el video.")
        break

    frame = cv2.resize(frame, (ancho, alto))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = kirbyClassif.detectMultiScale(
        gray,
        scaleFactor=5,
        minNeighbors=1000,
        minSize=(70, 78) )
    for (x, y, w, h) in toy:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (8, 255, 0), 2)
        cv2.putText(frame, "Kirby", (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f"Camara: {fuente}", (10, 25), 2, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow(f'Reconocimiento Kirby - {fuente}', frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()