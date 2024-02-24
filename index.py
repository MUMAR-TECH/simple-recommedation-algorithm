

# sample data
products = [
    {'name': 'Product A', 'rating': 4.5, 'price': 50, 'popularity': 100},
    {'name': 'Product B', 'rating': 3.8, 'price': 30, 'popularity': 80},
    {'name': 'Product C', 'rating': 1.5, 'price': 70, 'popularity': 12},
    {'name': 'Product D', 'rating': 3.5, 'price': 76, 'popularity': 10},
    {'name': 'Product E', 'rating': 3.6, 'price': 71, 'popularity': 20},
    {'name': 'Product F', 'rating': 2.2, 'price': 79, 'popularity': 120},
    {'name': 'Product T', 'rating': 4.5, 'price': 66, 'popularity': 110},
    {'name': 'Product J', 'rating': 4.0, 'price': 67, 'popularity': 40},
    {'name': 'Product K', 'rating': 4.6, 'price': 68, 'popularity': 50},
    {'name': 'Product L', 'rating': 4.1, 'price': 45, 'popularity': 70},
    {'name': 'Product Z', 'rating': 4.4, 'price': 65, 'popularity': 80},
    {'name': 'Product X', 'rating': 3.3, 'price': 35, 'popularity': 90},
    {'name': 'Product G', 'rating': 2.2, 'price': 12, 'popularity': 70},
    {'name': 'Product R', 'rating': 1.2, 'price': 22, 'popularity': 50},
    {'name': 'Product W', 'rating': 1.1, 'price': 34, 'popularity': 10},
    {'name': 'Product Q', 'rating': 0.6, 'price': 88, 'popularity': 55},
    {'name': 'Product U', 'rating': 4.1, 'price': 78, 'popularity': 111},
    {'name': 'Product H', 'rating': 5.0, 'price': 99, 'popularity': 100},
    {'name': 'Product S', 'rating': 0.9, 'price': 74, 'popularity': 45},
    {'name': 'Product V', 'rating': 1.0, 'price': 30, 'popularity': 113},
    {'name': 'Product JK', 'rating': 2.0, 'price': 100, 'popularity': 23},
    {'name': 'Product OP', 'rating': 3.0, 'price': 10, 'popularity': 44},
    {'name': 'Product CK', 'rating': 3.0, 'price': 90, 'popularity': 55},
    {'name': 'Product JJ', 'rating': 1.0, 'price': 60, 'popularity': 17},
    {'name': 'Product FY', 'rating': 1.5, 'price': 50, 'popularity': 10},
    {'name': 'Product ZW', 'rating': 4.0, 'price': 80, 'popularity': 119},

]

# Define weights
weights = {'rating': 0.4, 'price': 0.3, 'popularity': 0.3}

# Normalize data (assuming values are between 0 and 1 for simplicity)
def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

# Calclate Scores
for product in products:
    normalized_rating = normalize(product['rating'], 0,5)
    normalized_price = normalize(product['price'], 0, 100)
    normalized_popularity = normalize(product['popularity'], 0, 150)

    product['score'] = (weights['rating'] * normalized_rating) + (weights['price'] * normalized_price) + (weights['popularity'] * normalized_popularity)


# Rank products

ranked_products = sorted(products, key=lambda x: x['score'], reverse=True)

# Display rankings
for i, product in enumerate(ranked_products):
    print(f"{i + 1}, {product['name']} - Score: {product['score']}")