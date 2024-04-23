

This project provides an interactive dashboard and various data analysis functionalities for exploring and understanding data related to machine health. It leverages the power of Dash for interactive visualizations and Scikit-learn for machine learning tasks.

Key Features:

Interactive Dash App:
Visualize data from an Excel file using bar charts or scatter plots.
Select specific rows for focused analysis.
Data Analysis:
Calculate mean and median values for selected columns.
Perform multi-linear regression to understand relationships between features and a target variable.
Display predicted values based on new data.
Requirements:

Python 3.x
pandas
dash
dash-core-components (dcc)
dash-html-components (html)
plotly.express (px)
tkinter
numpy
scikit-learn
Installation:

Ensure you have Python 3 and the required libraries installed. You can install them using pip install pandas dash dash-core-components dash-html-components plotly.express tkinter numpy scikit-learn.
Clone or download this repository.
Running the App:

Navigate to the project directory in your terminal.
Run the Python script using python app.py.
A web browser window will open automatically, displaying the interactive Dash app.
Using the App:

Use the dropdown menu to select a row from the dataset.
Choose between bar charts and scatter plots to visualize selected data.
Click the "Calculate Mean" button to view the mean values of each column in the dataset.
Click the relevant buttons to display various data analysis results.
Multi-Linear Regression Example:

The code performs multi-linear regression on several features (axes_hydrostatic_tank_level, vibration_of_hydraulic_unit_oil_pump_22m2, and oil_delivery_pump_tp_y_pockets_40m4_current__b) to predict the table_hydrostatic_tank_level.
The coefficients, intercept, and predicted values for example new data points are displayed.
