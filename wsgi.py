# import app elements
from app import layout

app = layout.app

# 'application' reference required for wgsi / gunicorn
# https://docs.openshift.com/container-platform/3.11/using_images/s2i_images/python.html#using-images-python-configuration
application = app.server

# from flask import request
# @application.before_request
# def print_header():
#     print('============== START HEADERS ==============')
#     print(request.headers)
#     print('=============== END HEADERS ===============')

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")  # nosec

# run gunicorn manually
# TODO: move to readme
# gunicorn wsgi:application -b 0.0.0.0:8080
