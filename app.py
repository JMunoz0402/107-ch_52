from flask import Flask, request, jsonify
from config import db  # Assuming this sets up the MongoDB connection

app = Flask(__name__)

# Sample data for the product catalog
products = [
    {"id": 1, "name": "Jordans", "price": 350.99},
    {"id": 2, "name": "Nikes", "price": 150.99},
    {"id": 3, "name": "Versace", "price": 999.99}
]

# Root endpoint - Welcome page
@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to the Product Catalog API</h1>"

# About page endpoint
@app.route('/about', methods=['GET'])
def about():
    return "<h1>About This API</h1><p>This API provides information about products.</p>"

# POST endpoint to add a new product to the database
@app.route('/api/products', methods=['POST'])
def save_product():
    item = request.get_json()
    db.products.insert_one(item)  # Save the item to MongoDB
    return jsonify(fix_id(item)), 201

# GET endpoint for product count
@app.route('/api/product/count', methods=['GET'])
def get_product_count():
    product_count = db.products.count_documents({})  # Get count of documents in the products collection
    return jsonify({"product_count": product_count})

# #################################
products = []

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

if __name__ == '__main__':
    app.run(debug=True)
