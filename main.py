from fastapi import FastAPI
from .predictor import predict_image

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    prediction = predict_image(file)
    return prediction
