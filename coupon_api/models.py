# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coupon(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    discount_value = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)