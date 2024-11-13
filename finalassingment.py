from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory catalog storage (in a real-world scenario, this would be a database)
catalog = []

@app.route('/')
def welcome():
    return jsonify({"message": "Welcome to the Catalog API"}), 200

# GET /api/catalog - Retrieve all products
@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    return jsonify({"catalog": catalog}), 200

# POST /api/catalog - Add a new product
@app.route('/api/catalog', methods=['POST'])
def add_product():
    product = request.json
    if not product or 'name' not in product or 'price' not in product or 'category' not in product:
        return jsonify({"error": "Product must have a name, price, and category"}), 400
    catalog.append(product)
    return jsonify({"message": "Product added successfully", "product": product}), 201

# GET /api/reports/total - Get total value of all products in the catalog
@app.route('/api/reports/total', methods=['GET'])
def get_total_value():
    total_value = sum(item['price'] for item in catalog)
    return jsonify({"total_value": total_value}), 200

# GET /api/products/<category> - Retrieve products by category
@app.route('/api/products/<category>', methods=['GET'])
def get_products_by_category(category):
    products_in_category = [item for item in catalog if item['category'].lower() == category.lower()]
    return jsonify({"category": category, "products": products_in_category}), 200

if __name__ == '__main__':
    app.run(debug=True)
