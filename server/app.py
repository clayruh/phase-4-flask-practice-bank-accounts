#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Bank, Customer, Account

from models import db # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

@app.get('/customers')
def get_customers():
    customers = Customer.query.all()
    response = [customer.to_dict(rules=('-accounts',)) for customer in customers]
    return jsonify(response), 200

@app.get('/customers/<int:id>')
def get_customer_by_id(id):
    try: 
        customer = Customer.query.filter(Customer.id == id).first()
        return jsonify(customer.to_dict()), 200
    except:
        return jsonify({"error": "customer doesn't exist"}), 400
    
@app.delete('/customers/<int:id>')
def delete_customer(id):
    try: 
        customer = Customer.query.filter(Customer.id == id).first()
        for account in customer.account:
            db.session.delete(account)
        db.session.delete(customer)
        db.session.commit()
        return {}, 204
    except:
        return {"error": "customer doesn't exist"}, 400

@app.get('/banks')
def get_banks():
    banks = Bank.query.all()
    response = [bank.to_dict() for bank in banks]
    return jsonify(response), 200

@app.get('/banks/<int:id>')
def get_banks_by_id(id):
    bank = Bank.query.filter(Bank.id == id).first()
    return jsonify(bank.to_dict()), 200

@app.post('/account')
def create_account():
    try: 
        data = request.json
        customer = Customer.query.filter(Customer.id == data['customer_id']).first()
        bank = Bank.query.filter(Bank.id == data['bank_id']).first()

        new_account = Account(balance=data['balance'], account_type=data['account_type'], customer=customer, bank=bank)
        db.session.add(new_account)
        db.session.commit()
        return jsonify(new_account.to_dict()), 201
    except:
        return jsonify({"error": "invalid data"}), 300

if __name__ == '__main__':
    app.run(port=5555, debug=True)
