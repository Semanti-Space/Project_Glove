import math
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_lms in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
                thumb_tip = hand_lms.landmark[4]
                thumb_base = hand_lms.landmark[2]
                index_tip = hand_lms.landmark[8]
                index_base = hand_lms.landmark[5]
                middle_tip = hand_lms.landmark[12]
                middle_base = hand_lms.landmark[9]
                ring_tip = hand_lms.landmark[16]
                ring_base = hand_lms.landmark[13]
                pinky_tip = hand_lms.landmark[20]
                pinky_base = hand_lms.landmark[17]

                fingers = { "Thumb": "EXTENDED" if abs(thumb_tip.x - thumb_base.x) > 0.1 else "TUCKED",
    "Index": "EXTENDED" if index_base.y - index_tip.y > 0.35 else "CURLED",
    "Middle": "EXTENDED" if middle_base.y - middle_tip.y > 0.35 else "CURLED",
    "Ring": "EXTENDED" if ring_base.y - ring_tip.y > 0.35 else "CURLED",
    "Pinky": "EXTENDED" if pinky_base.y - pinky_tip.y > 0.28 else "CURLED",}

                y_pos = 30
                for finger, state in fingers.items():
                 color = (0, 255, 0) if "EXTENDED" in state else (0, 0, 255)
                 cv2.putText(frame, f"{finger}: {state}", (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                 y_pos += 30
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "EXTENDED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED":
                    cv2.putText(frame, "PATAKA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED" and abs(ring_tip.y - thumb_tip.y) > 0.1:
                    cv2.putText(frame, "TRIPATAKA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(middle_tip.x - index_tip.x) < 0.19:
                    cv2.putText(frame, "ARDHAPATAKA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 0, 250), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(middle_tip.x - index_tip.x) >0.21:
                    cv2.putText(frame, "KARTARIMUKHAHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED" and abs(ring_tip.y - thumb_tip.y) < 0.1:
                    cv2.putText(frame, "MAYURA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "EXTENDED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "EXTENDED":
                    cv2.putText(frame, "ARDHACHANDRASCHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "EXTENDED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) > 0.1:
                    cv2.putText(frame, "ARALA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED":
                    cv2.putText(frame, "SUKHATUNDAKAHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "EXTENDED" and abs(ring_base.y - thumb_tip.y) > 0.1 and abs(index_tip.y - index_base.y) < 0.1:
                    cv2.putText(frame, "MUSHTHI", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) > 0.1 and abs(thumb_tip.y - middle_tip.y) < 0.1 and abs(thumb_tip.y - ring_tip.y) < 0.1 and abs(thumb_tip.y - pinky_tip.y) < 0.1:
                    cv2.putText(frame, "SHIKHARA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (210, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) < 0.1 and abs(thumb_tip.y - middle_tip.y) > 0.1 and abs(thumb_tip.y - ring_tip.y) > 0.1 and abs(thumb_tip.y - pinky_tip.y) > 0.1:
                    cv2.putText(frame, "KAPITTHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                spread = abs(thumb_tip.y - index_tip.y)
                print(f"Spread: {abs(index_tip.y - thumb_tip.y):.2f}")
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "EXTENDED" and abs(thumb_base.y - index_tip.y)> 0.20:
                    cv2.putText(frame, "KATAKAMUKHAHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED":
                    cv2.putText(frame, "SUCHI", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "EXTENDED":
                    cv2.putText(frame, "CHANDRAKALA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) < 0.1 and abs(thumb_tip.y - middle_tip.y) < 0.1 and abs(thumb_tip.y - ring_tip.y) < 0.1 and abs(thumb_tip.y - pinky_tip.y) < 0.1 and abs(thumb_base.y - thumb_tip.y) > 0.1:
                    cv2.putText(frame, "PADMAKOSHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) > 0.1 and abs(thumb_tip.y - middle_tip.y) > 0.1 and abs(thumb_tip.y - ring_tip.y) > 0.1 and abs(thumb_tip.y - pinky_tip.y) > 0.1 and abs(thumb_base.y - thumb_tip.y) > 0.1:
                    cv2.putText(frame, "SHARPASIRSHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_base.y)> 0.1 and abs(thumb_tip.y - pinky_tip.y) > 0.40:
                    cv2.putText(frame, "MRIGARSHIRSHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED":
                    cv2.putText(frame, "SIMHAMUKHAHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_base.y - ring_tip.y) < 0.1 and abs(thumb_tip.y - index_tip.y) > 0.1:
                    cv2.putText(frame, "KANGULASCHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - ring_tip.y) > 0.1 and abs(thumb_tip.y - index_tip.y) > 0.1:
                    cv2.putText(frame, "ALAPADMAKAHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "EXTENDED" and abs(thumb_tip.y - index_tip.y) > 0.1 and abs(thumb_tip.y - middle_tip.y) > 0.1 and abs(thumb_tip.y - ring_tip.y) > 0.1 and abs(thumb_tip.y - pinky_tip.y) > 0.1 and abs(thumb_base.y - thumb_tip.y) > 0.1 and abs(ring_base.y - thumb_tip.y) < 0.1 and abs(middle_tip.y - index_tip.y)< 0.1:
                    cv2.putText(frame, "CHATURA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "EXTENDED" and abs(thumb_base.y - index_tip.y)<0.20:
                    cv2.putText(frame, "BHRAMAHARA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                SPREAD2 = abs(thumb_base.y - index_tip.y)
                print(f"SPREAD2: {abs(thumb_base.y - index_tip.y):.2f}")             
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "EXTENDED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "EXTENDED" and abs(thumb_tip.y - index_tip.y) < 0.1:
                    cv2.putText(frame, "HAMSASYA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "EXTENDED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_base.y) < 0.1 and abs(thumb_tip.y - pinky_tip.y) < 0.40:
                    cv2.putText(frame, "HAMSAPAKSHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) > 0.1 and abs(thumb_tip.y - middle_tip.y) > 0.1 and abs(thumb_tip.y - ring_tip.y) > 0.1 and abs(thumb_tip.y - pinky_tip.y) > 0.1 and abs(thumb_base.y - thumb_tip.y) > 0.1:
                    cv2.putText(frame, "SAMDAMSHA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "TUCKED" and abs(thumb_tip.y - index_tip.y) < 0.1 and abs(thumb_tip.y - middle_tip.y) < 0.1 and abs(thumb_tip.y - ring_tip.y) < 0.1 and abs(thumb_tip.y - pinky_tip.y) < 0.1 and abs(thumb_base.y - thumb_tip.y) > 0.1:
                    cv2.putText(frame, "MUKULA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (110,110,0), 2)
                if fingers["Index"] == "CURLED" and fingers["Middle"] == "CURLED" and fingers["Ring"] == "CURLED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "EXTENDED" and abs(index_tip.y - index_base.y) >0.1 and abs(middle_tip.y - index_tip.y) > 0.1:
                    cv2.putText(frame, "TAMRACHURA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (110, 255, 0), 2)
                if fingers["Index"] == "EXTENDED" and fingers["Middle"] == "EXTENDED" and fingers["Ring"] == "EXTENDED" and fingers["Pinky"] == "CURLED" and fingers["Thumb"] == "EXTENDED":
                    cv2.putText(frame, "TRISHULA", (10,330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
        cv2.imshow("Semanti's Mudra Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()