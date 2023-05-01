import mediapipe as mp
import cv2
import numpy as np
import pyautogui
import time
import keyboard
from pynput.keyboard import Key, Controller
import csv



def bicep_curl_to():
    # helps draw different detections from holistic models
    mp_drawing = mp.solutions.drawing_utils

    # import holistic models (this is just for point tracking with colors)
    mp_holistic = mp.solutions.holistic

    # mp pose
    mp_pose = mp.solutions.pose

    # cap = cv2.VideoCapture(0)
    # # Initiate holistic model
    # with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    #     while cap.isOpened():
    #         ret, frame = cap.read()
    #
    #         # Recolor Feed
    #         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         # Make Detections
    #         results = holistic.process(image)
    #         # print(results.face_landmarks)
    #
    #         # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
    #
    #         # Recolor image back to BGR for rendering
    #         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #
    #         # Draw face landmarks
    #         mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
    #
    #         # Right hand
    #         mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    #
    #         # Left Hand
    #         mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    #
    #         # Pose Detections
    #         mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    #
    #         cv2.imshow('Raw Webcam Feed', image)
    #
    #         if cv2.waitKey(10) & 0xFF == ord('q'):
    #             break
    #
    # cap.release()
    # cv2.destroyAllWindows()

    def calculate_angle(a, b, c):
        a = np.array(a)  # First
        b = np.array(b)  # Mid
        c = np.array(c)  # End

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle

    # bicep curl
    cap = cv2.VideoCapture(0)

    counterL = 0
    stageL = None

    counterR = 0
    stageR = None
    pinball_calories = 0

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue

            # Recolor image to RGB
            image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            # image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            # image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks (LEFT ARM!!)
            try:
                landmarksL = results.pose_landmarks.landmark

                # Get coordinates
                shoulderL = [landmarksL[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarksL[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbowL = [landmarksL[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarksL[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wristL = [landmarksL[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                          landmarksL[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                eyeL = [landmarksL[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].x,
                        landmarksL[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].y]

                # Calculate angle
                angleL = calculate_angle(shoulderL, elbowL, wristL)

                # Visualize angle
                cv2.putText(image, str(angleL),
                            tuple(np.multiply(elbowL, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                # Curl counter logic
                if eyeR[1] > 0.5 and eyeL[1] > 0.5:
                    pyautogui.keyDown('down')

                elif angleL > 120:
                    stageL = "down"
                    pyautogui.keyUp('down')
                    pyautogui.keyUp('right')

                # left bicep oup so duck else run continue
                elif angleL < 30 and stageL == 'down':
                    stageL = "up"
                    counterL += 1
                    pyautogui.keyUp('down')
                    pyautogui.keyDown('right')
                    print(counterL)

                else:
                    pyautogui.keyUp('down')

            except:
                pass

            # Extract landmarks (RIGHT ARM!)
            try:
                landmarksR = results.pose_landmarks.landmark

                # Get coordinates
                shoulderR = [landmarksR[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                             landmarksR[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbowR = [landmarksR[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                          landmarksR[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wristR = [landmarksR[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                          landmarksR[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                eyeR = [landmarksL[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].x,
                        landmarksL[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].y]

                # Calculate angle
                angleR = calculate_angle(shoulderR, elbowR, wristR)

                # Visualize angle
                cv2.putText(image, str(angleR),
                            tuple(np.multiply(elbowR, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                # Curl counter logic
                if eyeR[1] > 0.5 and eyeL[1] > 0.5:
                    pyautogui.keyDown('down')

                elif angleR > 120:
                    stageR = "down"
                    pyautogui.keyUp('down')
                    pyautogui.keyUp('left')


                # right bicep up to move right clipper
                elif angleR < 30 and stageR == 'down':
                    stageR = "up"
                    counterR += 1
                    pyautogui.keyUp('down')
                    pyautogui.keyDown('left')
                    print(counterR)

                else:
                    pyautogui.keyUp('down')

            except:
                pass

            # Render curl counter LEFT
            # Setup status box LEFT
            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            # Render curl counter RIGHT
            # Setup status box RIGHT
            cv2.rectangle(image, (240, 0), (465, 73), (245, 117, 16), -1)

            # Rep data LEFT
            cv2.putText(image, 'RIGHT REPS', (15, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counterL),
                        (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Stage data LEFT
            cv2.putText(image, 'STAGE', (135, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stageL,
                        (90, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0), 2, cv2.LINE_AA)

            # Rep data RIGHT
            cv2.putText(image, 'LEFT REPS', (255, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counterR),
                        (250, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Stage data RIGHT
            cv2.putText(image, 'STAGE', (375, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stageR,
                        (330, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        pinball_calories = 0.0125 * (counterL + counterR)

        # csv_file = open('dummy.csv', mode='a')
        with open('dummy2.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            row_data = [pinball_calories, counterL, counterR]
            csv_writer.writerow(row_data)
            csv_file.flush()
            csv_file.close()

if __name__ == "__main__":
    bicep_curl_to()