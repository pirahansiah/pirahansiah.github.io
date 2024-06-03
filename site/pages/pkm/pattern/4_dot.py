import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    for x in np.arange(0, size_cm[0], dot_spacing_cm):
        for y in np.arange(0, size_cm[1], dot_spacing_cm):
            circle = plt.Circle((x, y), dot_diameter_cm / 2, color='black', fill=True)
            ax.add_artist(circle)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)

    plt.close(fig)

def create_double_bubble_map(config):
    main_nodes = config['main_nodes']
    total_nodes = config['total_nodes']
    file_name_base = config['file_name_base']
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    def draw_bubble(ax, center, color):
        bubble = patches.Circle(center, radius=1.5, edgecolor='black', facecolor=color, lw=2)
        ax.add_patch(bubble)
        return center
    
    # Draw main nodes
    main_node_positions = []
    for i in range(main_nodes):
        angle = i * 360 / main_nodes
        x = 10 * np.cos(np.radians(angle))
        y = 10 * np.sin(np.radians(angle))
        main_node_positions.append(draw_bubble(ax, (x, y), 'lightblue'))
    
    # Connect main nodes to each other
    for i in range(main_nodes):
        for j in range(i+1, main_nodes):
            ax.plot([main_node_positions[i][0], main_node_positions[j][0]], 
                    [main_node_positions[i][1], main_node_positions[j][1]], 
                    'k-', lw=1)
    
    # Draw and connect secondary nodes to the nearest main node
    secondary_nodes_per_main = total_nodes // main_nodes
    for i, (mx, my) in enumerate(main_node_positions):
        for j in range(secondary_nodes_per_main):
            angle = j * 360 / secondary_nodes_per_main
            x = mx + 5 * np.cos(np.radians(angle))
            y = my + 5 * np.sin(np.radians(angle))
            ax.plot([mx, x], [my, y], 'k-', lw=1)
            draw_bubble(ax, (x, y), 'lightgreen')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)

    plt.close(fig)

def create_cornell_note_template(config):
    size_cm = config['size_cm']
    file_name_base = config['file_name_base']
    
    size_inch = [dim / 2.54 for dim in size_cm]
    
    fig, ax = plt.subplots(figsize=size_inch)
    ax.set_xlim(0, size_cm[0])
    ax.set_ylim(0, size_cm[1])
    ax.set_aspect('auto')
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    # Draw lines for the Cornell note layout
    margin = 2.5  # Left margin for the keywords/questions
    bottom_margin = 5  # Bottom margin for the summary
    line_width = 1  # Thicker line width
    
    # Main note-taking area
    ax.plot([margin, margin], [size_cm[1], bottom_margin], color='black', lw=line_width)
    ax.plot([0, size_cm[0]], [bottom_margin, bottom_margin], color='black', lw=line_width)
    
    # Optional: Draw horizontal lines for writing
    line_spacing_cm = 0.85
    for y in np.arange(bottom_margin + line_spacing_cm, size_cm[1], line_spacing_cm):
        ax.plot([margin, size_cm[0]], [y, y], color='gray', lw=line_width / 2)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)

    plt.close(fig)

# Path to the configuration file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.abspath(os.path.join(current_dir, 'config.json'))

# Read the configuration settings
config = read_config(config_file)

# Create the dot pattern
create_dot_pattern(config['journal_dot_pattern'])

# Create the double bubble map
create_double_bubble_map(config['double_bubble_map'])

# Create the Cornell note template
create_cornell_note_template(config['cornell_note'])
