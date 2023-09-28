# Tomato-Leaf-Disease-Detection
In this project, a convolution neural network is used to detect tomato leaf disease.
Dataset Link: https://www.kaggle.com/datasets/shylesh101/tomato-leaf-disease
In this dataset we have three(train,test,valid) folders.

Data Preparation
Step 1:
Data augmentation is done with operations like rescaling, rotation and horizontal flip.

step 2:
resize the image with dimension (28,28,3)

Model Building keypoints:
1. Batch normalization is applied to normalize the activations of the previous layer. It helps improve training stability and speed. 
2. Dropout is applied to randomly deactivate 33% of the neurons during training, which helps prevent overfitting.

Model Training:
Early stopping for preventing Overfitting

