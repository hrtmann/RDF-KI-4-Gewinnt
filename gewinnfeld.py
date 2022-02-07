import cv2
import numpy as np

class Gewinnfeld:

    def __init__(self):
        # Init-Werte setzen
        self.feldbreite = 120
        self.feldhoehe = 46
        self.offsethoehe = 204

    # Spielfeld zeichnen
    # Übergabe: Webcamframe
    # Rückgabe: Bearbeiteter Webcamframe
    def feld_zeichnen(self, frame):
        # Hauptfeld zeichnen
        frame = cv2.rectangle(frame, (0, 204), (720, 480), (255, 0, 0), thickness=3)

        # Spaltenbegrenzungen setzen
        ran = range(6)
        for x in ran:
            # x-Koordinaten berechnen
            xkoordinate1 = self.feldbreite * x
            ykoordinate1 = self.offsethoehe
            xkoordinate2 = xkoordinate1
            ykoordinate2 = 480
            # Linie setzen
            frame = cv2.line(frame, (xkoordinate1, ykoordinate1), (xkoordinate2, ykoordinate2),
                             (255, 0, 0), thickness=3)

        # Zeilenbegrenzungen setzen
        for x in ran:
            xkoordinate1 = 0
            # y-Koordinaten berechnen
            ykoordinate1 = self.offsethoehe + self.feldhoehe * x

            xkoordinate2 = 720
            ykoordinate2 = ykoordinate1
            # Linie setzen
            frame = cv2.line(frame, (xkoordinate1, ykoordinate1), (xkoordinate2, ykoordinate2),
                             (255, 0, 0), thickness=3)

        return frame

    # Spielsteine in Spielfeld zeichnen
    # Übergabe: Aktueller Frame
    # Rückgabe: Bearbeiteter Frame
    def kreis_zeichnen(self, frame, steinematrix):
        ran = range(6)
        # 2 For-Schleifen in einander, um Kreise in Zeilen und Spalten zu zeichnen
        for x in ran:
            # x-Koordinaten für jeweilige Zeile berechnen
            xkoordinate = (x * self.feldbreite) + (self.feldbreite/2)
            for y in ran:
                # y-Koordinaten für jeweilige Spalte berechnen
                ykoordinate = self.offsethoehe + (y * self.feldhoehe) + (self.feldhoehe / 2)
                # Kreise zeichnen
                frame = cv2.circle(frame, (int(xkoordinate), int(ykoordinate)), 15, (255, 0, 0), thickness=3)

                # Prüfen, ob Spieler schon entsprechende Felder gesetzt haben und dann diese entsprechend zeichnen
                if steinematrix[y][x] == 1.0:
                    frame = cv2.circle(frame, (int(xkoordinate), int(ykoordinate)), 15, (0, 255, 255), thickness=-1)
                elif steinematrix[y][x] == 2.0:
                    frame = cv2.circle(frame, (int(xkoordinate), int(ykoordinate)), 15, (0, 0, 255), thickness=-1)

        return frame
