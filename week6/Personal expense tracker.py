# initialize structures 
expense_records = []
category_totals = {}
unique_categories = set()

print("=== PERSONAL EXPENSE TRACKER ===")

# collect 5 expenses
for i in range(5):
    print(f"Expense {i+1}:")
    cat = input("Category: ")
    amt = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    
    # add to list 
    expense_records.append((cat, amt, date))
    
    # add to set and dictionary
    unique_categories.add(cat)
    current_total = category_totals.get(cat, 0)
    category_totals[cat] = current_total + amt

# calculate overall stats
amounts = []
for record in expense_records:
    amounts.append(record[1])

total_spent = sum(amounts)
avg_spent = total_spent / len(amounts)
highest_exp = max(amounts)
lowest_exp = min(amounts)

# print report
print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for cat, total in category_totals.items():
    print(f"{cat}: ${total:.2f}")

print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${total_spent:.2f}")
print(f"Average Expense: ${avg_spent:.2f}")
print(f"Highest Expense: ${highest_exp:.2f}")
print(f"Lowest Expense: ${lowest_exp:.2f}")