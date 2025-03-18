import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

datafile = 'FoodAccessResearchAtlas.csv'  # Hardcoded dataset file name
datafile_1 = 'FoodAccessResearchAtlas_1.csv'  # Hardcoded dataset file name
def generate_plot(state_name):
    df = pd.read_csv(datafile)  # Load dataset
    
    if 'State' in df.columns:
        state_counts = df['State'].value_counts()
        if state_name in state_counts:
            fig = px.bar(state_counts, x=state_counts.index, y=state_counts.values, title=f'Distribution of State: {state_name}')
            fig.update_layout(xaxis_title='States', yaxis_title='Count')
            
            # Ensure the 'static' directory exists
            if not os.path.exists('static'):
                os.makedirs('static')
            
            plot_path = 'static/plot.html'
            fig.write_html(plot_path)  # Save plot as HTML
            return plot_path
    return None

def generate_table(columns=None):
    df = pd.read_csv(datafile_1)  # Load dataset
    top_10_df = df.head(10)  # Get top 10 rows

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(top_10_df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[top_10_df.CensusTract, top_10_df.State, top_10_df.County, top_10_df.Urban, top_10_df.Pop2010, top_10_df.OHU2010], # Error: 'DataFrame' object has no attribute 'col1'
                   fill_color='lavender',
                   align='left'))
       # cells=dict(values=[top_10_df[col].tolist() for col in top_10_df.columns],
                   #fill_color='lavender',
                  # align='left'))
    ])
    # Ensure the 'static' directory exists
    if not os.path.exists('static'):
        os.makedirs('static')

    table_path = 'static/table.html'
    fig.write_html(table_path)  # Save table as HTML
    return table_path