import cv2                                               
import mediapipe as mp                                   
cap = cv2.VideoCapture(0)                               
hand_detector = mp.solutions.hands.Hands()               
drawing_utils = mp.solutions.drawing_utils               
while True:                                              
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)                           
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
    cv2.imshow('Hand landmarks detection ', frame)
    cv2.waitKey(1)
