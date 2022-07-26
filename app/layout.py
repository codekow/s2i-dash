'''
This is an example file which takes as an input the output of the data scientist's model.

This might be a csv, array, dataframe, or whatever

It should return a plotly layout object, which is consumed (wsgi.py)
'''

# used to display only
from dash import dash, dcc, html

# used for interactive callbacks
from dash import Input, Output

# pull in data to display
from app import model

# TODO return df instead of reference obj
df = model.df

import plotly.express as px

app = dash.Dash(__name__)

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
