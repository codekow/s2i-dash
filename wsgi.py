from dash import dash, html, dcc
from dash.dependencies import Input, Output


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

app.layout = html.Div([])

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")  # nosec
