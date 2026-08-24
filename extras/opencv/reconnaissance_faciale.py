# cv2: installer package opencv-python
# les fichiers haarcascade_frontalface_default.xml, haarcascade_eye.xml et haarcascade_smile.xml sont disponibles à :
# https://github.com/opencv/opencv/tree/master/data/haarcascades ou dans le répertoire data du package


import cv2


class ReconnaissanceFaciale:
    def __init__(self):
        # On charge le modèle pré-entraîné pour la reconnaissance faciale
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # On charge le modèle pré-entraîné pour la reconnaissance des yeux
        self.eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        # On charge le modèle pré-entraîné pour la reconnaissance du sourire
        self.smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
        self.capture_video = cv2.VideoCapture(0)

        self.executer()

    def detection_faces(self, frame_video):
        # On convertit l'image en niveaux de gris
        image_gris = cv2.cvtColor(frame_video, cv2.COLOR_BGR2GRAY)
        # On détecte les visages
        faces = self.face_cascade.detectMultiScale(image_gris, 1.3, 5)
        # On dessine un rectangle autour des visages
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_video, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = image_gris[y:y + h, x:x + w]
            roi_color = frame_video[y:y + h, x:x + w]
            # On détecte les yeux
            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # On détecte les sourires
            smiles = self.smile_cascade.detectMultiScale(roi_gray)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
        return faces

    def executer(self):
        while True:
            ret, frame_video = self.capture_video.read()
            self.detection_faces(frame_video)
            cv2.imshow('Reconnaissance faciale', frame_video)
            # Touche d'échappement pour quitter (esc)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        self.capture_video.release()
        cv2.destroyAllWindows()


app = ReconnaissanceFaciale()
