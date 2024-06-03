import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import matplotlib.backends.backend_svg as svg

def create_dot_pattern(size_cm, dots_per_cm, file_name_base):
    size_inch = [dim / 2.54 for dim in size_cm]
    dots_per_inch = dots_per_cm * 2.54

    fig, ax = plt.subplots(figsize=size_inch, dpi=300)
    ax.set_xlim(0, size_cm[0])
    ax.set_ylim(0, size_cm[1])
    ax.set_xticks(np.arange(0, size_cm[0], 1/dots_per_cm))
    ax.set_yticks(np.arange(0, size_cm[1], 1/dots_per_cm))
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=0.5)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Save as PNG
    canvas = agg.FigureCanvasAgg(fig)
    canvas.print_figure(f'{file_name_base}.png', dpi=300)
    
    # Save as SVG
    canvas_svg = svg.FigureCanvasSVG(fig)
    canvas_svg.print_svg(f'{file_name_base}.svg')

    plt.close(fig)

# A5 size in cm (14.8 cm x 21 cm)
a5_size_cm = [14.8, 21]
dots_per_cm = 1  # Adjust for density of dots

create_dot_pattern(a5_size_cm, dots_per_cm, 'journal_pattern')
