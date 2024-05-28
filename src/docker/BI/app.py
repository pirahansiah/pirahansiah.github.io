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
    config_file_path = 'folder_path.txt'
    
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
        app.run_server(debug=True)
