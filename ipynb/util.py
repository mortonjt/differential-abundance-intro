import numpy as np


def default_barplot(ax, x, t, ticks=False):
    ax.fill_between(t, x[:, 0], label='x1')
    ax.fill_between(t, x[:, 0], x[:, 0] + x[:, 1], label='x2')
    ax.fill_between(t, x[:, 0] + x[:, 1], x[:, 0] + x[:, 1] + x[:, 2], label='x3')
    ax.set_ylabel('Proportion', fontsize=18)
    if ticks is False:
        ax.set_xticks([])
    return ax

def default_ternary_labels(tax):

    # Draw Boundary and Gridlines
    tax.boundary(linewidth=2.0)
    tax.gridlines(multiple=0.2, color="blue")


    tax.ticks(axis='lbr', linewidth=1, tick_formats="%.1f",
              offset=0.02,  multiple=0.2) # Set ticks
    tax.get_axes().axis('off')
    tax.clear_matplotlib_ticks()

    # Set Axis labels and Title
    fontsize = 20
    tax.left_axis_label("$x_3$", fontsize=fontsize, fontdict={'color':  'black'})
    tax.right_axis_label("$x_2$", fontsize=fontsize, fontdict={'color':  'black'})
    tax.bottom_axis_label("$x_1$", fontsize=fontsize, fontdict={'color':  'black'})
    return tax


def extract_log_fold_change(fit, n, p, mc_samples=1000):
    colnames = np.array(fit.column_names)
    beta_idx = np.array(list(map(lambda x: 'beta' in x, colnames)))
    beta_samples = fit.variational_sample.iloc[:, beta_idx].values.reshape((
        mc_samples, n - 1, p))
    return beta_samples
