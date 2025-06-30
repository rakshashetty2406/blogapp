from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

posts = []

@app.route("/")
def serve_homepage():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def serve_css():
    return send_from_directory(".", "style.css")

@app.route("/script.js")
def serve_js():
    return send_from_directory(".", "script.js")

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

@app.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()
    posts.append(data)
    return jsonify({"message": "Post added"}), 201

@app.route("/posts/<int:index>", methods=["DELETE"])
def delete_post(index):
    if 0 <= index < len(posts):
        posts.pop(index)
        return jsonify({"message": "Post deleted"})
    else:
        return jsonify({"error": "Invalid index"}), 400

if __name__ == "__main__":
    app.run(debug=True)
