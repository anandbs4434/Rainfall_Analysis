from flask import Flask, render_template
import pandas as pd
import  plotly.express as px
import numpy as np

app = Flask(__name__)

def load_data():
    df = pd.read_csv('dataset/data.csv')
    return df 

@app.route('/')
def index():
    return render_template('graph1.html')
    
@app.route('/graph/1')
def graph1():
    grouped_obj=  load_data()
    fig = px.area(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
  

    fig1 = px.bar(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig2 = px.scatter(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    return render_template('graph1.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)