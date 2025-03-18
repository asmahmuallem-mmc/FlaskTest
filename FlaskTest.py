from flask import Flask, request, render_template
import plotly.io as pio
from plot_utils import generate_plot, generate_table

# Set the default renderer to suppress the deprecation warning
pio.renderers.default = 'notebook'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        state_name = request.form['state']
        image_url = generate_plot(state_name)
        table_url = generate_table()
        return render_template('index.html', state=state_name, image_url=image_url, table_url=table_url)

    return render_template('index.html', state=None)

if __name__ == '__main__':
    app.run(debug=True)