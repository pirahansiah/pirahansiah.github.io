import os
import pandas as pd
from PIL import Image
from datetime import datetime
import plotly.express as px
from dash import dcc, html, Dash
import numpy as np
import logging
from image_score import *
from dash.dependencies import Input, Output

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

def gather_folder_info(folder_path):
    folder_info = {}
    try:
        for root, _, files in os.walk(folder_path):
            image_count = sum(1 for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')))
            video_count = sum(1 for file in files if file.lower().endswith(('mp4', 'avi', 'mov', 'mkv')))
            folder_info[root] = {'images': image_count, 'videos': video_count}
        return folder_info
    except Exception as e:
        logging.error(f"Failed to gather folder info from {folder_path}: {e}")
        return {}

def gather_metadata(folder_path):
    metadata = []
    try:
        for root, _, files in os.walk(folder_path):
            image_count = 0
            video_count = 0
            for file in files:
                if image_count >= 2 and video_count >= 2:
                    break
                file_path = os.path.join(root, file)
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')) and image_count < 2:
                    meta = get_image_metadata(file_path)
                    #image_count += 1
                elif file.lower().endswith(('mp4', 'avi', 'mov', 'mkv')) and video_count < 2:
                    meta = get_video_metadata(file_path)
                    #video_count += 1
                else:
                    continue
                if meta:
                    metadata.append(meta)
        return pd.DataFrame(metadata)
    except Exception as e:
        logging.error(f"Failed to gather metadata from {folder_path}: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, 'folder_path.txt')
    folder_path = get_folder_path_from_file(config_file_path)
    folder_info = gather_folder_info(folder_path)
    
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = html.Div([
        html.H1("Image/Video Metadata Dashboard"),
        html.Div([
            html.P(f"Folder Path: {folder_path}"),
            html.P(f"Total Folders: {len(next(os.walk(folder_path))[1])+1}"),
            html.P(f"Total Files: {sum(info['images'] + info['videos'] for info in folder_info.values())}")
        ]),
        html.Div([
            html.H2("Folder Info"),
            html.Table([
                html.Thead([
                    html.Tr([html.Th("Folder Path"), html.Th("Number of Images"), html.Th("Number of Videos")])
                ]),
                html.Tbody([
                    html.Tr([html.Td(key), html.Td(value['images']), html.Td(value['videos'])]) for key, value in folder_info.items()
                ])
            ])
        ]),
        dcc.Loading(
            id="loading",
            type="default",
            children=[
                html.Div(id="metadata-dashboard")
            ]
        )
    ])
    
    @app.callback(
        Output('metadata-dashboard', 'children'),
        Input('loading', 'children')
    )
    def update_dashboard(_):
        metadata_df = gather_metadata(folder_path)
        if metadata_df.empty:
            return html.P("No metadata found. Check the folder path or the file types.")
        else:
            metadata_df.to_csv(os.path.join(script_dir, 'metadata.csv'), index=False)
            return dcc.Tabs([
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
                    html.Table([
                        html.Thead([
                            html.Tr([
                                html.Th("Filename"), html.Th("Thumbnail"), html.Th("MSCN Coefficients"), html.Th("NIQE Features"), html.Th("PIQE Index"), html.Th("JPEG Quality"), html.Th("BLIINDS Features"), html.Th("CORNIA Features"), html.Th("SSEQ"), html.Th("FQADI Features")
                            ])
                        ]),
                        html.Tbody([
                            html.Tr([
                                html.Td(img['filename']),
                                html.Td(html.Img(src=img['thumbnail'], style={'height': '50px', 'width': '50px'})),
                                html.Td(str(img['calculate_mscn_coefficients'])),
                                html.Td(str(img['compute_niqe_features'])),
                                html.Td(str(img['calculate_piqe_index'])),
                                html.Td(str(img['estimate_jpeg_quality'])),
                                html.Td(str(img['compute_bliinds_features'])),
                                html.Td(str(img['extract_cornia_features'])),
                                html.Td(str(img['calculate_sseq'])),
                                html.Td(str(img['calculate_fqadi_features']))
                            ]) for img in metadata_df.to_dict('records')
                        ])
                    ])
                ])
            ])
    
    app.run_server(debug=True)
