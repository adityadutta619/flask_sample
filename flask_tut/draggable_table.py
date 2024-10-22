from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    {"id": 4, "name": "Item 4"},
]

@app.route('/')
def index():
    return render_template('draggable_table.html', data=data)

@app.route('/update_order', methods=['POST'])
def update_order():
    new_order = request.json['order']
    print("New Order:", new_order)  # Log the new order (you can process it as needed)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
