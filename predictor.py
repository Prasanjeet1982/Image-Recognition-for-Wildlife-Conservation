import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from model import load_trained_model, classes

def predict_image(file):
    try:
        loaded_model = load_trained_model()
        image = load_img("uploaded_image.jpg", target_size=(224, 224))
        image = img_to_array(image) / 255.0
        image = tf.expand_dims(image, axis=0)
        
        prediction = loaded_model.predict(image)
        class_idx = tf.argmax(prediction[0]).numpy()
        class_label = classes[class_idx]
        
        return {"class_label": class_label}
    except Exception as e:
        return {"error": str(e)}
