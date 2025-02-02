import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Updated dataset with data for India
data = {
    "Year": [2020, 2003, 2000, 2023, 2008, 2015],
    "Country": ["China", "China", "China", "Italy", "France", "India"],
    "Air Quality Index (AQI)": [178, 441, 418, 44, 224, 162],
    "CO2 Emissions (Metric Tons)": [6.80, 3.91, 8.41, 5.63, 9.88, 2.48],
    "Renewable Energy (% of Total)": [93.29, 66.46, 26.64, 70.01, 90.46, 50.12],
    "Deforestation Rate (sq km/year)": [8858.34, 2092.38, 814.08, 4706.67, 6635.02, 1290.76],
    "Water Quality Index": [33, 100, 5, 14, 6, 45],
    "Waste Recycled (%)": [56.01, 37.73, 38.55, 47.45, 31.18, 12.37],
    "Average Temperature (°C)": [38.64, 25.00, 25.14, -6.21, -0.65, 30.25]
}
df = pd.DataFrame(data)
# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Interactive Dashboard"

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Environmental Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Bar Plot:"),
        dcc.Dropdown(
            id='bar-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[2],
            clearable=False
        ),
        dcc.Graph(id='bar-plot')
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    html.Div([
        html.Label("Line Plot:"),
        html.Label("Select X-axis Column:"),
        dcc.Dropdown(
            id='line-x-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[0],
            clearable=False
        ),
        html.Label("Select Y-axis Column:"),
        dcc.Dropdown(
            id='line-y-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[2],
            clearable=False
        ),
        dcc.Graph(id='line-plot')
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    html.Div([
        html.Label("Scatter Plot:"),
        html.Label("Select X-axis Column:"),
        dcc.Dropdown(
            id='scatter-x-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[0],
            clearable=False
        ),
        html.Label("Select Y-axis Column:"),
        dcc.Dropdown(
            id='scatter-y-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[2],
            clearable=False
        ),
        dcc.Graph(id='scatter-plot')
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    html.Div([
        html.Label("Pie Chart:"),
        dcc.Dropdown(
            id='pie-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[1],
            clearable=False
        ),
        dcc.Graph(id='pie-chart')
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
])

# Callbacks for updating plots
@app.callback(
    Output('bar-plot', 'figure'),
    Input('bar-column', 'value')
)
def update_bar_plot(column):
    if column:
        fig = px.bar(df, x=df.index, y=column, title=f"Bar Plot of {column}")
        return fig
    return {}

@app.callback(
    Output('line-plot', 'figure'),
    [Input('line-x-column', 'value'),
     Input('line-y-column', 'value')]
)
def update_line_plot(x_col, y_col):
    if x_col and y_col:
        fig = px.line(df, x=x_col, y=y_col, title=f"Line Plot of {y_col} vs {x_col}")
        return fig
    return {}

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-x-column', 'value'),
     Input('scatter-y-column', 'value')]
)
def update_scatter_plot(x_col, y_col):
    if x_col and y_col:
        fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot of {y_col} vs {x_col}")
        return fig
    return {}

@app.callback(
    Output('pie-chart', 'figure'),
    Input('pie-column', 'value')
)
def update_pie_chart(column):
    if column:
        fig = px.pie(df, names=column, title=f"Pie Chart of {column}")
        return fig
    return {}

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)