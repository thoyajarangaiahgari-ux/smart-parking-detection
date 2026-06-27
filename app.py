from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load your trained CNN model
model = load_model(
    r"smart_parking_cnn.h5"
)

UPLOAD_FOLDER = r"uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return render_template(
            "result.html",
            result="No Image Uploaded",
            message="Please upload an image.",
            image_name="partial.jpg"
        )

    file = request.files['image']

    if file.filename == '':
        return render_template(
            "result.html",
            result="No File Selected",
            message="Please select an image.",
            image_name="partial.jpg"
        )

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    # Preprocess image
    img = image.load_img(
        filepath,
        target_size=(128, 128)
    )

    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    score = float(prediction[0][0])

    print("Prediction Score:", score)

    # busy = 0, free = 1

    if score >= 0.80:
        result = "Parking Area Mostly Empty"
        message = "Great News! Parking spaces are available. You can safely park your vehicle."
        image_name = "free.jpg"

    elif score >= 0.40:
        result = "Parking Area Partially Occupied"
        message = "Parking availability is limited. Please proceed carefully and check nearby slots."
        image_name = "partial.jpg"

    else:
        result = "Parking Area Mostly Full"
        message = "Sorry to say, the parking area is heavily occupied. Please find a nearby parking location."
        image_name = "full.jpg"

    return render_template(
        "result.html",
        result=result,
        message=message,
        image_name=image_name
    )


if __name__ == "__main__":
    app.run(debug=True)
