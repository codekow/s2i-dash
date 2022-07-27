# Example Dash OpenShift / s2i Repo
This is meant to be a good starting point for creating Dash applications that are deployed to OpenShift.

Open an issue or PR if the explanations below are inadequate, and we can help get you up to speed! :thumbsup:

## How to use this repo to build your own application

1. Fork this repository into your own Git repo
    - This will create a copy that you will own
2. Log into OpenShift
2. Select the project in which you want to add an application
    - There will be a dropdown of projects you have permissions to
3. Go to the catalog and select 'python' to create a new python application
4. Enter the app name and the URL for the app's repository (from step #1),
5. Click 'Create'

## Local development

```
python -m venv venv
. ./venv/bin/activate

pip install -U pip
pip install -r requirements.txt

python wsgi.py
```
Access via http://localhost:8080/

## WSGI / gunicorn

This sample Python application relies on the support provided by the default S2I builder for deploying a WSGI application using the ``gunicorn`` WSGI server. The requirements which need to be satisfied for this to work are:

* The WSGI application code file needs to be named ``wsgi.py``.
* The WSGI application entry point within the code file needs to be named ``application``.
* The ``gunicorn`` package must be listed in the ``requirements.txt`` file for ``pip``.

In addition, the ``.s2i/environment`` file has been created to allow environment variables to be set to override the behavior of the default S2I builder for Python.

* The environment variable ``APP_CONFIG`` has been set to declare the name of the config file for ``gunicorn``.

See https://github.com/OpenShiftDemos/os-sample-python

## More information about this project

This repo contains an example dash application that can be deployed to OpenShift using Source to Image (S2I). Here are the main files:

1. The Dash Application (learn about Dash [HERE](https://dash.plotly.com/) )

    - `wsgi.py`;  main application, to be run by gunicorn

    - `app/model.py`;  an optional file, to demonstrate how to modularize code

    - `app/layout.py`;  an optional file, to demonstrate how to modularize code

2. The S2I environment variables. Used to setup additional environment varibles (ex: setup packages using a Nexus repository)

    - `.s2i/environment`

3. This file should contain the dependencies that your application needs to run, and those dependencies should be 'pinned' to a version.

    - `requirements.txt`

    One way to create a requirements file for your application is by running the following:

    ```
    pip freeze > requirements.txt
    ```

#### How it works

The file `wsgi.py` contains the instructions for python to run Dash. 

It relies on `app/model.py` to run calculations on some data, and on `app/layout.py` to return a plotly figure that can be shown by the application. 

When s2i builds the container, it will look into `.s2i` for additional instructions, including environment variables for installing packages with `pip`.


## Links
- [Python s2i examples](https://github.com/sclorg/s2i-python-container/tree/master/examples)
- [Dash (Plotly)](https://dash.plotly.com/)