import cv2
import mediapipe as mp
import numpy as np

# === EMOJI ===
emoji = cv2.imread("emoji.png", cv2.IMREAD_UNCHANGED)

# === MediaPipe setup ===
mp_face = mp.solutions.face_detection
detector = mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.6)

# === Global filtre seçimi ===
current_filter = "none"
clicked_filter = None

# === Filtre kutusu bilgileri ===
filter_buttons = {
    "emoji": (460, 380, 180, 40),
    "blur": (460, 430, 180, 40),
    "strip": (460, 480, 180, 40)
}

def draw_menu(frame, current_filter):
    for name, (x, y, w, h) in filter_buttons.items():
        color = (0, 255, 0) if current_filter == name else (200, 200, 200)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, -1)
        cv2.putText(frame, name.upper(), (x + 10, y + 28),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

# === Filtreler ===
def apply_emoji(frame, bbox):
    x, y, w, h = bbox
    emoji_resized = cv2.resize(emoji, (w, h))
    for c in range(3):
        alpha = emoji_resized[:, :, 3] / 255.0
        frame[y:y+h, x:x+w, c] = (1 - alpha) * frame[y:y+h, x:x+w, c] + alpha * emoji_resized[:, :, c]

def apply_blur(frame, bbox):
    x, y, w, h = bbox
    roi = frame[y:y+h, x:x+w]
    blur = cv2.GaussianBlur(roi, (31, 31), 30)
    frame[y:y+h, x:x+w] = blur

def apply_strip(frame, bbox):
    x, y, w, h = bbox
    eye_y = y + int(h * 0.25)  # Daha yukarı al
    eye_h = int(h * 0.2)
    frame[eye_y:eye_y + eye_h, x:x+w] = [0, 0, 0]

# === Mouse Tıklama Olayı ===
def mouse_event(event, mx, my, flags, param):
    global current_filter
    if event == cv2.EVENT_LBUTTONDOWN:
        for name, (x, y, w, h) in filter_buttons.items():
            if x <= mx <= x + w and y <= my <= y + h:
                current_filter = name
                print(f"Filter selected: {name}")

# === Kamera Aç ===
cap = cv2.VideoCapture(0)
cv2.namedWindow("MediaPipe Face Filter")
cv2.setMouseCallback("MediaPipe Face Filter", mouse_event)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detector.process(rgb)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x = int(bboxC.xmin * iw)
            y = int(bboxC.ymin * ih)
            w = int(bboxC.width * iw)
            h = int(bboxC.height * ih)
            x, y = max(0, x), max(0, y)
            w, h = min(w, iw - x), min(h, ih - y)
            bbox = (x, y, w, h)

            if current_filter == "blur":
                apply_blur(frame, bbox)
            elif current_filter == "strip":
                apply_strip(frame, bbox)
            elif current_filter == "emoji":
                apply_emoji(frame, bbox)

    # Menü çizin
    draw_menu(frame, current_filter)

    # Bilgi metni
    cv2.putText(frame, f"Filter: {current_filter}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("MediaPipe Face Filter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
