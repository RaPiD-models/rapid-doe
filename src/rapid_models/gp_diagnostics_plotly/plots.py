import numpy as np
import plotly.graph_objs as go

from .utils import snorm_qq

def qq_residuals(y_pred_mean, y_pred_var, y_test, title = '', showlegend = True):
    """
    Create QQ plot
    Input: 
    y_pred_mean - prediction mean
    y_pred_var - prediction variance
    y_test - true y value
    title - (optional) 
    Output:
    fig - plotly figure
    """

    # Calculate residuals
    y_pred_std = np.power(y_pred_var, 0.5)
    residuals_y = (y_pred_mean - y_test)/y_pred_std # Standardized residuals

    # Calculate QQ data
    q_sample, q_snorm, q_snorm_upper, q_snorm_lower = snorm_qq(residuals_y)

    qq_scatter = go.Scatter(
        x = q_snorm,
        y = q_sample,
        mode = 'markers',
        marker = dict(
            size = 6,
            color='rgb(105, 144, 193)'
        ),
        name = 'Data'
    )

    qq_upper = go.Scatter(
        x = q_snorm_upper,
        y = q_sample,
        mode = 'lines',
        line = dict(
            color='rgb(150, 150, 150)',
            dash = 'dot'
        ),
        name = '95% confidence band',
        legendgroup = 'conf'
    )

    qq_lower = go.Scatter(
        x = q_snorm_lower,
        y = q_sample,
        mode = 'lines',
        line = dict(
            color='rgb(150, 150, 150)',
            dash = 'dot'
        ),
        name = 'lower',
        legendgroup = 'conf',
        showlegend = False
    )

    minval = np.min([q_sample.min(), q_snorm.min()])
    maxval = np.max([q_sample.min(), q_snorm.max()])

    line = go.Scatter(
        x = [minval, maxval],
        y = [minval, maxval],
        mode = 'lines',
        line = dict(
            color='rgb(0, 0, 0)',
            dash = 'dash'
        ),
        name = 'x = y'
    )

    layout = go.Layout(
        title=title,
        showlegend=showlegend,
        autosize=False,
        width=700,
        height=600,
        xaxis=dict(
            title='Standard normal quantiles',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            ),
            range = [q_snorm.min() - 0.2, q_snorm.max() + 0.2]
        ),
        yaxis=dict(
            title='Sample quantiles',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

    data = [qq_scatter, qq_upper, qq_lower, line]
    fig = go.Figure(data=data, layout=layout)
    
    return fig