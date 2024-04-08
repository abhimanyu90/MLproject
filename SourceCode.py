import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

# Load your data
df = pd.read_excel('partialxyx.xlsx', sheet_name='Sheet1')

# Data processing logic
l = []  # List to store datetime values
totaltime = 0
i = 0
time1=0;

for index, row in df.iterrows():
    mydict = {"vibration": row['vibration_of_hydraulic_unit_oil_pump_22m2'], "oil": row['oil_delivery_pump_tp_y_pockets_40m4_current__b'], "time": row['entrytime']}
    time1 = mydict['time']
    
    l.append(time1)

    if i == 0:
        time1 = mydict['time']
        i += 1
    else:
        if float(mydict['vibration']) > 0.426794  and float(mydict['oil']) > 6.511502:
            a = (l[i] - l[i - 1])
            totaltime = totaltime + a
            i += 1

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout for Dash app
app.layout = html.Div([
    html.H1("Data Visualization"),
    dcc.Dropdown(
        id='row-dropdown',
        options=[
            {'label': f'Row {i}', 'value': i}
            for i in range(1, len(df) + 1)
        ],
        value=1
    ),
    dcc.Dropdown(
        id='chart-type',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Scatter Plot', 'value': 'scatter'}
        ],
        value='bar',
        clearable=False
    ),
    dcc.Graph(id='chart'),
    html.Button('Calculate Mean', id='calculate-button', n_clicks=0),
    html.Pre(id='mean-values')
])

# Define callbacks to update components in the layout based on user interactions
@app.callback(
    [Output('chart', 'figure'),
     Output('mean-values', 'children')],
    [Input('row-dropdown', 'value'),
     Input('chart-type', 'value'),
     Input('calculate-button', 'n_clicks')]
)
def update_chart(selected_row, chart_type, n_clicks):
    try:
        custom_scale_min = 0
        custom_scale_max = 500
    
        row_data = df.iloc[selected_row - 1]

        if chart_type == 'bar':
            fig = px.bar(row_data, x=row_data.index, y=row_data.values, title=f'Bar Chart for Row {selected_row}')
        elif chart_type == 'scatter':
            fig = px.scatter(row_data, x=row_data.index, y=row_data.values, title=f'Scatter Plot for Row {selected_row}')
        
        fig.update_yaxes(range=[custom_scale_min, custom_scale_max])
        
        if n_clicks > 0:
            column_means = df.mean()
            mean_values_text = "Mean Values:\n" + "\n".join(f"{col}: {mean:.2f}" for col, mean in column_means.items())
        else:
            mean_values_text = ""
        
        return fig, mean_values_text
    except Exception as e:
        return {
            'data': [],
            'layout': {
                'title': f'Error: {str(e)}'
            }
        }, ""

root = tk.Tk()
root.title('Machine')
root.geometry("400x400")

def run_dash_app():
    app.run_server(debug=False, host='localhost', port=8050)

def time():
    f1="Total machine running time:"+str(totaltime)+" seconds"
    mylabel=Label(root,text=f1).pack()

def mean1():
    m = df["vibration_of_hydraulic_unit_oil_pump_22m2"].mean()
    mylabel1 = Label(root, text=m).pack()

def mean2():
    m1 = df["oil_delivery_pump_tp_y_pockets_40m4_current__b"].mean()
    mylabel2 = Label(root, text=m1).pack()

def median1():
    m2 = df["vibration_of_hydraulic_unit_oil_pump_22m2"].median()
    mylabel3 = Label(root, text=m2).pack()

def median2():
    m3 = df['oil_delivery_pump_tp_y_pockets_40m4_current__b'].median()
    mylabel4 = Label(root, text=m3).pack()

def linear_regression():
    X = df['vibration_of_hydraulic_unit_oil_pump_22m2'].values.reshape(-1, 1)
    y = df['oil_delivery_pump_tp_y_pockets_40m4_current__b'].values
    
    model = LinearRegression()
    model.fit(X, y)
    slope = model.coef_[0]
    intercept = model.intercept_
    
    equation_text = f"Linear Regression Equation: y = {slope:.2f}x + {intercept:.2f}"
    mylabel5 = Label(root, text=equation_text).pack()

clicked = StringVar()
drop = OptionMenu(root, clicked, "vibration_of_hydraulic_unit_oil_pump_22m2", "oil_delivery_pump_tp_y_pockets_40m4_current__b", "time")
drop.pack()
button = tk.Button(root, text="Run Dash App", command=run_dash_app)
button.pack()
myButton1 = Button(root, text="Show time", command=time).pack()
myButton2 = Button(root, text="show mean of vibration", command=mean1).pack()
myButton3 = Button(root, text="show mean of oil", command=mean2).pack()
myButton4 = Button(root, text="show median of vibration", command=median1).pack()
myButton5 = Button(root, text="show median of oil", command=median2).pack()
myButton6 = Button(root, text="Linear Regression", command=linear_regression).pack()

root.mainloop()
