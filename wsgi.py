# used to display only
from dash import dash, dcc, html

# used for interactive callbacks
from dash import Input, Output

# import app elements
from apps import model

df = model.df

import plotly.express as px

app = dash.Dash(__name__)

# 'application' reference required for wgsi / gunicorn
# https://docs.openshift.com/container-platform/3.11/using_images/s2i_images/python.html#using-images-python-configuration
application = app.server

# from flask import request
# @application.before_request
# def print_header():
#     print('============== START HEADERS ==============')
#     print(request.headers)
#     print('=============== END HEADERS ===============')

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")  # nosec
