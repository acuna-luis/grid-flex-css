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
            html.Div([
                html.Span('Herramientas'),
                html.Div([html.P('Rechazo'), html.P('My Web')], className='dropdown-content', id='dropdown-content-herramientas'),
                ], 
            className="dropdown"),
            html.Div([
                html.Span('Config'),
                html.Div([html.P('conf1'), html.P('conf2')], className='dropdown-content', id='dropdown-content-config'),
                ], 
            className="dropdown"),
            html.Div([
                html.Span('Ayuda'),
                html.Div([html.P('ayuda1'), html.P('ayuda2')], className='dropdown-content', id='dropdown-content-ayuda'),
                ], 
            className="dropdown"),
        ], className='menu'),
        html.Div([
            html.Div(['a'], style={
                    'background-image': 'url("/assets/img/fcgui_logo.png")',
                    'background-repeat': 'no-repeat',
                    'margin-top': '5px',
                    'min-height': '90px'}),
            html.Div([
                html.H4('IP PLC:', style={'padding': '5px 0px 0px 0px'}),
                dcc.Input(className='input', id='ip-plc',type='text',placeholder='',style={'padding': '0px 0px 0px 0px', 'background-color': 'green', 'width': '50%'}, value='{}'.format('MODO DEMO'), readOnly=True),],
            style={ 'height': '50%', 
                    'align': 'right',
                    'text-align': 'right',
                    'display': 'grid',
                    'grid-template-columns': '1fr 1fr',
                    'padding': '2.5% 0px 0px 0px',
            })
        ], className='hbottom', ),
    ]),
   
    html.Div([
        #First row
        html.Div([
            html.Div( 
                html.Div([
                    html.Div(html.H3('', 
                    className='container top left left')),
                    html.Div([
                        html.H4('PRODUCTO:'),
                        dcc.Input(className='input', id='producto',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTÁNDAR:'),
                        dcc.Input(className='input', id='t-estandar',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('TAKT TIME:'),
                        dcc.Input(className='input', id='takt-time',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('T. ESTIMADO:'),
                        dcc.Input(className='input', id='t-estimado',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('CANTIDAD:'),
                        dcc.Input(className='input', id='cantidad',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('ORDEN:'),
                        dcc.Input(className='input', id='orden',type='text',placeholder='', value='{}'.format(''), style={'background-color': 'white'}),
                        html.P(''),
                        html.Div([
                            html.Button('INICIAR PRODUCCIÓN', id='iniciar-parar-produccion', n_clicks=0, style={'background-color': 'green', 'color': 'white', 'width': '150px', 'margin': '10px 0px 0px 0px'}),
                        ], style={'align': 'right'}),
                    ],    
                    #style={'margin': '0px 0px 0px 0px'},
                    className='container top left right')
                ],
                className='container top left'), 
            className="card"),
            html.Div(
                html.Div([
                    html.Div([
                        html.H4('ESTADO PRODUCCIÓN:',style={'padding':'5%'}),
                        dcc.Input(id='estado',type='text',placeholder='',style={'background-color': 'orange','textAlign': 'center', 'padding':'5%', 'border-radius': '10px'}, value='{}'.format('EN PREPARACIÓN'), readOnly=True),
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
                        html.Button('Modificar', id='modificar', n_clicks=0, style={'background-color': '#2d5f7c', 'color': 'white'}),
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
                        dcc.Input(className='input', id='ok',type='text',placeholder='',style={'padding-bottom': '10%', 'padding-top': '10%', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('NOK:'),
                        dcc.Input(className='input', id='nok',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '10%', 'padding-top': '10%', 'background-color': 'red'})], 
                className='container middle left'),
            className="card"),
            html.Div(
                html.Div([
                        html.H4('OEE_D:'),
                        dcc.Input(className='input', id='oee-d',type='text',placeholder='',style={'padding-bottom': '5%', 'padding-top': '5%', 'background-color': 'green'}, value='{}'.format('MODO DEMO'), readOnly=True),
                        html.H4('OEE_R:'),
                        dcc.Input(className='input', id='oee-r',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '5%', 'padding-top': '5%', 'background-color': 'green'}),
                        html.H4('OEE_C:'),
                        dcc.Input(className='input', id='oee-c',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '5%', 'padding-top': '5%', 'background-color': 'red'})], 
                className='container middle middle1'),
            className="card"),
            html.Div(
                html.Div([
                        html.H4('OEE:', style={'margin-top': '20%', 'margin-right': '20%'}),
                        dcc.Input(className='input', id='oee',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True, style={ 'padding-bottom': '25%', 'padding-top': '25%', 'background-color': 'green'})], 
                className='container middle right'),
            className="card")
        ], className="container middle"),

        #Third row
        html.Div( [
            html.Div(
                html.Div([
                    html.H5('NOMBRE:'),
                    dcc.Input(className='input', id='nombre',type='text',placeholder='',style={'display':'inline-block'}, value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('ID:'),
                    dcc.Input(className='input', id='id',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TURNO/INICIO:'),
                    html.Div([
                        dcc.Input(className='input', id='turno',type='text',placeholder='', value='{}'.format('TURNO DEMO'), readOnly=True),
                        dcc.Input(className='input', id='inicio2',type='text',placeholder='', value='{}'.format('INICIO DEMO'), readOnly=True),
                    ],style={'display': 'grid', 'grid-template-columns': '1fr 3fr', 'grid-gap': '10px'}),
                    html.H5('TIEMPO PRODUCCIÓN:'),
                    dcc.Input(className='input', id='t-produccion',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO DE PREPARACIÓN:'),
                    dcc.Input(className='input', id='t-preparacion',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO DE MICRO-PARADAS:'),
                    dcc.Input(className='input', id='t-microparadas',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True),
                    html.H5('TIEMPO PARADAS:'),
                    dcc.Input(className='input', id='t-paradas',type='text',placeholder='', value='{}'.format('MODO DEMO'), readOnly=True)],
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

