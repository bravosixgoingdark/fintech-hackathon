from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for the application
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
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense = {
        'title': request.form['expense_title'],
        'amount': int(request.form['expense_amount'])
    }
    expenses.append(expense)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)