import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def add_footer(ax, pattern_name):
    ax.text(1, 0.5, f"{pattern_name} - Pirahansiah.com", 
            horizontalalignment='right', verticalalignment='bottom', 
            transform=ax.transAxes, fontsize=4, color='gray')

def create_concept_map(levels, colors, file_name_base):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.patch.set_alpha(0)
    
    y_spacing = 10  # Vertical spacing between levels
    x_spacing = 5   # Horizontal spacing between nodes
    
    def draw_node(ax, center, level, shape, color):
        if shape == 'circle':
            node = patches.Circle(center, radius=1.5, edgecolor='black', facecolor=color, lw=2)
        else:
            node = patches.FancyBboxPatch((center[0] - 1.5, center[1] - 1.5), 3, 3, boxstyle="round,pad=0.3", edgecolor='black', facecolor=color, lw=2)
        ax.add_patch(node)
        return center
    
    # Draw main concept node (circle)
    main_center = (0, 0)
    draw_node(ax, main_center, 0, 'circle', 'lightgray')
    
    # Draw other nodes (squares) and arrange them in levels
    current_level = 1
    for level_nodes in levels:
        y = -current_level * y_spacing
        for i in range(level_nodes):
            x = (i - level_nodes / 2) * x_spacing
            color_index = (current_level - 1) % len(colors)
            draw_node(ax, (x, y), current_level, 'square', colors[color_index])
        current_level += 1
    
    add_footer(ax, 'Concept Map')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.png'))
    svg_file_path = os.path.abspath(os.path.join(current_dir, f'{file_name_base}.svg'))
    
    # Save as PNG
    fig.savefig(png_file_path, dpi=300, transparent=True)
    
    # Save as SVG
    fig.savefig(svg_file_path, format='svg', transparent=True)
    
    plt.close(fig)

# Example usage
levels = [3, 5, 7, 9]  # Number of nodes per level
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99']  # Different colors for each level
file_name_base = 'concept_map'

create_concept_map(levels, colors, file_name_base)
