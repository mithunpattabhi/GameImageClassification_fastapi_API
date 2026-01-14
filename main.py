from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.responses import JSONResponse
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import io
import json

app = FastAPI(title="VideoGame Image Classification API")
model = tf.keras.models.load_model("model/game_effnetb0.h5")
classes = json.load(open("model/class_names.json"))
SIZE = 224

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    image = image.resize((SIZE, SIZE))
    x = np.array(image)
    x = preprocess_input = tf.keras.applications.efficientnet.preprocess_input(x)

    predictions = model.predict(np.expand_dims(x,0))[0]
    predicted_index = np.argmax(predictions)
    predicted_class = classes[predicted_index]
    confidence = float(predictions[predicted_index])

    response = {
        "predicted_Game": predicted_class,
        "confidence": confidence
    }
    return JSONResponse(content=response)
