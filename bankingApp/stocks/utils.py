import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, width=10, height=5, title='', x_label='', y_label='', outside_color='white', inside_color='white', bar_plot_colors='green', color='green', x_ticks=None, plot_linestyle='solid', bar_plot=False):
    plt.switch_backend('AGG')
    # plt.figure(figsize=(width, height))
    plt.figure(figsize=(width, height), facecolor=outside_color)
    plt.title(title)

    if bar_plot:
        plt.bar(x, y, color=bar_plot_colors)
    else:
        plt.plot(x, y, color=color, linestyle=plot_linestyle)
        plt.grid(color='red', linestyle='--')

    if x_ticks is not None:
        plt.xticks(x, x_ticks, rotation=-90)
    else:
        plt.xticks(rotation=-90)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    #
    ax = plt.gca()
    ax.set_facecolor(inside_color)
    graph = get_graph()
    return graph
