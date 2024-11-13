from flask import Flask, request
import jsonify

app = Flask(__name__)

# Sample data for the product catalog
products = [
    {"id": 1, "name": "Jordans", "price": 350.99},
    {"id": 2, "name": "Nikes", "price": 150.99},
    {"id": 3, "name": "Versace", "price": 999.99}
]

# Root endpoint - Welcome page
@app.route('/')
def welcome():
    return "<h1>Welcome to the Product Catalog API</h1>"

# About page endpoint
@app.route('/about')
def about():
    return "<h1>About This API</h1><p>This API provides information about products.</p>"

# GET endpoint for product list
@app.route('/api/product', methods=['GET'])
def get_products():
    return jsonify(products)

# GET endpoint for product count
@app.route('/api/product/count', methods=['GET'])
def get_product_count():
    return jsonify({"product_count": len(products)})

if __name__ == '__main__':
    app.run(debug=True)