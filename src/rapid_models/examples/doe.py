import numpy as np
from scipy import stats
import plotly.graph_objs as go

from rapid_models import doe


def doe_example_plot(nsamp=25, doe_type='lhs', dimensions=2):

    if doe_type == "lhs":
        xs = doe.lhs(2, nsamp)
    elif doe_type == "fullfact":
        ffact = doe.fullfact([int(nsamp**(0.5))]*2)
        ffact_norm = ffact/ffact.max()
        xs = ffact_norm+0.01
    elif doe_type == "adaptive":
        xs = doe.lhs(2, int(nsamp/4))
        tmp = np.random.rand(int(nsamp/4*3))  # *(1-0.5)+0.5

        xs = np.vstack([xs, np.vstack([0.1+2*stats.norm.pdf(tmp*1.5)+np.random.rand(len(tmp))*0.05, tmp]).T])

    if doe_type == "lhs":
        bShowGrid = True
    else:
        bShowGrid = False
    tickvals = np.linspace(0, 1, nsamp+1)

    fig = go.Figure()

    fig.add_scatter(x=xs[:, 0], y=xs[:, 1], name="samples",
                    mode="markers",
                    marker={"size": 7, "color": "black"}
                    )
    fig.update_layout(width=400, height=400,
                      margin={"t": 10, "r": 10, "b": 10, "l": 10},
                      xaxis={"title": "$X_1$",
                             'range': [-0.0, 1.01], 'tickmode': 'array', 'tickvals': tickvals, 'showticklabels': False,
                             "showgrid": bShowGrid, "gridwidth": 1, "gridcolor": 'lightgrey',
                             "zeroline": True, "zerolinecolor": "black"},
                      yaxis={"title": "$X_2$",
                             'range': [-0.0, 1.01], 'tickmode': 'array', 'tickvals': tickvals, 'showticklabels': False,
                             "showgrid": bShowGrid, "gridwidth": 1, "gridcolor": 'lightgrey',
                             "zeroline": True, "zerolinecolor": "black"},
                      font={
                          "family": "Times New Roman",
                          "size": 22,
                      },
                      legend={"orientation": "h"},
                      paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)"  # "#FFFFFF"
                      )

    return fig
