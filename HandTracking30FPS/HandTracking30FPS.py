import mediapipe as mp
import cv2
# to check the frame-rate
import time

cap = cv2.VideoCapture(0)

# Hand Detection Module
mpHands = mp.solutions.hands
hands = mpHands.Hands() # default false
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    # Inorder to know if something is detected or not we use .multi_hand_landmarks)
    # We put in a for loop to check if we have multiple hands or not
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # For getting the landmark information
            for id, lm in enumerate(handLms.landmark):
                for id, lm in enumerate(handLms.landmark):
                    # print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id,cx,cy)

                    # Inorder to detect specific points
                    if (id == 4):
                        cv2.circle(img, (cx,cy), 25, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_ITALIC, 2, (255,0,255),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
