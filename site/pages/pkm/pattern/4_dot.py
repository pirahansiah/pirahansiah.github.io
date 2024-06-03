import json
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from itertools import cycle

# Path to the configuration file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.abspath(os.path.join(current_dir, 'config.json'))

def add_footer(ax, pattern_name):
    ax.text(1, 0.01, f"{pattern_name} - Pirahansiah.com",
            horizontalalignment='right', verticalalignment='bottom',
            transform=ax.transAxes, fontsize=4, color='gray')

def create_dot_pattern(config, key, pattern_name):
    pattern_config = config[key]
    
    # Extract configuration
    size_cm = pattern_config.get('size_cm', config['default']['size_cm'])
    line_spacing_cm = pattern_config.get('line_spacing_cm', config['default']['line_spacing_cm'])
    dot_diameter_cm = pattern_config.get('dot_diameter_cm', config['default']['dot_diameter_cm'])
    dot_spacing_cm = pattern_config.get('dot_spacing_cm', config['default'].get('dot_spacing_cm', 0.85))
    file_name_base = pattern_config.get('file_name_base', config['default']['file_name_base'])
    colors = pattern_config.get('colors', config['default']['colors'])
    
    # Convert cm to inches for matplotlib
    size_in = [x / 2.54 for x in size_cm]
    dot_diameter_in = dot_diameter_cm / 2.54
    dot_spacing_in = dot_spacing_cm / 2.54

    # Create figure and axis
    fig, ax = plt.subplots(figsize=size_in)
    ax.set_xlim(0, size_in[0])
    ax.set_ylim(0, size_in[1])
    ax.set_aspect('equal')
    ax.axis('off')

    color_cycle = cycle(colors)
    y = dot_spacing_in
    while y < size_in[1]:
        x = dot_spacing_in
        while x < size_in[0]:
            color = next(color_cycle)
            dot = patches.Circle((x, y), dot_diameter_in / 2, color=color, fill=True)
            ax.add_patch(dot)
            x += dot_spacing_in
        y += dot_spacing_in
    
    add_footer(ax, pattern_name)
    
    # Save as PNG
    plt.savefig(f'{file_name_base}_{pattern_name}.png', format='png', bbox_inches='tight', pad_inches=0, transparent=True)
    # Save as SVG
    plt.savefig(f'{file_name_base}_{pattern_name}.svg', format='svg', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()

def create_text_image(text, file_name):
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.text(0.5, 0.5, text, verticalalignment='center', horizontalalignment='center', 
            transform=ax.transAxes, fontsize=12, wrap=True)
    ax.axis('off')

    # Save as PNG
    plt.savefig(f'{file_name}.png', format='png', bbox_inches='tight', pad_inches=0, transparent=True)
    # Save as SVG
    plt.savefig(f'{file_name}.svg', format='svg', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()

def generate_second_brain(config):
    create_dot_pattern(config, 'default', 'second_brain')

def generate_zettelkasten(config):
    create_dot_pattern(config, 'default', 'zettelkasten')

def generate_smart_notes(config):
    smart_notes_text = """# Smart Notes

## Table of Contents
1. [Index](#index)
2. [Fleeting Notes](#fleeting-notes)
3. [Literature Notes](#literature-notes)
4. [Permanent Notes](#permanent-notes)
5. [Tags](#tags)

---

## Index
*A directory of your notes.*

- [20240603A](#20240603A) - Fleeting Note 1
- [20240603B](#20240603B) - Literature Note 1
- [20240603C](#20240603C) - Permanent Note 1

---

## Fleeting Notes
*Quick, temporary notes to capture ideas.*

### 20240603A - Fleeting Note 1
- Idea or thought captured quickly.
- Reference or context (if any).

---

### 20240603B - Fleeting Note 2
- Idea or thought captured quickly.
- Reference or context (if any).

---

## Literature Notes
*Notes taken from reading materials.*

### 20240603C - Literature Note 1
**Source:**
- [Book Title] by [Author]
- [Article Title] by [Author]
- [Website Title] ([URL])

**Summary:**
- Key points and ideas.

**Quotes:**
- "Relevant quote from the text."

**Comments:**
- Personal thoughts or connections.

---

### 20240603D - Literature Note 2
**Source:**
- [Book Title] by [Author]
- [Article Title] by [Author]
- [Website Title] ([URL])

**Summary:**
- Key points and ideas.

**Quotes:**
- "Relevant quote from the text."

**Comments:**
- Personal thoughts or connections.

---

## Permanent Notes
*Well-thought-out notes that capture insights and ideas.*

### 20240603E - Permanent Note 1
**Content:**
- Description of the main idea or concept.
- Explanation and analysis.

**Links:**
- Related notes: [[20240603C]], [[20240603D]]

**Tags:**
- #tag1 #tag2

---

### 20240603F - Permanent Note 2
**Content:**
- Description of the main idea or concept.
- Explanation and analysis.

**Links:**
- Related notes: [[20240603E]], [[20240603B]]

**Tags:**
- #tag3 #tag4

---

## Tags
*A list of tags for categorizing notes.*

- **#tag1:** Description of tag1
- **#tag2:** Description of tag2
- **#tag3:** Description of tag3
- **#tag4:** Description of tag4

---

*This template can be customized to fit your specific needs. Use it to keep your fleeting notes, literature notes, and permanent notes well-organized and easily accessible.*
"""
    create_text_image(smart_notes_text, 'smart_notes')

# Load configuration
with open(config_file, 'r') as f:
    config = json.load(f)

# Generate images for the three methods
generate_second_brain(config)
generate_zettelkasten(config)
generate_smart_notes(config)
