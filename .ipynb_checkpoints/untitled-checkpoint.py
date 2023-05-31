import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

app = dash.Dash()

df = pd.read_csv(
    "Pokemon.csv"
)

p = {'Grass':'#056608', 'Fire':'#f73718', 'Water':'#00008B', 'Bug':'#90EE90', 'Normal':'#F0EAD6',
    'Poison':'#b70df2', 'Electric':'#FFFF33', 'Ground':'#C4A484', 'Fairy':'#ffb6c1', 'Fighting': '#964B00', 'Psychic': '#3a243b',
    'Rock': '#5C4033', 'Ghost':'#452D2E', 'Ice':'#368BC1', 'Dragon': '#FFD580', 'Dark':'#070D0D', 'Steel': '#AAA9AD', 'Flying':'#87CEEB'}

fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)