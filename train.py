import tensorflow as tf
from model import build_model, classes
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_model(train_data_dir, num_epochs):
    model = build_model(len(classes))
    
    train_datagen = ImageDataGenerator(
        # Augmentation options
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )
    
    model.fit(train_generator, epochs=num_epochs)
    model.save_weights("trained_model.h5")

if __name__ == "__main__":
    train_model("path/to/train_data", num_epochs=10)
