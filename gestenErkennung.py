# OpenCV und Mediapipe einbinden
import cv2
import mediapipe as mp

class gesten:

    def __init__(self):
        # MediaPipe einrichten
        self.mpHands = mp.solutions.hands
        # Hand Einstellungen
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils
        # Gedrueckt Status Abfrage
        self.gedrueckt_status = False

    def erkenne_geste(self, frame):
            # Parameter setzen
            gedrueckt = False
            position_x = 0
            distance = 0
            x, y, c = frame.shape

            # Frame drehen
            frame = cv2.flip(frame, 1)
            # Frame Farbschema ändern
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Hand Landmarks erkennen
            result = self.hands.process(framergb)

            # Landmarks verarbeiten
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)

                        landmarks.append([lmx, lmy])

                    # Erkannte Hand zeichnen
                    self.mpDraw.draw_landmarks(frame, handslms, self.mpHands.HAND_CONNECTIONS)

                    # x-Distanz von Landmarks 12 und 8 bestimmen
                    distance = landmarks[12][0] - landmarks[8][0]
                    # x-Mittelwert von Landmark 12 und 8 bestimmen
                    position_x = landmarks[12][0] + landmarks[8][0] / 2
                    # Distanz als "unsigned" casten -> Werte könnten Hand abhänig negativ werden
                    unsigned_distance = abs(distance)

                    # Erkenne ob Finger zusammen sind und Zustandsvariable False ist -> setze zustandsvariable auf True
                    if unsigned_distance > 5 and unsigned_distance < 20 and self.gedrueckt_status is False:
                        self.gedrueckt_status = True

                    # Erkenne ob Finger geöffnet wurden und ob Zustandvariable auf True steht -> gedrueckt = True
                    if unsigned_distance > 40 and self.gedrueckt_status is True:
                        gedrueckt = True
                        self.gedrueckt_status = False

            # Status ob Zustandänderung eingetreten ist und Mittlere X-Position zurückgeben
            return frame, gedrueckt, position_x