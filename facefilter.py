import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import matplotlib.pyplot as plt

# === MODELS ===
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

# === Image Process ===
def process_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("Error", f"cannot read:\n{file_path}")
        return None, None, None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    # Find faces
    faces_frontal = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    faces_profile = profile_cascade.detectMultiScale(gray, scaleFactor=1.25, minNeighbors=4)
    faces = list(faces_frontal) + list(faces_profile)

    original = image_rgb.copy()
    blurred = image_rgb.copy()
    striped = image_rgb.copy()

    if not faces:
        messagebox.showwarning("Warning", "App cannot find any faces.")
        return original, blurred, striped

    for (x, y, w, h) in faces:
        # Dinamik blur boyutu
        kernel_size = max(15, (w // 5) | 1)
        roi = blurred[y:y+h, x:x+w]
        blurred[y:y+h, x:x+w] = cv2.GaussianBlur(roi, (kernel_size, kernel_size), 30)

        # Şerit
        eye_y = y + int(h * 0.35)
        eye_h = int(h * 0.2)
        striped[eye_y:eye_y + eye_h, x:x+w] = [0, 0, 0]

    return original, blurred, striped

# === Select image ===
def show_images():
    file_path = filedialog.askopenfilename(
        title="Select image",
        filetypes=[("Images", "*.jpg *.jpeg *.png")],
        initialdir="/"  # Her yerden dosya seçilebilsin
    )
    if not file_path:
        return

    original, blurred, striped = process_image(file_path)
    if original is None:
        return

    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    for ax, (title, img) in zip(axs, [("Original", original), ("Blur", blurred), ("Strip", striped)]):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()

# === UI ===
root = tk.Tk()
root.title("Face Filter App")
root.geometry("300x150")
root.resizable(False, False)

tk.Button(root, text="📂 Select image", font=("Arial", 14), width=20, command=show_images).pack(pady=40)

root.mainloop()
