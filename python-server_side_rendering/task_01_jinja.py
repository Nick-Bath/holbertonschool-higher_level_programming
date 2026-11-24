from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product_display')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template('product_display.html', error='Wrong source')
    elif source == 'json':
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)        
    elif source == 'csv':
        with open('products.csv', 'r', encoding='utf-8') as file:
            products = list(csv.DictReader(file))

    if product_id is not None:
        data = []
        for product in products:
            if str(product['id']) == product_id:
                data.append(product)
    else:
        data = products
                
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)