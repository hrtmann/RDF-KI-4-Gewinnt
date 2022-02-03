# importiere Numpy und OpenCV
import numpy as np
import cv2
# importiere Klassen
from gestenErkennung import gesten
from gewinnfeld import Gewinnfeld
from spaltenerkennung import SpalteErkennen
from gewinnueberpruefung import Gewinnueberpruefung

# erzeuge Objekte aus Klassen
GewinnfeldZeichnen = Gewinnfeld()
GesteErkennen = gesten()
SpaltenErkennung = SpalteErkennen()
GewinnPruefung = Gewinnueberpruefung()

# Laufvariable einführen => 99 = keiner gewonnen; Spieler 1 beginnt
spielergewonnen = 99
aktiverspieler = 1.0
# 6 x 6 Matrix für Spielsteine erzeugen
steinematrix = np.zeros(36).reshape(6, 6)

# Kamera öffnen
cap = cv2.VideoCapture(0)
# Prüfen ob Webcam funktioniert
if not cap.isOpened():
    raise IOError("Webcam Fehler!")

# Speicher Frame Abmessungen für Sizing
ret, frame = cap.read()
format = frame.shape

while True:
    # Lese Frame ein
    ret, frame = cap.read()
    # Passe Frame auf 720x480 fest an
    frame = cv2.resize(frame, None, fx=720 / format[1], fy=480 / format[0], interpolation=cv2.INTER_AREA)

    # Ausführen solange kein Spieler gewonnen hat
    if spielergewonnen == 99:
        # Geste erkennen
        frame, gedrueckt, position_x = GesteErkennen.erkenne_geste(frame)
        # Spielfeld zeichnen
        frame = GewinnfeldZeichnen.feld_zeichnen(frame)
        # Erkannte Spalte zeichnen und Steinmatrix befüllen falls Stein gesetzt wurde
        frame, steinematrix, aktiverspieler = SpaltenErkennung.linie_zeichnen(position_x, gedrueckt, steinematrix, aktiverspieler, frame)
        # Spielsteine auf Matrix Basis zeichnen
        frame = GewinnfeldZeichnen.kreis_zeichnen(frame, steinematrix)
        # Prüfen ob Spieler gewonnen hat
        spielergewonnen = GewinnPruefung.ueberpruefe_gewinn(steinematrix)

    # Spieler hat gewonnen:
    else:
        # Gewinner Namen einblenden
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, "Spieler: " + str(spielergewonnen) + " hat gewonnen!", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        # Spielfeld zeichnen
        frame = GewinnfeldZeichnen.feld_zeichnen(frame)
        # Spielsteine auf Matrix Basis zeichnen
        frame = GewinnfeldZeichnen.kreis_zeichnen(frame, steinematrix)

    # Frame Größe zum anzeigen vergrößern
    frame = cv2.resize(frame, None, fx=1.6, fy=1.6, interpolation=cv2.INTER_AREA)
    # Frame anzeigen
    cv2.imshow('KI-4-Gewinnt IAV3/RDF', frame)

    # Prüfen ob 'ESC' gedrückt wurde, um Programm zu beenden
    c = cv2.waitKey(1)
    if c == 27:
        break

# Programm beenden
cap.release()
cv2.destroyAllWindows()
