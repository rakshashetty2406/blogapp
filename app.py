from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# In-memory storage
posts = []

# Serve homepage
@app.route("/")
def serve_homepage():
    return send_from_directory(".", "index.html")

# Serve CSS
@app.route("/style.css")
def serve_css():
    return send_from_directory(".", "style.css")

# Serve JS
@app.route("/script.js")
def serve_js():
    return send_from_directory(".", "script.js")

# API to get all posts or add a new post
@app.route("/posts", methods=["GET", "POST"])
def handle_posts():
    if request.method == "POST":
        data = request.get_json()
        posts.append(data)
        return jsonify({"message": "Post added", "data": data}), 201
    return jsonify(posts)

# Delete a post by index
@app.route("/posts/<int:index>", methods=["DELETE"])
def delete_post(index):
    if 0 <= index < len(posts):
        removed = posts.pop(index)
        return jsonify({"message": "Deleted", "data": removed})
    return jsonify({"error": "Invalid index"}), 400

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
