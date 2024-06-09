# This function takes the user's input for the savings goal, starting balance, saving time, annual interest rate, and payment frequency. Then, it calculates and returns the contribution needed per deposit period to reach the specified savings goal.
def calc_contribution_per_period(savings_goal, starting_balance, saving_time, annual_interest_rate, deposit_frequency):
    # Convert annual interest rate to decimal
    annual_interest_rate_decimal = annual_interest_rate / 100
    
    # Determine the number of deposits per year based on deposit frequency
    if deposit_frequency == "weekly":
        deposits_per_year = 52
    elif deposit_frequency == "monthly":
        deposits_per_year = 12
    elif deposit_frequency == "quarterly":
        deposits_per_year = 4
    elif deposit_frequency == "yearly":
        deposits_per_year = 1
    else:
        raise Exception("Invalid deposit frequency") 
    
    # Calculate total number of deposits
    total_deposits = saving_time * deposits_per_year
    
    # Calculate periodic interest rate
    periodic_interest_rate = annual_interest_rate_decimal / deposits_per_year
    
    # Calculate future value of the savings goal using compound interest formula
    future_value = savings_goal - starting_balance * (1 + periodic_interest_rate)**total_deposits
    
    # Calculate contribution needed per payment period
    contribution = future_value / (((1 + periodic_interest_rate) ** total_deposits - 1) / periodic_interest_rate)
    
    return contribution
