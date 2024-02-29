
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form.get('name')
    email = request.form.get('email')
    coffee_type = request.form.get('coffee_type')
    quantity = request.form.get('quantity')

    # Validation logic goes here

    # Store order in database or send to fulfillment system

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
