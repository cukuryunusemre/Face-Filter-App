📷 Face Filter App
This project includes two computer vision applications:

Image Filter App (image_filter_app.py)

Applies blur or black stripe to detected faces in static images.

Uses Haar Cascades for frontal and profile face detection.

GUI is built with Tkinter.

Live Webcam Face Filter (live_face_filter.py)

Applies real-time filters on detected faces using MediaPipe.

Filter types: emoji overlay, blur, and black strip.

Includes an on-screen filter selector menu (clickable).

Emoji overlay uses transparent .png files.

Camera view is interactive with real-time selection.

✅ Requirements
bash
Kopyala
Düzenle
pip install opencv-python mediapipe numpy matplotlib
Optional for system-wide virtual camera output:

bash
Kopyala
Düzenle
pip install pyvirtualcam
⚠️ pyvirtualcam requires OBS Studio with the Virtual Camera plugin installed and running.

📁 Files
File	Description
image_filter_app.py	Filter on static images (blur & strip)
live_face_filter.py	Real-time webcam filtering
emoji_sunglasses.png	Emoji used for face overlay
emoji_cat.png	Optional emoji
emoji_smile.png	Optional emoji

🚀 Usage
1. Run the image filter:
bash
Kopyala
Düzenle
python image_filter_app.py
2. Run the webcam filter:
bash
Kopyala
Düzenle
python live_face_filter.py
Use your mouse to click on the filter options in the bottom-left menu.

Press Q to quit.

🧠 Features to Add
Emoji picker via UI

Face mesh-based effects (e.g. eye targeting)

CustomTkinter GUI

Export to .exe format

