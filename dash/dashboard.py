import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = [dbc.themes.BOOTSTRAP, 'dash/style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])

def card(title, content):
    return dbc.Col([
        dbc.Card([
            html.H4(title, className="dash-title"),
            *content
        ], className="dash-card")
    ], className="col-md-6 col-12")

content_placeholder = html.Div(style={"height": 200})

app.layout = dbc.Container([
    html.H2("Population effects"),
    html.P("Intro goes here"),
    dbc.Row([
        card("Select a plan:", [content_placeholder]),
        card("Poverty", [content_placeholder]),
        card("Inequality", [content_placeholder]),
        card("Decile changes", [content_placeholder])
    ]),
    html.H2("Family effects"),
    html.P("Intro goes here"),
    dbc.Row([
        card("About you", [content_placeholder]),
        card("Your possible outcomes", [content_placeholder]),
        card("Broken down by tax-benefits", [content_placeholder]),
        card("In relation to everyone else", [content_placeholder])
    ])
    
])

if __name__ == '__main__':
    app.run_server(debug=True)