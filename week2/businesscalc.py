''' calculator should calculate profit
and margin percentage ffrom revenue and cost data'''

# Get user input
revenue = float(input("Enter revenue: "))
costs = float(input("Enter costs: "))

# Calculate profit
profit = revenue - costs

# Calculate profit margin percentage

margin = (profit / revenue) * 100

# Display results to user 

print("\n... Revenue Calculation ...")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs: ${costs:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:,.1f}%")