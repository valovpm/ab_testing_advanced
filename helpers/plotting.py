
import numpy as np
import plotly.graph_objects as go


def trace_pvalues_histogram(pvalues, name, bin_size=0.05):
    """
    Get trace of histogram, specifically tuned to show pvalue-distribution during AA-testing and AB-testing
    :param pvalues: data containing p-values
    :param name: for example "AA-testing p-values" or "AB-testing p-values"
    :param bin_size: is equal to default significance level (5%), making it easier to assess type-I error
    :return: histogram of p-values
    """
    trace = go.Histogram(
        x=pvalues,
        opacity=0.6,  # non-transparency
        name=name,  # p-values name
        # nbinsx=n_bins,
        xbins=dict(
            start=0,  # minimum value of a p-value is 0
            end=1,  # maximum value of a p-value is 1
            size=bin_size  # bin size, can be equal to a significance level
        ),
    )

    return trace


def trace_pvalues_ecdf(pvalues, name='ECDF of p-values'):
    # Sort data and compute ECDF
    x = np.sort(pvalues)
    y = np.arange(1, len(x) + 1) / len(x)

    trace = go.Scatter(x=x, y=y, mode='lines', name=name)
    return trace


def plot_pvalues_histogram(pvalues, name, bin_size=0.05):
    # Create the histogram trace
    trace = trace_pvalues_histogram(pvalues, name, bin_size)

    # Create the histogram figure
    fig = go.Figure(data=[trace])

    # Update layout
    fig.update_layout(
        template='plotly_dark',
        title=name,
        width=500,
        height=500,
        xaxis_title="value",
        yaxis_title="count",
    )

    fig.show()


def plot_pvalues_ecdf(pvalues, name='ECDF of p-values'):
    """
    Plot empirical cumulative distribution function of p-values
    """

    # Create ECDF trace
    trace = trace_pvalues_ecdf(pvalues, name)
    fig = go.Figure(data=[trace])

    # Define number of grid lines
    num_grid_lines = 11

    # Axis ranges
    x_range = [np.min(pvalues), np.max(pvalues)]
    y_range = [0, 1]

    # Compute ticks
    x_ticks = np.round(np.linspace(*x_range, num=num_grid_lines), decimals=1)
    y_ticks = np.linspace(*y_range, num=num_grid_lines)

    # Update layout to control grid lines
    fig.update_layout(
        template='plotly_dark',
        title=name,
        width=500,
        height=500,
        xaxis=dict(
            title='value',
            tickmode='array',
            tickvals=x_ticks,
            showgrid=True,
            gridcolor='lightgrey'
        ),
        yaxis=dict(
            title='ECDF',
            tickmode='array',
            tickvals=y_ticks,
            showgrid=True,
            gridcolor='lightgrey'
        )
    )

    fig.show()


def plot_compare_histograms(x, x_label, y, y_label, title, height=500, width=500):
    # Create the histogram traces
    trace1 = go.Histogram(x=x, opacity=0.6, name=x_label, nbinsx=100)
    trace2 = go.Histogram(x=y, opacity=0.6, name=y_label, nbinsx=100)

    # Create the figure
    fig = go.Figure(data=[trace1, trace2])

    # Update layout for better visibility
    fig.update_layout(
        template='plotly_dark',
        title= title,
        width=width,
        height=height,
        barmode="overlay",  # Overlay the histograms instead of stacking
        xaxis_title="Value",
        yaxis_title="Count",
    )

    fig.show()


def plot_scatter(x, x_label, y, y_label, title='scatter plot'):
    # Create scatter plot
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=dict(size=8)))

    fig.update_layout(
        template='plotly_dark',
        title=title,
        width=500,
        height=500,
        xaxis_title=x_label,
        yaxis_title=y_label,
        xaxis=dict(showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(showgrid=True, gridcolor='lightgrey')
    )

    fig.show()

