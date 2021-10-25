import cv2
import mediapipe as mp
import numpy as np
import time
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle



#video
cap = cv2.VideoCapture(0)
stage=None
stages=None
stagess=None
lapes=0
laps=0
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.75, min_tracking_confidence=0.75) as pose:
    x=int(input("enter 1 to start"))
    if x==1:
        time.sleep(5)
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

            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                foot = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

            # Calculate angle
                angle_of_knee = calculate_angle(hip, knee, ankle)
                angle_of_ankle = calculate_angle(knee, ankle, foot)
                angle_of_hip = calculate_angle(shoulder, hip, knee)
            # Visualize angle
                cv2.putText(image, str(angle_of_knee),
                            tuple(np.multiply(knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle_of_ankle),                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                foot = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

            # Calculate angle
                angle_of_knee = calculate_angle(hip, knee, ankle)
                angle_of_ankle = calculate_angle(knee, ankle, foot)
                angle_of_hip = calculate_angle(shoulder, hip, knee)
            # Visualize angle
                cv2.putText(image, str(angle_of_knee),
                            tuple(np.multiply(knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle_of_ankle),
                            tuple(np.multiply(ankle, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle_of_hip),
                            tuple(np.multiply(hip, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                            )

                #timer
                cv2.putText(image, f'Timer: {int(laps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 5)

                            tuple(np.multiply(ankle, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle_of_hip),
                            tuple(np.multiply(hip, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                            )

                #timer
                cv2.putText(image, f'Timer: {int(laps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 5)

                #correction check
                if angle_of_knee >= 160:
                    stage="pass"
                    if angle_of_ankle <= 100:
                        stages="pass"
                        if angle_of_hip<=110:
                            stagess="pass"
                            start=time.time()
                        else:
                            stagess="fail"
                    else:
                        stages="fail"
                else:
                    stage="fail"
                if stages=="fail"or stagess=="fail" or stage=="fail":
                    end=time.time()
                    laps=end-start
                    print(laps)

            except:
                pass

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

