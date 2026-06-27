# 🚗 Smart Parking Detection System

## Overview

The Smart Parking Detection System is an AI-powered web application that detects parking occupancy from an uploaded parking lot image using a Convolutional Neural Network (CNN).

The system classifies the parking area into one of the following categories:

- Mostly Empty Parking
- Partially Occupied Parking
- Mostly Full Parking

The project is developed using Python, Flask, TensorFlow, HTML, CSS, and JavaScript.

---

## Features

- Upload parking lot images
- AI-based parking occupancy detection
- Attractive responsive user interface
- Real-time prediction
- Displays parking availability with suitable messages and images

---

## Technologies Used

- Python
- Flask
- TensorFlow / Keras
- NumPy
- HTML5
- CSS3
- JavaScript

---

## Project Structure

```
python/
│
├── app.py
├── smart_parking_cnn.h5
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── images/
│       ├── free.jpg
│       ├── partial.jpg
│       └── full.jpg
│
└── uploads/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/thoyajarangaiahgari-ux/smart-parking-detection.git
```

Move into the project

```bash
cd smart-parking-detection
```

Install required packages

```bash
pip install flask tensorflow numpy pillow
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Working

1. Upload a parking lot image.
2. CNN processes the image.
3. Parking occupancy is predicted.
4. Result page displays the occupancy status with a recommendation.

---

## Future Improvements

- Real-time CCTV camera integration
- Parking slot counting
- GPS-based nearby parking suggestion
- Mobile application integration
- Cloud deployment

---

## Author

**Rangaiahgari Thoyaja**

B.Tech Electronics and Communication Engineering

Sri Venkateshwara College of Engineering

GitHub:
https://github.com/thoyajarangaiahgari-ux