from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faqs.db'
db = SQLAlchemy(app)

# FAQ model
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    fruit_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "fruit_name": self.fruit_name
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Route to serve the HTML file from the root directory
@app.route('/')
def home():
    return send_from_directory('.', 'faq.html')

# Route to serve the CSS file
@app.route('/faq.css')
def serve_css():
    return send_from_directory('.', 'faq.css')

# Route to serve the image
@app.route('/orange.png')
def serve_image():
    return send_from_directory('.', 'orange.png')

# API Routes
@app.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = FAQ.query.all()
    return jsonify([faq.to_dict() for faq in faqs]), 200

@app.route('/faqs/<int:id>', methods=['GET'])
def get_faq(id):
    faq = FAQ.query.get_or_404(id)
    return jsonify(faq.to_dict()), 200

@app.route('/faqs', methods=['POST'])
def create_faq():
    data = request.get_json()
    if not all([data.get('question'), data.get('answer'), data.get('fruit_name')]):
        return jsonify({"error": "Invalid input"}), 400

    new_faq = FAQ(
        question=data['question'],
        answer=data['answer'],
        fruit_name=data['fruit_name']
    )
    db.session.add(new_faq)
    db.session.commit()
    return jsonify(new_faq.to_dict()), 201

@app.route('/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    faq = FAQ.query.get_or_404(id)
    data = request.get_json()
    
    faq.question = data.get('question', faq.question)
    faq.answer = data.get('answer', faq.answer)
    faq.fruit_name = data.get('fruit_name', faq.fruit_name)

    db.session.commit()
    return jsonify(faq.to_dict()), 200

@app.route('/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    faq = FAQ.query.get_or_404(id)
    db.session.delete(faq)
    db.session.commit()
    return jsonify({"message": "FAQ deleted"}), 200

# Error handling
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
