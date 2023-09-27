from flask import Flask, request, render_template, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('Tomato_Leaf_Disease_Detection_model.h5')
class_label = ['Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight',
               'Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot','Tomato___Spider_mites Two-spotted_spider_mite',
               'Tomato___Target_Spot','Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Tomato_mosaic_virus',
               'Tomato___healthy']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Get the uploaded image file
        image = request.files['image']
        if not image:
            return jsonify(error="No file provided"), 400

        # Read and preprocess the image
        image = Image.open(image)
        image = image.resize((28, 28))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        # Make predictions using the loaded model
        predictions = model.predict(image)

        # Get the top predicted class and its confidence score
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_label[predicted_class_index]  # You can replace this with your class labels if available

        return jsonify(Class=predicted_class_label, Confidence=float(predictions[0][predicted_class_index])*100)

    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
