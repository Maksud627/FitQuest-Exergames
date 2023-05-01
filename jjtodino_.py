import mediapipe as mp
import cv2
import numpy as np
import pyautogui
import time
import keyboard
from pynput.keyboard import Key, Controller
import csv

def jumping_jack_to():
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

    # JUMPING JACKS #

    cap = cv2.VideoCapture(0)

    # Curl counter variables
    counter = 0
    squat_counter = 0
    jump_counter = 0
    stage = None
    isSquat = False

    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks (LEFT ARM!!)
            try:
                landmarksL = results.pose_landmarks.landmark

                # Get coordinates
                shoulderL = [landmarksL[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                             landmarksL[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                elbowL = [landmarksL[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                          landmarksL[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                wristL = [landmarksL[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                          landmarksL[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                eyeL = [landmarksL[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].x,
                        landmarksL[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].y]

                # Calculate angle
                angleL = calculate_angle(shoulderL, elbowL, wristL)

            except:
                pass

            # Extract landmarks (RIGHT ARM!)
            try:
                landmarksR = results.pose_landmarks.landmark

                # Get coordinates
                shoulderR = [landmarksR[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                             landmarksR[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                elbowR = [landmarksR[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarksR[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                wristR = [landmarksR[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                          landmarksR[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
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
                    if isSquat == False:
                        squat_counter += 1
                        isSquat = True
                    pyautogui.keyDown('down')


                elif angleR and angleL > 130:
                    stage = "up"
                    isSquat = False
                    pyautogui.keyUp('down')
                    pyautogui.press('space')
                    # jump_counter += 1
                    # keyboard.press_and_release('up')
                    # time.sleep(1)
                    # q.put("Jump")

                    # pyautogui.press('up')

                    # keyboard.press('up')
                    # keyboard.on_presskey("up", lambda: print("You pressed up"))
                    # print(keyboard.is_pressed('up'))
                    # if keyboard.read_key() == "up":
                    #     print("You pressed up")
                    # keyboard.release('up')
                    # print(pyautogui.press('up'))
                    # keyboard = Controller()
                    # keyboard.press(Key.up)
                    # print(keyboard.press(Key.up))
                    # keyboard.release(Key.up)

                elif angleR and angleL < 20 and stage == 'up':
                    stage = "down"
                    isSquat = False
                    counter += 1
                    # q.put("Duck")
                    print(counter)

                else:
                    isSquat = False
                    pyautogui.keyUp('down')

            except:
                pass

            # Render curl counter LEFT
            # Setup status box LEFT
            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            # Rep data
            cv2.putText(image, 'JUMP JACKS', (15, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter),
                        (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Stage data
            cv2.putText(image, ' STAGE', (145, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage,
                        (85, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )

            cv2.imshow('Mediapipe Feed', image)


            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        jump_counter = counter
        dino_calories = 0.2 * jump_counter + 0.32 * squat_counter

        # csv_file = open('dummy.csv', mode='a')
        with open('dummy.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            row_data = [dino_calories, jump_counter, squat_counter]
            csv_writer.writerow(row_data)
            csv_file.flush()
            csv_file.close()


if __name__ == '__main__':
    jumping_jack_to()

