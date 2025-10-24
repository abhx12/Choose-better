import heapq
from datastructures import Product, insert_avl, range_query_avl
from heap_sort import compute_rating_price_score

def greedy_range_query(products, min_price, max_price, max_results=10):
    # Filter products in price range using AVL tree
    root = None
    for product in products:
        if product.price != "N/A":
            root = insert_avl(root, product)

    if not root:
        return [], 0

    range_products = []
    range_query_avl(root, min_price, max_price, range_products)
    if not range_products:
        return [], 0

    # Compute scores
    scores = [compute_rating_price_score(p) for p in range_products]

    # Greedy selection 
    indexed_products = [(scores[i], i, range_products[i]) for i in range(len(range_products))]
    indexed_products.sort(reverse=True)  # Sort by score descending
    top_products = []
    for score, _, product in indexed_products[:min(max_results, len(range_products))]:
        product.score = score
        top_products.append(product)

    return top_products, len(range_products)

# RANGE QUERY HANDLER

def handle_range_query(products):
    try:
        min_price = input("Enter minimum price (₹): ").strip()
        max_price = input("Enter maximum price (₹): ").strip()
        min_price = float(min_price)
        max_price = float(max_price)
        if min_price < 0 or max_price < 0:
            print("Prices must be non-negative.")
            return [], None, None
        if min_price > max_price:
            print("Minimum price cannot exceed maximum price.")
            return [], None, None
        top_products, valid_count = greedy_range_query(products, min_price, max_price)
        return top_products, min_price, max_price

    except ValueError:
        print("Invalid input. Please enter numeric values for prices.")
        return [], None, None