import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def get_config(defaults, section):
    config = defaults.copy()
    config.update(section)
    return config

def add_footer(ax, pattern_name):
    ax.text(1, 0.5, f"{pattern_name} - Pirahansiah.com", 
            horizontalalignment='right', verticalalignment='bottom', 
            transform=ax.transAxes, fontsize=4, color='gray')

def create_dot_pattern(config):
    size_cm = config['size_cm']
    dot_spacing_cm = config['dot_spacing_cm']
    dot_diameter_cm = config['dot_diameter_cm']
    file_name_base = config['file_name_base']
    colors = config['colors']
    
    size_inch = [dim / 2.54 for dim in size_cm]
    dot_spacing_inch = dot_spacing_cm / 2.54
    dot_diameter_inch = dot_diameter_cm / 2.54

    fig, ax = plt.subplots(figsize=size_inch)
    ax.set_xlim(0, size_cm[0])
    ax.set_ylim(0, size_cm[1])
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    color_index = 0
    for x in np.arange(0, size_cm[0], dot_spacing_cm):
        for y in np.arange(0, size_cm[1], dot_spacing_cm):
            color = colors[color_index % len(colors)]
            circle = plt.Circle((x, y), dot_diameter_cm / 2, color=color, fill=True)
            ax.add_artist(circle)
            color_index += 1
    
    add_footer(ax, 'Journal Dot Pattern')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)

    plt.close(fig)

def create_double_bubble_map(config):
    size_cm = config['size_cm']
    main_nodes = config['main_nodes']
    total_nodes = config['total_nodes']
    file_name_base = config['file_name_base']
    colors = config['colors']
    
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
        color = colors[i % len(colors)]
        main_node_positions.append(draw_bubble(ax, (x, y), color))
    
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
            color = colors[(i * secondary_nodes_per_main + j) % len(colors)]
            ax.plot([mx, x], [my, y], 'k-', lw=1)
            draw_bubble(ax, (x, y), color)
    
    add_footer(ax, 'Double Bubble Map')
    
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
    colors = config['colors']
    
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
    ax.plot([margin, margin], [size_cm[1], bottom_margin], color=colors[0], lw=line_width)
    ax.plot([0, size_cm[0]], [bottom_margin, bottom_margin], color=colors[1 % len(colors)], lw=line_width)
    
    # Optional: Draw horizontal lines for writing
    line_spacing_cm = config['line_spacing_cm']
    for i, y in enumerate(np.arange(bottom_margin + line_spacing_cm, size_cm[1], line_spacing_cm)):
        color = colors[(i + 2) % len(colors)]
        ax.plot([margin, size_cm[0]], [y, y], color=color, lw=line_width / 2)
    
    add_footer(ax, 'Cornell Note')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)

    plt.close(fig)

def create_ruled_narrow_template(config):
    size_cm = config['size_cm']
    line_spacing_cm = config['line_spacing_cm']
    file_name_base = config['file_name_base']
    colors = config['colors']
    
    size_inch = [dim / 2.54 for dim in size_cm]
    
    fig, ax = plt.subplots(figsize=size_inch)
    ax.set_xlim(0, size_cm[0])
    ax.set_ylim(0, size_cm[1])
    ax.set_aspect('auto')
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    # Draw horizontal lines for writing
    line_width = 1  # Thicker line width
    for i, y in enumerate(np.arange(line_spacing_cm, size_cm[1], line_spacing_cm)):
        color = colors[i % len(colors)]
        ax.plot([0, size_cm[0]], [y, y], color=color, lw=line_width)
    
    add_footer(ax, 'Ruled Narrow')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)

    plt.close(fig)

def create_storyboard_template(config):
    size_cm = config['size_cm']
    rows = config['rows']
    columns = config['columns']
    file_name_base = config['file_name_base']
    colors = config['colors']
    
    size_inch = [dim / 2.54 for dim in size_cm]
    
    fig, ax = plt.subplots(figsize=size_inch)
    ax.set_xlim(0, size_cm[0])
    ax.set_ylim(0, size_cm[1])
    ax.set_aspect('auto')
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    # Calculate the size of each cell
    cell_width = size_cm[0] / columns
    cell_height = size_cm[1] / rows
    
    # Draw the grid for the storyboard
    line_width = 1  # Thicker line width
    for row in range(rows + 1):
        color = colors[row % len(colors)]
        ax.plot([0, size_cm[0]], [row * cell_height, row * cell_height], color=color, lw=line_width)
    for col in range(columns + 1):
        color = colors[col % len(colors)]
        ax.plot([col * cell_width, col * cell_width], [0, size_cm[1]], color=color, lw=line_width)
    
    add_footer(ax, 'Storyboard')
    
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
config_data = read_config(config_file)
default_config = config_data['default']

# Create the dot pattern
dot_pattern_config = get_config(default_config, config_data['journal_dot_pattern'])
create_dot_pattern(dot_pattern_config)

# Create the double bubble map
double_bubble_map_config = get_config(default_config, config_data['double_bubble_map'])
create_double_bubble_map(double_bubble_map_config)

# Create the Cornell note template
cornell_note_config = get_config(default_config, config_data['cornell_note'])
create_cornell_note_template(cornell_note_config)

# Create the ruled narrow template
ruled_narrow_config = get_config(default_config, config_data['ruled_narrow'])
create_ruled_narrow_template(ruled_narrow_config)

# Create the storyboard template
storyboard_config = get_config(default_config, config_data['storyboard'])
create_storyboard_template(storyboard_config)
