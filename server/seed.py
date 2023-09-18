#!/usr/bin/env python3

from app import app
from models import db, Bank, Customer, Account
from faker import Faker
import random

faker = Faker()

def create_customers():
    customers = []
    for _ in range(100):
        c = Customer(
            first_name=faker.first_name(),
            last_name=faker.last_name()
        )
        customers.append(c)
    return customers

def create_banks():
    banks = []
    for _ in range(10):
        b = Bank(
            name=faker.company()
        )
        banks.append(b)
    return banks

def create_accounts():
    accounts = []
    account_types = ["checking", "savings", "retirement", "cd", "brokerage"]
    for _ in range(1000):
        a = Account(
            balance = random.randint(0, 1000000),
            account_type = random.choice(account_types),
            bank = random.choice(banks),
            customer = random.choice(customers)
        )
        accounts.append(a)
    return accounts

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Account.query.delete()
        Bank.query.delete()
        Customer.query.delete()

        print("Seeding database...")
        customers = create_customers()
        db.session.add_all(customers)
        db.session.commit()

        banks = create_banks()
        db.session.add_all(banks)
        db.session.commit()

        accounts = create_accounts()
        db.session.add_all(accounts)
        db.session.commit()

        print("Seeding complete!")
