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
import base64, os

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
image_filename = os.getcwd()+'/assets/img/fcgui_logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app.layout = html.Div([
    html.Header([
        html.Div([
            html.Span('Herramientas'),
            html.Div([html.P('Rechazo'), html.P('My Web')], className='dropdown-content')], 
        className="dropdown"),
        html.Div([],
        style={'background-image': 'url("/assets/img/fcgui_logo.png")',
            'background-repeat': 'no-repeat',
            'margin-top': '5px',
        }
        )
    ]),
   
    html.Div([
        #First row
        html.Div([
            html.Div( 
                html.Div([
                    html.Div(html.H3('', 
                    className='container top left left')),
                    html.Div([
                        html.H4('IP PLC:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='ip-plc',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TURNO:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='turno',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('PRODUCTO:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='producto',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTÁNDAR:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='t-estandar',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TAKT TIME:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='takt-time',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTIMADO:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='t-estimado',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('CANTIDAD:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='cantidad',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                    style={'margin-top': '10px'}, 
                    className='container top left right')
                ],
                className='container top left'), 
            className="card"),
            html.Div( 
                html.Div([
                        html.H4('IP PLC:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='ip-plc2',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TURNO:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='turno2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('PRODUCTO:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='producto2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTÁNDAR:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='t-estandar2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TAKT TIME:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='takt-time2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTIMADO:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='t-estimado2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('CANTIDAD:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='cantidad2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container top right'), 
            className="card")],
        className="container top"),

        #Second row
        html.Div( [
            html.Div(
                html.Div([
                        html.H4('OK:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='ip-plc22',type='text',placeholder='',style={'padding-bottom': '10%', 'padding-top': '10%', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('NOK:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='turno22',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '10%', 'padding-top': '10%'})], 
                className='container middle left'),
            className="card"),
            html.Div(
                html.Div([
                        html.H4('OEE_D:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='ip-plc223',type='text',placeholder='',style={'padding-bottom': '5%', 'padding-top': '5%', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('OEE_R:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='turno232',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '5%', 'padding-top': '5%'}),
                        html.H4('OEE_C:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='turno223',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '5%', 'padding-top': '5%'})], 
                className='container middle middle'),
            className="card"),
            html.Div(
                html.Div([
                        html.H4('OEE:', style={ 'margin-right': '20px'}),
                        dcc.Input(className='input', id='turno2243',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '20%', 'padding-top': '20%'})], 
                className='container middle right'),
            className="card")
        ], className="container middle"),

        #Third row
        html.Div( [
            html.Div(
                html.Div([
                    html.H4('IP PLC:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='ip-plc7',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('TURNO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='turno7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('PRODUCTO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='producto7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('T. ESTÁNDAR:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='t-estandar7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('TAKT TIME:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='takt-time7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('T. ESTIMADO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='t-estimado7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('CANTIDAD:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='cantidad7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container bottom left left'),
            className="card"),
            html.Div(
                html.Div([
                    html.H4('IP PLC:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='ip-plc5',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('TURNO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='turno5',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('PRODUCTO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='producto5',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('T. ESTÁNDAR:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='t-estandar5',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('TAKT TIME:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='takt-time5',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('T. ESTIMADO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='t-estimado5',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container bottom left middle'),
            className="card"),
            html.Div(
                html.Div([
                    html.H4('IP PLC:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='ip-plc56',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('TURNO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='turno56',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H4('PRODUCTO:', style={ 'margin-right': '20px'}),
                    dcc.Input(className='input', id='producto56',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container bottom left right'),
            className="card")
        ], className="container bottom")],
    className="container")
])


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')

