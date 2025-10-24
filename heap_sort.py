import heapq
import re
import math
from datastructures import Product
from utilities import parse_discount, parse_rating

def sort_by_discount(products, max_results=10):
    heap = []
    for i, product in enumerate(products):
        if product.price != "N/A":
            discount = parse_discount(product.discount)
            heapq.heappush(heap, (-discount, i, product))  # Max heap for discount
    top_products = []
    for _ in range(min(max_results, len(heap))):
        if heap:
            top_products.append(heapq.heappop(heap)[2])
    return top_products

def sort_by_price_asc(products, max_results=10):
    heap = []
    valid_count = 0
    for i, product in enumerate(products):
        if product.price != "N/A":
            heapq.heappush(heap, (product.price, i, product))  # Min heap for price
            valid_count += 1
    top_products = []
    for j in range(min(max_results, valid_count)):
        if heap:
            top_products.append(heapq.heappop(heap)[2])
    return top_products

def sort_by_price_desc(products, max_results=10):
    heap = []
    valid_count = 0
    for i, product in enumerate(products):
        if product.price != "N/A":
            heapq.heappush(heap, (-product.price, i, product))  # Max heap for price
            valid_count += 1
    top_products = []
    for j in range(min(max_results, valid_count)):
        if heap:
            top_products.append(heapq.heappop(heap)[2])
    return top_products

def sort_by_rating(products, max_results=10):
    heap = []
    for i, product in enumerate(products):
        if product.price != "N/A":
            rating = parse_rating(product.rating)
            heapq.heappush(heap, (-rating, i, product))  # Max heap for rating
    top_products = []
    for _ in range(min(max_results, len(heap))):
        if heap:
            top_products.append(heapq.heappop(heap)[2])
    return top_products

# RATING-PRICE RECOMMENDATION SYSTEM

def compute_rating_price_score(product):
    rating = parse_rating(product.rating)
    price = product.price
    if price <= 0:  # Avoid log(0) or negative
        price = 1
    return (rating ** 2) / math.log10(price)

def get_rating_price_recommendations(products, max_results=10):
    # Filter products with valid prices
    valid_products = [p for p in products if p.price != "N/A"]
    if not valid_products:
        return [], 0

    # Compute scores and use max heap
    heap = []
    for i, product in enumerate(valid_products):
        score = compute_rating_price_score(product)
        heapq.heappush(heap, (-score, i, product))  # Max heap

    top_products = []
    for _ in range(min(max_results, len(heap))):
        if heap:
            score, j, product = heapq.heappop(heap)
            product.score = -score  # Store score for display
            top_products.append(product)

    return top_products, len(valid_products)
