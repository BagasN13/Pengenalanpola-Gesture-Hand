import cv2
import mediapipe as mp
import subprocess
import pyautogui
import time

# Inisiasi MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()  # Resolusi layar

# Fungsi cek jari terbuka
def finger_open(hand_landmarks):
    finger = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        finger.append(1)
    else:
        finger.append(0)

    # 4 jari lain (index, middle, ring, pinky)
    tip_ids = [8, 12, 16, 20]
    for tip in tip_ids:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger.append(1)
        else:
            finger.append(0)
    return finger

# Rule-based gesture classification
def classify_gesture(fingers):
    if fingers == [0,1,0,0,0]:
        return "POINT"
    elif fingers == [1,1,1,1,1]:
        return "OPEN PALM"
    elif fingers == [0,0,0,0,0]:
        return "FIST"
    elif fingers == [1,0,0,0,0]:
        return "THUMB UP"
    else:
        return "UNKNOWN"

# Main Program
cap = cv2.VideoCapture(0)
last_gesture = ""
cooldown = 1
last_time = 0
chrome_opened = False
click_cooldown = 1
last_click_time = 0

# Path Chrome + opsi guest + TikTok
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
tiktok_url = "https://www.tiktok.com"
chrome_args = [chrome_path, "--guest", tiktok_url]

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while True:
        success, img = cap.read()
        if not success:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        gesture = "NONE"

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
                fingers = finger_open(handLms)
                gesture = classify_gesture(fingers)

                # ===== MOUSE CONTROL =====
                if gesture == "POINT":  # gerakkan pointer
                    x = handLms.landmark[8].x * screen_w
                    y = handLms.landmark[8].y * screen_h
                    pyautogui.moveTo(x, y, duration=0.01)

                # ===== CLICK ACTION =====
                current_time = time.time()
                if gesture == "THUMB UP" and current_time - last_click_time > click_cooldown:
                    pyautogui.click()
                    last_click_time = current_time

        # Tampilkan gesture
        cv2.putText(img, gesture, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        # ===== OPEN CHROME + TIKTOK =====
        current_time = time.time()
        if gesture != last_gesture and current_time - last_time > cooldown:
            if gesture == "FIST" and not chrome_opened:
                subprocess.Popen(chrome_args)
                chrome_opened = True

            last_gesture = gesture
            last_time = current_time

        # ===== SCROLL DENGAN POINT GESTURE =====
        if chrome_opened and gesture == "POINT":
            pyautogui.scroll(-50)  # scroll ke bawah setiap frame

        cv2.imshow("Hand Gesture Mouse Control TikTok", img)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

cap.release()
cv2.destroyAllWindows()
