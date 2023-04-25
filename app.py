from flask import Flask, render_template, jsonify

app = Flask(__name__ , template_folder='src/view')

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/data')
def get_data():
    data = [
        {'name': 'Item 1', 'value': 10},
        {'name': 'Item 2', 'value': 20},
        {'name': 'Item 3', 'value': 30},
        {'name': 'Item 4', 'value': 40},
        {'name': 'Item 5', 'value': 50},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)