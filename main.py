import cv2                                               #Importing openCV library for computer vision and image processing
import mediapipe as mp                                   #This library is used to detect the hands
cap = cv2.VideoCapture(0)                                #This will return video from the first webcam on your computer
hand_detector = mp.solutions.hands.Hands()               #
drawing_utils = mp.solutions.drawing_utils               #Used to display hand landmarks
while True:                                              #To capture frames from video and display video feed
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)                           #Used to flip the video
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
    cv2.imshow('Hand landmarks detection ', frame)
    cv2.waitKey(1)