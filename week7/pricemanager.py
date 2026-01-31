import os

def calculate_price():
    # Variables for the summary report
    total_products = 0
    total_discount_sum = 0
    
    print("Starting Product Pricing Manager...")

    try:
        # Open thhe input file for reading and output file for writing
        with open("products.txt", "r") as input_file, \
             open("pricing_report.txt", "w") as output_file:

            # Write the header
            output_file.write(f"{'Product Name':<25} {'Base Price':<12} {'Discount':<10} {'Final Price':<12}\n")
            output_file.write("-" * 60 + "\n")

            for line in input_file:
                # Strip whitespace and split by comma
                parts = line.strip().split(',')
                
                # Skip empty lines
                if len(parts) != 4:
                    continue

                # Clean up the data
                name = parts[0].strip()
                price_str = parts[1].strip()
                category = parts[2].strip()
                tier = parts[3].strip()

                try:
                    # Convert price to float
                    base_price = float(price_str)
                    
                    # 1. Calculate Category Discount 
                    cat_discount_percent = 0
                    if category == "Electronics":
                        cat_discount_percent = 0.10
                    elif category == "Clothing":
                        cat_discount_percent = 0.15
                    elif category == "Books":
                        cat_discount_percent = 0.05
                    elif category == "Home":
                        cat_discount_percent = 0.12
                    
                    # 2. Calculate Tier Discount
                    tier_discount_percent = 0
                    if tier == "Premium":
                        tier_discount_percent = 0.05
                    elif tier == "Standard":
                        tier_discount_percent = 0.00
                    elif tier == "Budget":
                        tier_discount_percent = 0.02

                    # 3. Calculate Final Math 
                    total_percent = cat_discount_percent + tier_discount_percent
                    discount_amount = base_price * total_percent
                    final_price = base_price - discount_amount

                    # Write to file formatted clearly 
                    output_file.write(f"{name:<25} ${base_price:<11.2f} {total_percent*100:<9.0f}% ${final_price:<11.2f}\n")

                    # Update statistics
                    total_products += 1
                    total_discount_sum += total_percent

                except ValueError:
                    # Handle invalid price formats
                    print(f"Error processing product '{name}': Invalid price format.")
                    continue

        # Console Summary
        avg_discount = 0
        if total_products > 0:
            avg_discount = (total_discount_sum / total_products) * 100
            
        print("\n--- Processing Complete ---")
        print(f"Total products processed: {total_products}")
        print(f"Average discount applied: {avg_discount:.2f}%")
        print("Report generated: pricing_report.txt")

    except FileNotFoundError:
        # Handle missing input file 
        print("Error: The file 'products.txt' was not found.")
    except PermissionError:
        # Handle write permission errors 
        print("Error: Could not write to 'pricing_report.txt'. Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    calculate_price()