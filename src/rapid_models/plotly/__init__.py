from plotly import graph_objects as go


def Figure(data=None, layout=None):
    return go.Figure(data=data, layout=layout)


def export_fig(fig, config=None, asType='json'):  # , filename=None):
    """
    asType: enum of 'json' outputting plotly json, 'html' outputting a standalone 'html' file, 'div' outputting a text string of <div> to embed in html code, 'png','jpg','jpeg','svg','pdf' outputting file of said format.
    """

    if asType == 'html':
        # if filename is None:
        return fig.to_html(config=config, include_plotlyjs='cdn', include_mathjax='cdn', full_html=True)
        # else:
        #     return fig.write_html(file=filename, config=config, include_plotlyjs='cdn', include_mathjax='cdn', full_html=True)
    elif asType == 'div':
        # if filename is None:
        return fig.to_html(config=config, include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)
        # else:
        #     return fig.write_html(file=filename, config=config, include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)
    elif asType in ['png', 'jpg', 'jpeg', 'svg', 'pdf']:
        # if filename is None:
        return fig.to_image(format=asType)
        # else:
        #     return fig.write_image(file=filename, format=asType)
    else:
        # if filename is None:
        return fig.to_json(pretty=False)
        # else:
        #     return fig.write_json(file=filename, pretty=False)
