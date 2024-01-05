# Step a: Define and initialize variables with given values
principal_amount = 5000
annual_interest_rate = 4.5  # In percentage, needs to be converted to decimal
compounding_periods = 12
time_years = 40

# Step b: Calculate the periodic interest rate (r/n)
annual_interest_rate_decimal = annual_interest_rate / 100  # Convert to decimal
periodic_interest_rate = annual_interest_rate_decimal / compounding_periods

# Step c: Calculate the total number of interest periods (nt)
total_interest_periods = compounding_periods * time_years

# Step d: Calculate the accrued amount (A) using the formula
accrued_amount = principal_amount * (1 + periodic_interest_rate) ** total_interest_periods

# Step e: Print input values with appropriate labels
print("Principal amount: $" + str(principal_amount))
print("Annual nominal interest rate: " + str(annual_interest_rate) + "%")
print("Compounding periods per year: " + str(compounding_periods))
print("Time in years: " + str(time_years))

# Step f: Print the final result with an appropriate label, rounded to two decimal places
print("Accrued amount after", time_years, "years: $" + "{:.2f}".format(accrued_amount))
