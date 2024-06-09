import math

# Calculate how much money you need to contribute each payment period in order to arrive at a specific savings goal. It should have the user input their savings goal (amount of money), saving time (in years), interest rate (percent), and the frequency at which they make deposits (select either weekly, monthly, quarterly or yearly)        
def calculate_payment_amount(goal, years, interest_rate, deposit_frequency):
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100
    
    # Determine number of deposits per year
    if deposit_frequency.lower() == 'weekly':
        deposits_per_year = 52
    elif deposit_frequency.lower() == 'monthly':
        deposits_per_year = 12
    elif deposit_frequency.lower() == 'quarterly':
        deposits_per_year = 4
    elif deposit_frequency.lower() == 'yearly':
        deposits_per_year = 1
    else:
        print("Invalid deposit frequency. Please choose from weekly, monthly, quarterly, or yearly.")
        return None
    
    # Calculate number of periods
    total_periods = years * deposits_per_year
    
    # Calculate future value factor
    future_value_factor = (1 + interest_rate_decimal / deposits_per_year) ** total_periods
    
    # Calculate payment amount
    payment_amount = goal * (interest_rate_decimal / deposits_per_year) / (future_value_factor - 1)
    
    return payment_amount
    

