import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import matplotlib.backends.backend_svg as svg

def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def create_dot_pattern(config):
    size_cm = config['size_cm']
    dot_spacing_cm = config['dot_spacing_cm']
    dot_diameter_cm = config['dot_diameter_cm']
    file_name_base = config['file_name_base']
    
    size_inch = [dim / 2.54 for dim in size_cm]
    dot_spacing_inch = dot_spacing_cm / 2.54
    dot_diameter_inch = dot_diameter_cm / 2.54

    fig, ax = plt.subplots(figsize=size_inch)
    ax.set_xlim(0, size_cm[0])
    ax.set_ylim(0, size_cm[1])
    ax.set_aspect('equal')

    for x in np.arange(0, size_cm[0], dot_spacing_cm):
        for y in np.arange(0, size_cm[1], dot_spacing_cm):
            circle = plt.Circle((x, y), dot_diameter_cm / 2, color='black', fill=True)
            ax.add_artist(circle)
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    canvas = agg.FigureCanvasAgg(fig)
    canvas.print_figure(png_file_path, dpi=300)
    
    # Save as SVG
    canvas_svg = svg.FigureCanvasSVG(fig)
    canvas_svg.print_svg(svg_file_path)

    plt.close(fig)

# Path to the configuration file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.abspath(os.path.join(current_dir, 'config.json'))

# Read the configuration settings
config = read_config(config_file)

# Create the dot pattern
create_dot_pattern(config)
