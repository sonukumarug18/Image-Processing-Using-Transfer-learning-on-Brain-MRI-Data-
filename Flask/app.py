
import os
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the pre-trained VGG16 model
model = load_model("brain_vgg16.h5",compile=False)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


index = ["no_tumor", "meningioma_tumor", "glioma_tumor", "pituitary_tumor"]
# Define a function to preprocess the image for the VGG16 model
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img=img/255.0
    return img


@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/upload',methods =['GET','POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)

    image_file = request.files['image']

    if image_file.filename == '':
        return redirect(request.url)

    if image_file:
        image_path = os.path.join('static/upload', image_file.filename)
        image_file.save(image_path)
        img = preprocess_image(image_path)
        pred = model.predict(img)
        pred_class=np.argmax(pred,axis=1)
        pred_sport=index[pred_class[0]]
        

        return render_template('index.html', image_path=image_path, predictions=pred_sport)


if __name__ == '__main__':
    app.run(debug=True)
