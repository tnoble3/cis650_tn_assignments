sales_records = [
" laptop Pro 15 ",
"WIRELESS MOUSE",
"keyboard---mechanical",
" USB-C Hub ",
"monitor 27inch ",
" webcam HD",
"laptop pro 15",
"HEADPHONES--noise cancel"]

prices = [1299.99, 45.50, 89.00, 35.99, 349.00, 79.99, 1299.99,
159.00]

cleaned_products = []

for name in sales_records:
    cleaned = name.strip()
    cleaned = cleaned.replace("---", " ")
    cleaned = cleaned.replace("-", " ")
    
    words = cleaned.split()#getting rid of any extra whitespace
    cleaned = " ".join(words)
    
    cleaned = cleaned.title()
    cleaned_products.append(cleaned)
    
combined = []
for i in range(len(cleaned_products)):
    row = [cleaned_products[i], prices[i]]
    combined.append(row)
    
unique_products = []
existing_products = []

for row in combined:
    product_name = row[0]
    if product_name not in existing_products:
        unique_products.append(row)
        existing_products.append(product_name)

unique_products.sort()
print(" ")
print("Cleaned Sales Report")
print("---------------------")
for row in unique_products:
    product_name = row[0]
    price = row[1]
    print(product_name + " : $" + format(price, ".2f" ))