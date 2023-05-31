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
                                {"label": "Total", "value":"Total"},
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
    Input("Type-dropdown", "value"),
    Input("Stat-dropdown", "value")
)



def update_figure(Type, Stat):
    
    filtered_dataset = df[(df["Type 1"] == Type)]
    
    if(Type):
        c=p[Type]

    if(Stat or Stat!="Total"):
        fig = px.histogram(filtered_dataset, x=Stat, color_discrete_sequence = [c], range_x = [0, 300])
    else:
        fig = px.histogram(filtered_dataset, x="Total", color_discrete_sequence = [c],  range_x = [0, 900])
   
    fig.update_layout(
        
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)