'''

docker run -p 8050:8050 \
           -v /Users/farshid/code/pirahansiah.github.io/src/docker/BI/folder_path.txt:/config/folder_path.txt \
           -v /Users/farshid/code/Work/images:/usr/src/app/images \
           farshid_pirahansiah_bi
'''

import os
import pandas as pd
from PIL import Image
from datetime import datetime
import plotly.express as px
from dash import dcc, html
from jupyter_dash import JupyterDash
import numpy as np
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to read folder path from a file
def get_folder_path_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            folder_path = file.readline().strip()  # Read the first line and strip any extra whitespace/newline
            logging.info(f'Reading folder path from {file_path}: {folder_path}')
            return folder_path
    except Exception as e:
        logging.error(f"Failed to read the folder path from {file_path}: {e}")
        raise

# Function to extract metadata from images
def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            return {
                "filename": os.path.basename(image_path),
                "size": img.size,
                "mode": img.mode,
                "format": img.format,
                "created_at": datetime.fromtimestamp(os.path.getctime(image_path)),
                "file_size": os.path.getsize(image_path),
                "resolution": img.size[0] * img.size[1]
            }
    except Exception as e:
        logging.error(f"Error extracting metadata from image {image_path}: {e}")
        return None

# Function to extract metadata from videos (placeholder function)
def get_video_metadata(video_path):
    try:
        return {
            "filename": os.path.basename(video_path),
            "created_at": datetime.fromtimestamp(os.path.getctime(video_path)),
            "file_size": os.path.getsize(video_path)
        }
    except Exception as e:
        logging.error(f"Error extracting metadata from video {video_path}: {e}")
        return None

# Function to gather metadata from a folder
def gather_metadata(folder_path):
    metadata = []
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                    meta = get_image_metadata(file_path)
                elif file.lower().endswith(('mp4', 'avi', 'mov', 'mkv')):
                    meta = get_video_metadata(file_path)
                if meta:
                    metadata.append(meta)
        return pd.DataFrame(metadata)
    except Exception as e:
        logging.error(f"Failed to gather metadata from {folder_path}: {e}")
        return pd.DataFrame()

# Main section of the script
if __name__ == '__main__':
          
    #config_file_path = '/config/folder_path.txt'        
    folder_path = get_folder_path_from_file(config_file_path)
    metadata_df = gather_metadata(folder_path)

    if metadata_df.empty:
        logging.warning("No metadata found. Check the folder path or the file types.")
    else:
        metadata_df.to_csv('metadata.csv', index=False)
        logging.info("Metadata CSV file has been created successfully.")

        # Initialize and configure the Dash app
        app = JupyterDash(__name__, suppress_callback_exceptions=True)

        # Define the layout of the dashboard
        app.layout = html.Div([
            html.H1("Image/Video Metadata Dashboard"),
            dcc.Tabs([
                dcc.Tab(label='File Count by Format', children=[dcc.Graph(figure=px.bar(metadata_df, x='format', title='File Count by Format'))]),
                dcc.Tab(label='File Size Distribution', children=[dcc.Graph(figure=px.histogram(metadata_df, x='file_size', title='File Size Distribution'))]),
                dcc.Tab(label='Resolution Distribution', children=[dcc.Graph(figure=px.histogram(metadata_df[metadata_df['resolution'].notna()], x='resolution', title='Resolution Distribution'))]),
                dcc.Tab(label='Creation Date Timeline', children=[dcc.Graph(figure=px.line(metadata_df.sort_values(by='created_at'), x='created_at', y='file_size', title='File Size Over Time'))])
            ])
        ])

        # Run the app
        #app.run_server(debug=True)
        app.run_server(debug=True, host='0.0.0.0', port=8050)

'''
# TODO 1:
No-Reference Metrics (NR)
No-reference metrics assess the quality of an image without any reference to the original.

Blind/Referenceless Image Spatial Quality Evaluator (BRISQUE): Uses natural scene statistics to assess distortions.
Natural Image Quality Evaluator (NIQE): A no-reference image quality score based on a statistical model of image naturalness.


Entropy-based Image Quality Assessment (EIQA): EIQA is a no-reference method that measures the amount of information in an image. The idea is that a high-quality image should have a high degree of entropy, or information content. Here's some sample Python code using OpenCV to compute the entropy of an image:

import cv2
import numpy as np

def entropy(img):
    hist, bins = np.histogram(img.flatten(), 256, [0,256])
    prob = hist / np.sum(hist)
    entropy = -np.sum(prob * np.log2(prob)) )
    return entropy

img = cv2.imread('image.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
score = entropy(gray_img)
print('Entropy score:', score)
Blind Image Quality Index (BIQI): BIQI is a no-reference method that uses a combination of image features, such as contrast, sharpness, and colorfulness, to predict perceived image quality. Here's some sample Python code using OpenCV to compute the BIQI of an image:

import cv2
import numpy as np

def biqi(img):
    mean_subtracted_img = img - np.mean(img)
    covariance_matrix = np.cov(mean_subtracted_img.T)
    eigenvalues, _ = np.linalg.eig(covariance_matrix)
    contrast = np.sqrt(np.mean(eigenvalues))
    sharpness = np.mean(cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F))**2)
    colorfulness = np.std(img.mean(axis=0)) + np.std(img.mean(axis=1))
    score = (contrast + sharpness + colorfulness) / 3
    return score

img = cv2.imread('image.jpg')
score = biqi(img)
print('BIQI score:', score)
No-Reference Image Quality Assessment using Convolutional Neural Networks (NR-IQA): NR-IQA is a no-reference method that uses deep learning to predict perceived image quality. The idea is to train a convolutional neural network (CNN) on a large dataset of images with human-rated quality scores, and then use the trained CNN to predict the quality of new images. Here's some sample Python code using Keras and TensorFlow to train and use an NR-IQA model:

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load and preprocess the training data
train_images = ...
train_labels = ...
train_images = np.array(train_images) / 255.0
train_images = np.expand_dims(train_images, axis=3)

# Define the NR-IQA model architecture
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(224,224,1)))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64, (3,3), activation='relu')
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(128, (3,3), activation='relu')
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(128, (3,3), activation='relu')
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(1024, activation='relu')
model.add(Dense(1, activation='linear')

# Compile and train the NR-IQA model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(train_images, train_labels, epochs=10, batch_size=32)

# Use the NR-IQA model to predict the quality of a new image
img = cv2.imread('image.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(gray_img, (224,224))
normalized_img = np.array(resized_img) / 255.0
expanded_img = np.expand_dims(normalized_img, axis=0)
expanded_img = np.expand_dims(expanded_img, axis=3)
score = model.predict(expanded_img)[0][0]
print('NR-IQA score:', score)

'''

