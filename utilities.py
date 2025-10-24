import re

def parse_discount(discount):
    if discount == "N/A":
        return 0
    try:
        return int(re.sub(r"[^\d]", "", discount))
    except ValueError:
        return 0

def parse_rating(rating):
    if rating == "N/A":
        return 0.0
    try:
        return float(rating)
    except ValueError:
        return 0.0
    
def impute_na_ratings(products):
    # Compute average rating from valid ratings
    valid_ratings = [parse_rating(p.rating) for p in products if parse_rating(p.rating) > 0]
    avg_rating = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 4.0  # Default 4.0
    na_count = sum(1 for p in products if parse_rating(p.rating) == 0)

    # Update products with "N/A" ratings
    for product in products:
        if parse_rating(product.rating) == 0:
            product.rating = f"{avg_rating:.1f}"

    return na_count, avg_rating


