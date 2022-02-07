import cv2


class SpalteErkennen:

    def __init__(self):
        pass

    # Aktuelle Spalte erkennen und Nutzer anzeigen, damit dieser weiß wo Spielstein gesetzt werden würde
    # Wenn gesetzt wurde, Matrix befüllen und aktuellen Spieler ändern
    # Übergabe: Fingerposition, Spielfeldmatrix, Aktueller Spieler, Aktueller Frame
    # Rückgabe: Bearbeiteter Frame, Bearbeitete Spielfeldmatrix, Neuer Spieler
    def linie_zeichnen(self, x, gedrueckt, steinematrix, aktiverspieler, frame):
        # Angabe falls keine Spalte erkannt wurde
        spalte = 99
        # X-Koordinate auf Spalten-Index prüfen
        if x > 0 and x <= 120:
            cv2.line(frame, (1, 150), (1, 480), (0, 255, 0), thickness=2)
            cv2.line(frame, (120, 150), (120, 480), (0, 255, 0), thickness=2)
            spalte = 0
        elif x > 120 and x <= 240:
            cv2.line(frame, (120, 150), (120, 480), (0, 255, 0), thickness=2)
            cv2.line(frame, (240, 150), (240, 480), (0, 255, 0), thickness=2)
            spalte = 1
        elif x > 240 and x <= 360:
            cv2.line(frame, (240, 150), (240, 480), (0, 255, 0), thickness=2)
            cv2.line(frame, (360, 150), (360, 480), (0, 255, 0), thickness=2)
            spalte = 2
        elif x > 360 and x <= 480:
            cv2.line(frame, (360, 150), (360, 480), (0, 255, 0), thickness=2)
            cv2.line(frame, (480, 150), (480, 480), (0, 255, 0), thickness=2)
            spalte = 3
        elif x > 480 and x <= 600:
            cv2.line(frame, (480, 150), (480, 480), (0, 255, 0), thickness=2)
            cv2.line(frame, (600, 150), (600, 480), (0, 255, 0), thickness=2)
            spalte = 4
        elif x > 600 and x <= 720:
            cv2.line(frame, (600, 150), (600, 480), (0, 255, 0), thickness=2)
            cv2.line(frame, (718, 150), (718, 480), (0, 255, 0), thickness=2)
            spalte = 5

        # Wenn Spalte erkannt wurde und Stein plaziert:
        if spalte != 99 and gedrueckt is True:
            # Parameter einfügen
            stein_gefunden = False
            abbruch = False
            stein_gesetzt = False

            # Gefundene Spalte iterieren, um bereits vorhandene Steine zu finden
            for i in range(6):
                if steinematrix[i][spalte] != 0.0:
                    # stein_gefunden Index setzen und abbruch auf True
                    stein_gefunden = i
                    abbruch = True
                    break

            # Wenn Spalte nicht voll und Stein gefunden wurde:
            if i != 0 and stein_gefunden >= 0:
                # über gefunden Stein neuen Stein speichern
                steinematrix[stein_gefunden-1][spalte] = aktiverspieler
                stein_gesetzt = True
            # Ersten Stein setzen wenn keiner gefunden wurde
            elif stein_gefunden is False and abbruch is False:
                steinematrix[5][spalte] = aktiverspieler
                stein_gesetzt = True

            # Wenn Stein gesetzt wurde: aktiven Spieler ändern
            if stein_gesetzt is True:
                if aktiverspieler == 1.0:
                    aktiverspieler = 2.0
                else:
                    aktiverspieler = 1.0

        # Aktiven Spieler aufdrucken
        if aktiverspieler == 1.0:
            cv2.putText(frame, "Spieler: " + str(int(aktiverspieler)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        elif aktiverspieler == 2.0:
            cv2.putText(frame, "Spieler: " + str(int(aktiverspieler)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        return frame, steinematrix, aktiverspieler
