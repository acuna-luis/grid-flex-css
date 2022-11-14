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
                        html.H4('IP PLC:'),
                        dcc.Input(className='input', id='ip-plc',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TURNO:'),
                        dcc.Input(className='input', id='turno',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('PRODUCTO:'),
                        dcc.Input(className='input', id='producto',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTÁNDAR:'),
                        dcc.Input(className='input', id='t-estandar',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TAKT TIME:'),
                        dcc.Input(className='input', id='takt-time',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTIMADO:'),
                        dcc.Input(className='input', id='t-estimado',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('CANTIDAD:'),
                        dcc.Input(className='input', id='cantidad',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                    style={'margin-top': '10px'}, 
                    className='container top left right')
                ],
                className='container top left'), 
            className="card"),
            html.Div(
                html.Div([
                    html.Div([
                        html.H4('ESTADO PRODUCCIÓN:',style={'padding':'5%'}),
                        dcc.Input(id='estado',type='text',placeholder='',style={'background-color': 'orange','textAlign': 'center', 'padding':'5%'}, value='{}'.format('EN PREPARACIÓN'), readOnly=True),
                    ], className='container top right row1'
                    ),    
                    html.Div([
                        html.H4('PARADA:',style={'margin-right':20}),
                        dcc.Dropdown(['', '1', '2', '3'], '',style={'width':'50px','textAlign': 'center'}, id='parada-dropdown'),
                        dcc.Input(id='parada',type='text',placeholder='', value='{}'.format(''), readOnly=True),
                    ], className='container top right row2'
                    ), 
                    html.Div([
                        html.H4('INICIO/TOTAL:',style={'margin-right':20}),
                        dcc.Input(id='inicio',type='text',placeholder='', value='{}'.format(''), readOnly=True),
                        dcc.Input(id='total',type='text',placeholder='', value='{}'.format(''), readOnly=True),
                    ], className='container top right row3'
                    ), 
                    html.Div([
                        html.H4('CAUSAS:',style={'margin-right':20}),
                        dcc.Dropdown(['', 'CAUSA 1', 'CAUSA 2', 'CAUSA 3'], '', style={'textAlign': 'center'}, id='causa-dropdown'),
                    ], className='container top right row4'
                    ), 
                    html.Div([
                        html.Button('Modificar', id='modificar', n_clicks=0)
                    ], className='container top right row5'
                    )],
                className='container top right'), 
            className="card")],
        className="container top"),

        #Second row
        html.Div( [
            html.Div(
                html.Div([
                        html.H4('OK:'),
                        dcc.Input(className='input', id='ip-plc22',type='text',placeholder='',style={'padding-bottom': '10%', 'padding-top': '10%', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('NOK:'),
                        dcc.Input(className='input', id='turno22',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '10%', 'padding-top': '10%'})], 
                className='container middle left'),
            className="card"),
            html.Div(
                html.Div([
                        html.H4('OEE_D:'),
                        dcc.Input(className='input', id='ip-plc223',type='text',placeholder='',style={'padding-bottom': '5%', 'padding-top': '5%', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('OEE_R:'),
                        dcc.Input(className='input', id='turno232',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '5%', 'padding-top': '5%'}),
                        html.H4('OEE_C:'),
                        dcc.Input(className='input', id='turno223',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '5%', 'padding-top': '5%'})], 
                className='container middle middle1'),
            className="card"),
            html.Div(
                html.Div([
                        html.H4('OEE:', style={'margin-top': '20%', 'margin-right': '20%'}),
                        dcc.Input(className='input', id='turno2243',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '25%', 'padding-top': '25%'})], 
                className='container middle right'),
            className="card")
        ], className="container middle"),

        #Third row
        html.Div( [
            html.Div(
                html.Div([
                    html.H5('NOMBRE:'),
                    dcc.Input(className='input', id='ip-plc7',type='text',placeholder='',style={'display':'inline-block', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('ID:'),
                    dcc.Input(className='input', id='turno7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('INICIO:'),
                    dcc.Input(className='input', id='producto7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO PRODUCCIÓN:'),
                    dcc.Input(className='input', id='t-estandar7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO DE PREPARACIÓN:'),
                    dcc.Input(className='input', id='takt-time7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO DE MICRO-PARADAS:'),
                    dcc.Input(className='input', id='t-estimado7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO PARADAS:'),
                    dcc.Input(className='input', id='cantidad7',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container bottom left'),
            className="card"),
            html.Div(
                html.Div([
                    html.H5('T CICLO REAL:'),
                    dcc.Input(className='input', id='tcicloreal',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('T ÚLTIMA:'),
                    dcc.Input(className='input', id='tultima',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('T ESTACIÓN 1:'),
                    dcc.Input(className='input', id='t-estacion1',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('T ESTACIÓN 2:'),
                    dcc.Input(className='input', id='t-estacion2',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('T ESTACIÓN 3'),
                    dcc.Input(className='input', id='t-estacion3',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('T ESTACIÓN 4'),
                    dcc.Input(className='input', id='t-estacion4',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container bottom middle2'),
            className="card"),
            html.Div(
                html.Div([
                    html.H5('ESPERADA:'),
                    dcc.Input(className='input', id='esperada',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('PROYECTADA:'),
                    dcc.Input(className='input', id='proyectada',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('OBJETIVA:'),
                    dcc.Input(className='input', id='objetiva',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
                className='container bottom right'),
            className="card")
        ], className="container bottom")],
    className="container")
])


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')

