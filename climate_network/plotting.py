"""Plotting-related stuff."""

from contextlib import contextmanager

from matplotlib import pyplot as plt

# Article on function-based context manager: https://realpython.com/python-with-statement/#creating-function-based-context-managers

LATEX_PLOT_STYLE = {
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath,bm}",
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 11,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 300,
    "figure.figsize": [6, 4],
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.alpha": 0.5,
    "mathtext.fontset": "cm",
}


@contextmanager
def LaTeX_plot_style():
    """Context manager for custom matplotlib plotting style with LaTeX rendering."""
    # Store original rcParams
    original_rcParams = plt.rcParams.copy()

    try:
        plt.style.use("default")
        plt.rcParams.update(LATEX_PLOT_STYLE)

        yield

    finally:
        # Restore original rcParams
        plt.rcParams.update(original_rcParams)
