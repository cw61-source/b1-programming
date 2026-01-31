# create the sample file
with open("products.txt", "w") as f:
    f.write("Laptop Computer, 999.99, Electronics, Premium\n")
    f.write("Winter Jacket, 129.99, Clothing, Standard\n")
    f.write("Python Programming Book, 49.99, Books, Standard\n")
    f.write("Coffee Maker, 79.99, Home, Budget\n")
    f.write("Wireless Headphones, 199.99, Electronics, Premium\n")
    # test exception handling
    f.write("Broken Item, FiveDollars, Home, Standard\n")