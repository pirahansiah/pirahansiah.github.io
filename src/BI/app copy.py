import os
import pandas as pd
from PIL import Image
from datetime import datetime
import plotly.express as px
from dash import dcc, html
from jupyter_dash import JupyterDash
import numpy as np
import logging
from image_score import *
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def get_folder_path_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            folder_path = file.readline().strip()
            logging.info(f'Reading folder path from {file_path}: {folder_path}')
            return folder_path
    except Exception as e:
        logging.error(f"Failed to read the folder path from {file_path}: {e}")
        raise
def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            img_cv = np.array(img)
            img_cv = img_cv[:, :, ::-1].copy()
            thumbnail = img.resize((100, 100))
            return {
                "filename": os.path.basename(image_path),
                "size": img.size,
                "mode": img.mode,
                "format": img.format,
                "created_at": datetime.fromtimestamp(os.path.getctime(image_path)),
                "file_size": os.path.getsize(image_path),
                "resolution": img.size[0] * img.size[1],
                "thumbnail": thumbnail,
                "calculate_mscn_coefficients": calculate_mscn_coefficients(img_cv),
                "compute_niqe_features": compute_niqe_features(img_cv),
                "calculate_piqe_index": calculate_piqe_index(img_cv),
                "estimate_jpeg_quality": estimate_jpeg_quality(img_cv),
                "compute_bliinds_features": compute_bliinds_features(img_cv),
                "extract_cornia_features": extract_cornia_features(img_cv),
                "calculate_sseq": calculate_sseq(img_cv),
                "calculate_fqadi_features": calculate_fqadi_features(img_cv)
            }
    except Exception as e:
        logging.error(f"Error extracting metadata and computing scores for image {image_path}: {e}")
        return None
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
if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, 'folder_path.txt')
    # config_file_path = 'folder_path.txt'
    folder_path = get_folder_path_from_file(config_file_path)
    metadata_df = gather_metadata(folder_path)
    if metadata_df.empty:
        logging.warning("No metadata found. Check the folder path or the file types.")
    else:
        metadata_df.to_csv(os.path.join(script_dir,'metadata.csv'), index=False)
        logging.info("Metadata CSV file has been created successfully.")
        app = JupyterDash(__name__, suppress_callback_exceptions=True)
        app.layout = html.Div([
            html.H1("Image/Video Metadata Dashboard"),
            dcc.Tabs([
                dcc.Tab(label='File Count by Format', children=[
                    dcc.Graph(figure=px.bar(metadata_df, x='format', title='File Count by Format'))
                ]),
                dcc.Tab(label='File Size Distribution', children=[
                    dcc.Graph(figure=px.histogram(metadata_df, x='file_size', title='File Size Distribution'))
                ]),
                dcc.Tab(label='Resolution Distribution', children=[
                    dcc.Graph(figure=px.histogram(metadata_df[metadata_df['resolution'].notna()], x='resolution', title='Resolution Distribution'))
                ]),
                dcc.Tab(label='Creation Date Timeline', children=[
                    dcc.Graph(figure=px.line(metadata_df.sort_values(by='created_at'), x='created_at', y='file_size', title='File Size Over Time'))
                ]),
                dcc.Tab(label='Image Quality Details', children=[
                    html.Div([
                        html.Div([
                            html.Img(src=img['thumbnail'], style={'height': '50px', 'width': '50px'}),
                            html.P(f"MSCN Coefficients: {img['calculate_mscn_coefficients']}"),
                            html.P(f"NIQE Features: {img['compute_niqe_features']}"),
                            html.P(f"PIQE Index: {img['calculate_piqe_index']}"),
                            html.P(f"JPEG Quality: {img['estimate_jpeg_quality']}"),
                            html.P(f"BLIINDS Features: {img['compute_bliinds_features']}"),
                            html.P(f"CORNIA Features: {img['extract_cornia_features']}"),
                            html.P(f"SSEQ: {img['calculate_sseq']}"),
                            html.P(f"FQADI Features: {img['calculate_fqadi_features']}")
                        ], className="image-details") for img in metadata_df.to_dict('records')
                    ], className="image-gallery")
                ])
            ])
        ])
        app.run_server(debug=True)
