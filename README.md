# 🎮 Game Image Classification – FastAPI Backend

## Overview
This repository contains the **FastAPI-based backend inference service** for a deep learning project that classifies video game screenshots.

The backend serves a trained **EfficientNetB0** model and exposes a REST API endpoint that accepts an image and returns the predicted game along with confidence.  
The frontend (Streamlit UI) for this project is maintained as a **separate repository**, following proper backend–frontend separation used in real-world systems.

---

## Key Features
- REST API built using **FastAPI**
- Deep learning inference using **EfficientNetB0 (Transfer Learning)**
- Accepts image uploads via API
- Returns predicted class with confidence score
- Clean, modular backend design
- Easily reusable with any frontend (Web / Mobile / UI frameworks)

---

## Supported Classes
The model currently supports classification for the following video games:
- GTA 5
- Indiana Jones
- Spider-Man
- Tomb Raider

---

## Tech Stack
- **Backend Framework:** FastAPI  
- **Model:** TensorFlow / Keras (EfficientNetB0)  
- **Inference Server:** Uvicorn  
- **Image Processing:** Pillow, NumPy  

---

## API Endpoint

### `POST /predict`

**Description:**  
Accepts an image file and returns the predicted game label with confidence.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Parameter: `file` (image file)

**Response (JSON):**
```json
{
  "predicted_Game": "game_name",
  "confidence": score
}
```

##How to Run Locally:
**1) Clone the Repository**
```1) Clone the Repository
   git clone https://github.com/your-username/GameImageClassification_fastapi_API.git
   cd GameImageClassification_fastapi_API
```
**2) Install Dependencies**
```2) Install Dependencies
   pip install -r requirements.txt
```
**3) Start the FastAPI Server**
```3) Start the FastAPI Server
   uvicorn app:app --reload
```
**4) Test the API**
```4) Test the API
   http://127.0.0.1:8000/docs
```
