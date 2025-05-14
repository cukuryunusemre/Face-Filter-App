# 📷 Face Filter App

This project includes two computer vision applications:

### 1. Image Filter App (`facefilter.py`)
- Applies blur or black stripe to detected faces in **static images**.
- Uses Haar Cascades for frontal and profile face detection.
- GUI is built with `Tkinter`.

### 2. Live Webcam Face Filter (`webcam.py`)
- Applies real-time filters on detected faces using **MediaPipe**.
- Filter types: `emoji overlay`, `blur`, and `black strip`.
- On-screen filter selector (clickable boxes).
- Emoji overlay supports transparent `.png` files.
- Optional: Output to system-wide virtual camera (OBS required).

---

## ✅ Requirements

```bash
pip install opencv-python mediapipe numpy matplotlib
```
Optional for virtual camera output:
```bash
pip install pyvirtualcam
```
⚠️ You must install OBS Studio and start the virtual camera from Tools > Start Virtual Camera.

| File                   | Description                            |
| ---------------------- | -------------------------------------- |
| `faveflter.py`         | Filter on static images (blur & strip) |
| `webcam.py`            | Real-time webcam filtering             |
| `emoji_sunglasses.png` | Emoji used for face overlay            |
| `emoji_cat.png`        | Optional emoji                         |
| `emoji_smile.png`      | Optional emoji                         |


