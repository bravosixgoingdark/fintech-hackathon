from flask import Flask, render_template, request, redirect, url_for
import json
import os
# add future value and present value

app = Flask(__name__)

# Dummy data for the application
expenses = []
budget = 0
balance = 0

def save_to_json():
    with open('data.json', 'w') as f:
        json.dump({expenses: expenses, budget: budget, balance: balance}, f)

def load_from_json():
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
        with open('data.json', 'r') as f:
            data = json.load(f)
            expenses = data['expenses']
            budget = data['budget']
            balance = data['balance']
    else:
        expenses = []
        budget = 0
        balance = 0

@app.route('/')
def index():
    global balance
    balance = budget - sum(expense['amount'] for expense in expenses)
    return render_template('index.html', expenses=expenses, budget=budget, balance=balance)

@app.route('/set_budget', methods=['POST'])
def set_budget():
    global budget
    budget = int(request.form['budget'])
    save_to_json()
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense = {
        'title': request.form['expense_title'],
        'amount': int(request.form['expense_amount'])
    }
    expenses.append(expense)
    save_to_json()
    return redirect(url_for('index'))

if __name__ == '__main__':
    load_from_json()
    app.run(host='0.0.0.0', port='5000', debug=True)