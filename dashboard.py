import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import plotly.graph_objects as go
from dash import Input, Output



c = "#070D0D" 
app = dash.Dash()

df = pd.read_csv(
    "Pokemon.csv"
)

p = {'Grass':'#056608', 'Fire':'#f73718', 'Water':'#00008B', 'Bug':'#90EE90', 'Normal':'#F0EAD6',
    'Poison':'#b70df2', 'Electric':'#FFFF33', 'Ground':'#C4A484', 'Fairy':'#ffb6c1', 'Fighting': '#964B00', 'Psychic': '#3a243b',
    'Rock': '#5C4033', 'Ghost':'#452D2E', 'Ice':'#368BC1', 'Dragon': '#FFD580', 'Dark':'#070D0D', 'Steel': '#AAA9AD', 'Flying':'#87CEEB'}



colors = {"background": "#011833", "text": "#7FDBFF"}


app.layout = html.Div(
    [
        html.H1(
            "Gotta graph em all",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("Pokemon Type"),
                        dcc.Dropdown(
                            id="Type-dropdown",
                            options=[
                                {"label": s, "value": s} for s in df["Type 1"].unique()
                            ],
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("Pokemon Stat"),
                        dcc.Dropdown(
                            id="Stat-dropdown",
                            options=[
                                {"label": "HP", "value": "HP"},
                                {"label": "Attack", "value": "Attack"},
                                {"label": "Defense", "value": "Defense"},
                                {"label": "Sp. Atk", "value": "Sp. Atk"},
                                {"label": "Sp. Def", "value": "Sp. Def"},
                                {"label": "Speed", "value": "Speed"}
                                
                            ],
                            className="dropdown",
                        ),
                    ]


                    
                )
            ]
        ),
        html.Div(dcc.Graph(id="Type-vs-Stat"), className="chart"),
        
    ],
    className="container",

    
)


@app.callback(
    Output("Type-vs-Stat", "figure"),
    Input("Type-dropdown", "value")
)



def update_figure(Type):
    
    filtered_dataset = df[(df["Type 1"] == Type)]
    
    print(Type)
    if(Type):
        c=p[Type]
    fig = px.histogram(filtered_dataset, x="Total", color_discrete_sequence = [c])
   
    fig.update_layout(
        
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


'''fig = go.Figure()

types = ['Grass', 'Fire', 'Water', 'Bug', 'Normal',
    'Poison', 'Electric', 'Ground', 'Fairy', 'Fighting', 'Psychic',
    'Rock', 'Ghost', 'Ice', 'Dragon', 'Dark', 'Steel', 'Flying']

for type in types:
    fig.add_trace(go.Violin(x=df['Type 1'][df['Type 1'] == type],
                            y=df['Total'][df['Type 1'] == type],
                            name=type,
                            box_visible=True,
                            meanline_visible=True,
                            line_color = p[type]))






#fig = px.violin(df, y="Total", x="Type 1", color=p, box=True, points="all",width=800, height=500)


app.layout = html.Div([dcc.Graph(id="Primary Type to stat total", figure=fig)])
'''

if __name__ == "__main__":
    app.run_server(debug=True)