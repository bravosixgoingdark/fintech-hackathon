from flask import Flask, render_template, request, redirect, url_for
import json
import os
from calculations import calc_contribution_per_period
import math 
# add future value and present value

app = Flask(__name__)


expenses = []
budget = 0
balance = 0
contribution = 0
def save_to_json():
    global expenses, budget, balance, contribution  # Ensure these variables are accessible
    with open('data.json', 'w') as f:
        json.dump({"expenses": expenses, "budget": budget, "balance": balance, "contribution": contribution}, f)

def load_from_json():
    global expenses, budget, balance, contribution  # Ensure these variables are accessible
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
        with open('data.json', 'r') as f:
            data = json.load(f)
            expenses = data['expenses']
            budget = data['budget']
            balance = data['balance']
            contribution = data['contribution']
    else:
        contribution = 0
        expenses = []
        budget = 0
        balance = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global balance, budget, expenses, contribution
    contribution = None  # Initialize contribution variable
    if request.method == 'POST':
        if 'savings_goal' in request.form and 'starting_balance' in request.form:
            # Extract data from form
            savings_goal = float(request.form['savings_goal'])
            starting_balance = float(request.form['starting_balance'])
            saving_time = int(request.form['saving_time'])
            annual_interest_rate = float(request.form['bank'])
            deposit_frequency = request.form['deposit_frequency']
            
            # Calculate contribution
            contribution = calc_contribution_per_period(savings_goal, starting_balance, saving_time, annual_interest_rate, deposit_frequency)
        
        # Handle other POST requests like adding expenses or setting budget here

    balance = budget - sum(expense['amount'] for expense in expenses)
    return render_template('index.html', expenses=expenses, budget=budget, balance=balance, contribution=contribution)

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

@app.route('/calculate_contribution', methods=['POST'])
def calculate_contribution():
    global contribution
    savings_goal = float(request.form['savings_goal'])
    starting_balance = float(request.form['starting_balance'])
    saving_time = int(request.form['saving_time'])
    bank = request.form['bank']
    deposit_frequency = request.form['deposit_frequency']
    
    # Check if the "Other" option is selected for the bank and use the custom interest rate
    if bank == 'other':
        annual_interest_rate = float(request.form['custom_interest_rate'])
    else:
        annual_interest_rate = float(bank)
    
    contribution = math.ceil(float(calc_contribution_per_period(savings_goal, starting_balance, saving_time, annual_interest_rate, deposit_frequency)))
    save_to_json() 
    return redirect(url_for('index'))

@app.errorhandler(Exception)
def all_exception_handler(error):
   return 'Error', 500


if __name__ == '__main__':
    load_from_json()
    app.run(host='0.0.0.0', port='5000', debug=True)