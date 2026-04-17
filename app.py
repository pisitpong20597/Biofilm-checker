# Biofilm-checkerapp.pyapp.pyimport streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("📸 pH Detector")

def estimate_ph(r, g, b):
    color = np.uint8([[[int(r), int(g), int(b)]]])
    hsv = cv2.cvtColor(color, cv2.COLOR_RGB2HSV)
    hue = hsv[0][0][0]

    if hue < 10:
        return 2
    elif hue < 25:
        return 4
    elif hue < 35:
        return 6
    elif hue < 85:
        return 7
    elif hue < 130:
        return 10
    else:
        return 13

image_file = st.camera_input("📷 Take a picture")

if image_file:
    image = Image.open(image_file).convert("RGB")
    img = np.array(image)

    st.image(image)

    h, w, _ = img.shape
    center = img[h//2-20:h//2+20, w//2-20:w//2+20]

    avg_color = center.mean(axis=(0,1))
    r, g, b = avg_color

    ph = estimate_ph(r, g, b)

    st.write(f"RGB: {int(r)}, {int(g)}, {int(b)}")
    st.write(f"🧪 pH: {ph}")
