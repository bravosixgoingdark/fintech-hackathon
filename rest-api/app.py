from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Here you would typically fetch the posts from your WordPress database
    # For simplicity, we're returning a static response
    return jsonify([
        {"id": 1, "title": "First post", "content": "Hello, World!"},
        {"id": 2, "title": "Second post", "content": "Another post"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)