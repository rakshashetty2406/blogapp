from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory list to store posts
posts_data = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        data = request.get_json()
        posts_data.append(data)
        return jsonify({"message": "Post added", "data": data})
    return jsonify(posts_data)

@app.route('/posts/<int:index>', methods=['DELETE'])
def delete_post(index):
    if 0 <= index < len(posts_data):
        removed = posts_data.pop(index)
        return jsonify({"message": "Deleted", "data": removed})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
