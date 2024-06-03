import os
import json
import numpy as np
import matplotlib.pyplot as plt

def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def get_config(defaults, section):
    config = defaults.copy()
    config.update(section)
    return config

def add_footer(ax, pattern_name):
    ax.text(1, 0.01, f"{pattern_name} - Pirahansiah.com", 
            horizontalalignment='right', verticalalignment='bottom', 
            transform=ax.transAxes, fontsize=4, color='gray')

def create_template(config, sections, pattern_name):
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
    
    # Draw section headers
    y_positions = np.linspace(size_cm[1], 0, len(sections) + 1)
    for i, (section, y) in enumerate(zip(sections, y_positions[1:])):
        color = colors[i % len(colors)]
        ax.text(0.5, y + 0.3, section, fontsize=10, color=color, ha='center', transform=ax.transData)
        if i < len(sections) - 1:
            ax.plot([0, size_cm[0]], [y, y], color=color, lw=1)
    
    add_footer(ax, pattern_name)
    
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

# Create templates for different note types
note_templates = {
    'meeting_notes': ['Date', 'Attendees', 'Agenda', 'Notes', 'Action Items'],
    'conference_notes': ['Date', 'Speaker', 'Topic', 'Key Points', 'Notes'],
    'workshop_notes': ['Date', 'Instructor', 'Topic', 'Key Learnings', 'Notes'],
    'study_notes': ['Date', 'Subject', 'Topic', 'Summary', 'Detailed Notes']
}

for template_name, sections in note_templates.items():
    config = get_config(default_config, config_data[template_name])
    create_template(config, sections, template_name.replace('_', ' ').title())
