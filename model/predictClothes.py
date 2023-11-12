from imp import load_module
import tensorflow as tf
from PIL import Image
import numpy as np
import keras

img_path = ""
labels = ['T-shirt/Top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle Boot']
img= Image.open(img_path).convert('L')
np_img = np.array(img)
#print(np_img.shape)

np_img = np.resize(np_img, (28, 28))
print(np_img.shape)

img_reshaped = np_img[np.newaxis, :, :, np.newaxis]
#print(img_reshaped.shape)

model = tf.keras.models.load_model("ecoThreads_classification_model.keras")

predictions = model.predict(img_reshaped)
#print(predictions)
predicted_label = predictions.argmax(axis=-1)
print("The image is of a " + labels[int(predicted_label)])


