import cv2

def capture_image():
    """
    Captura una imagen desde la cámara.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("No se pudo acceder a la cámara.")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise Exception("No se pudo capturar la imagen.")
    return frame
