# 📷 Face Filter App

This project includes two computer vision applications:

### 1. Image Filter App (`image_filter_app.py`)
- Applies blur or black stripe to detected faces in **static images**.
- Uses Haar Cascades for frontal and profile face detection.
- GUI is built with `Tkinter`.

### 2. Live Webcam Face Filter (`live_face_filter.py`)
- Applies real-time filters on detected faces using **MediaPipe**.
- Filter types: `emoji overlay`, `blur`, and `black strip`.
- On-screen filter selector (clickable boxes).
- Emoji overlay supports transparent `.png` files.
- Optional: Output to system-wide virtual camera (OBS required).

---

## ✅ Requirements

```bash
pip install opencv-python mediapipe numpy matplotlib
