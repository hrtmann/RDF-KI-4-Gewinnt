import numpy as np

class Gewinnueberpruefung(object):

    def __init__(self):
        pass

    # Überprüfe, ob und wer gewonnen hat
    # Übergabe: Spielfeldmatrix
    # Rückgabe: Wer gewonnen hat
    def ueberpruefe_gewinn(self, steinematrix):
        gewonnen = 0
        letzterstein = 0


        # Überprüfe Gewinn in Zeilen
        for zeile in range(6):
            anzahlsteine = 0
            letzterstein = 0
            for spalte in range(6):
                # Alle Spalte und Zeilen durchgehen und prüfen, ob Stein schon gespielt wurde
                if steinematrix[zeile][spalte] == letzterstein and letzterstein != 0:
                    # Geprüfte Steine hochsetzen
                    anzahlsteine = anzahlsteine + 1
                    # Wenn 4 Steine gezählt wurden, hat ein Spieler gewonnen und danach break von Gewinnüberprüfung
                    if anzahlsteine == 4:
                        gewonnen = 1

                        break
                elif steinematrix[zeile][spalte] == 0:
                    letzterstein = steinematrix[zeile][spalte]
                    anzahlsteine = 0
                else:
                    # Geprüfte Steine auf 1 setzen
                    anzahlsteine = 1
                    letzterstein = steinematrix[zeile][spalte]
            if gewonnen == 1:
                break

        if gewonnen == 1:
            return letzterstein

        # Überprüfe Gewinn in Spalten
        for spalte in range(6):
            anzahlsteine = 0
            letzterstein = 0
            for zeile in range(6):
                # Alle Spalte und Zeilen durchgehen und prüfen, ob Stein schon gespielt wurde
                if steinematrix[zeile][spalte] == letzterstein and letzterstein != 0:
                    # Geprüfte Steine hochsetzen
                    anzahlsteine = anzahlsteine + 1
                    # Wenn 4 Steine gezählt wurden, hat ein Spieler gewonnen und danach break von Gewinnüberprüfung
                    if anzahlsteine == 4:
                        gewonnen = 1
                        break
                elif steinematrix[zeile][spalte] == 0:
                    letzterstein = steinematrix[zeile][spalte]
                    anzahlsteine = 0
                else:
                    # Geprüfte Steine auf 1 setzen
                    anzahlsteine = 1
                    letzterstein = steinematrix[zeile][spalte]
            if gewonnen == 1:
                break

        if gewonnen == 1:
            return letzterstein

        # Start um Diagonale zu prüfen
        # richtungdiagonale: 1 = rechtsunten, 2 = linksunten, 3 = rechtsoben, 4 = linksoben

        for zeile in range(6):
            richtungdiagonale = 0
            anzahlrichtigesteine = 0
            aktuellerspielstein = 0
            for spalte in range(6):
                anzahlrichtigesteine = 0
                letztergetestersteinzeile = 0
                letztergetestersteinspalte = 0
                aktuellerspielstein = steinematrix[zeile][spalte]
                richtung = self.richtung(zeile, spalte)
                # Testen, ob zu prüfender Spielstein schon gespielt wurde
                if aktuellerspielstein != 0:
                    letztergetestersteinzeile = zeile
                    letztergetestersteinspalte = spalte
                    # For-Schleife über zu testenden Spielsteins vom ersten Spielstein aus gehend
                    for versuch in range(4):
                        # Testen, ob Spielstein gleich vorherigen Spielstein ist
                        if aktuellerspielstein == steinematrix[letztergetestersteinzeile][letztergetestersteinspalte]:
                            anzahlrichtigesteine = anzahlrichtigesteine + 1
                            # Wenn 4 gleiche Steine gefunden wurden, hat ein Spieler gewonnen
                            if anzahlrichtigesteine == 4:
                                gewonnen = 1
                                break
                        else:
                            break
                        # Nächsten zu testenden Spielstein durch Funktion holen
                        letztergetestersteinzeile, letztergetestersteinspalte = \
                            self.naechster_spielstein(letztergetestersteinzeile, letztergetestersteinspalte, richtung)
                        if letztergetestersteinzeile == -1 or letztergetestersteinspalte == -1:
                            break
                    if gewonnen == 1:
                        break
            if gewonnen == 1:
                break
        if gewonnen == 1:
            return aktuellerspielstein
        else:
            return 99

    # Feststellen der Richtung abhängig vom Spielstein
    # Übergabe: Zeile, Spalte von Stein
    # Rückgabe: Richtung in die getestet werden soll
    # 1 = rechts unten; 2 = links unten; 3 = rechts oben; 4 = links oben
    def richtung(self, zeile, spalte):
        if zeile < 3 and spalte < 3:
            return 1
        elif zeile < 3 and spalte > 2:
            return 2
        elif zeile > 2 and spalte < 3:
            return 3
        elif zeile > 2 and spalte > 2:
            return 4

    # Rückgabe des nächsten Spielsteins abhängig von der Richtung der erforderlichen Prüfung
    # Übergabe: Zeile, Spalte von Stein und Richtung, in die getestet werden soll
    # Rückgabe: Nächster zu testender Spielstein
    def naechster_spielstein(self, zeile, spalte, richtung):
        if richtung == 1:
            zeile = zeile + 1
            spalte = spalte + 1
        elif richtung == 2:
            zeile = zeile + 1
            spalte = spalte - 1
        elif richtung == 3:
            zeile = zeile - 1
            spalte = spalte + 1
        elif richtung == 4:
            zeile = zeile - 1
            spalte = spalte - 1
        # Überprüfen, ob Spalte oder Zeile < 0 oder > 5 ist, dann außerhalb des Spielfelds
        if zeile < 0 or zeile > 5:
            zeile = -1
        if spalte < 0 or spalte > 5:
            spalte = -1
        return zeile, spalte