import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
from labels import labels

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Traffic Sign Recognition",
    page_icon="🚦",
    layout="centered"
)

# =========================
# LOAD MODEL
# =========================
model = load_model("traffic_sign_model.keras")


# =========================
# HEADER
# =========================
st.title("🚦 Traffic Sign Recognition System")
st.markdown("Upload a traffic sign image and get instant prediction using a CNN model.")

st.divider()

# =========================
# UPLOAD IMAGE
# =========================
file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# =========================
# PREPROCESS
# =========================
def preprocess(img):
    img = img.convert("RGB")
    img = img.resize((30, 30))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# =========================
# PREDICTION
# =========================
if file is not None:

    image = Image.open(file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    processed = preprocess(image)
    prediction = model.predict(processed)

    class_id = np.argmax(prediction)
    class_name = labels.get(class_id, "Unknown")
    confidence = float(np.max(prediction))

    with col2:
        st.subheader("Prediction Result 🚦")

        st.success(class_name)

        st.metric(label="Confidence Score", value=f"{confidence:.2f}")

        st.progress(confidence)

    st.divider()

    st.caption("Model trained using CNN on Traffic Sign Dataset (GTSRB)")