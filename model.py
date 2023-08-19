import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.optimizers import Adam

classes = ["class1", "class2", "class3"]  # Update with actual class labels

def build_model(num_classes):
    # Build the model architecture
    
    model = ResNet50(input_shape=(224, 224, 3), classes=num_classes)
    return model

def load_trained_model():
    model = build_model(len(classes))
    model.load_weights("trained_model.h5")
    model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model
