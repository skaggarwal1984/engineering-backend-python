from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all origins and methods
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Sample data
articles = [
    { "title": "Article 1", "description": "Brief description of Article 1", "link": "/articles/article-1", "image": "https://via.placeholder.com/150" },
    { "title": "Article 2", "description": "Brief description of Article 2", "link": "/articles/article-2", "image": "https://via.placeholder.com/150" },
    { "title": "Article 3", "description": "Brief description of Article 3", "link": "/articles/article-3", "image": "https://via.placeholder.com/150" },
]

@app.route('/api/articles', methods=['GET'])
def get_articles():
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
