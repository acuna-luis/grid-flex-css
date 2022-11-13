#!/usr/bin/env python
import dash
from dash import dcc
from dash import html
from dash.html import Iframe
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from flask import redirect
from flask_login import logout_user, current_user
from flask import Flask, request
from urllib.parse import urlparse
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=yes'
        }
    ],
    external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(
        className="titulo",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ]), className="app-header--description"
    )
])


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')

