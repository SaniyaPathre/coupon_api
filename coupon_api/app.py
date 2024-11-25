# app.py
from flask import Flask, request, jsonify
from models import Coupon, db
from database import init_db  # Import the init_db function
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/generate_coupon', methods=['POST'])
def generate_coupon():
    data = request.json
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    product_id = data.get('product_id')
    user_id = data.get('user_id')
    discount_value = data.get('discount_value')

    if not product_id or not user_id or discount_value is None:
        return jsonify({'error': 'Missing required fields'}), 400

    coupon_id = str(uuid.uuid4())
    expiration_date = datetime.utcnow() + timedelta(days=1)

    new_coupon = Coupon(id=coupon_id, product_id=product_id, user_id=user_id,
                        discount_value=discount_value, expiration_date=expiration_date)

    db.session.add(new_coupon)
    db.session.commit()

    return jsonify({'coupon_id': coupon_id, 'expiration_date': expiration_date}), 201

@app.route('/validate_coupon', methods=['POST'])
def validate_coupon():
    data = request.json
    coupon_id = data.get('coupon_id')
    product_id = data.get('product_id')
    user_id = data.get('user_id')

    coupon = Coupon.query.filter_by(id=coupon_id, product_id=product_id, user_id=user_id).first()

    if not coupon:
        return jsonify({'error': 'Invalid coupon'}), 400

    if coupon.expiration_date < datetime.utcnow():
        return jsonify({'error': 'Coupon has expired'}), 400

    return jsonify({'valid': True, 'discount_value': coupon.discount_value}), 200

if __name__ == '__main__':
    app.run(debug=True)