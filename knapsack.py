from datastructures import Product, insert_avl, range_query_avl
from greedy import compute_rating_price_score
# NEW: DP BUDGET KNAPSACK (OPTION 7)

def budget_knapsack_dp(products, budget, max_items=5):
    """
    DP 0/1 Knapsack: Maximize total score within budget and max_items constraint
    dp[i][w][k] = max score using first i items, weight <= w, items <= k
    """
    valid_products = [p for p in products if p.price != "N/A"]
    n = len(valid_products)
    
    if n == 0:
        return [], 0, 0
    
    # 3D DP Table: dp[i][w][k]
    dp = [[[0 for _ in range(max_items + 1)] 
           for _ in range(budget + 1)] 
           for _ in range(n + 1)]
    
    # Track choices for backtracking
    choice = [[[0 for _ in range(max_items + 1)] 
               for _ in range(budget + 1)] 
               for _ in range(n + 1)]
    
    # Fill DP Table
    for i in range(1, n + 1):
        price = valid_products[i-1].price
        score = compute_rating_price_score(valid_products[i-1])
        
        for w in range(budget + 1):
            for k in range(max_items + 1):
                # Skip this item
                dp[i][w][k] = dp[i-1][w][k]
                choice[i][w][k] = 0
                
                # Take this item if possible
                if price <= w and k >= 1:
                    new_score = dp[i-1][w-price][k-1] + score
                    if new_score > dp[i][w][k]:
                        dp[i][w][k] = new_score
                        choice[i][w][k] = 1
    
    # Backtrack to reconstruct optimal solution
    selected = []
    total_cost = 0
    i, w, k = n, budget, max_items
    
    while i > 0 and w > 0 and k > 0:
        if choice[i][w][k] == 1:  # Took this item
            product = valid_products[i-1]
            product.temp_score = compute_rating_price_score(product)  # Store score
            selected.append(product)
            total_cost += product.price
            w -= product.price
            k -= 1
        i -= 1
    
    return selected[::-1], dp[n][budget][max_items], total_cost


# NEW: Budget Handler for Option 7

def handle_budget_knapsack(products):
    try:
        budget = int(input("Enter budget (₹): ").strip())
        max_items = int(input("Max number of products: ").strip())
        
        if budget <= 0 or max_items <= 0:
            print(" Budget and max items must be positive!")
            return [], 0, 0, 0, 0
        
        selected_products, total_score, total_cost = budget_knapsack_dp(products, budget, max_items)
        return selected_products, total_score, total_cost, budget, max_items
        
    except ValueError:
        print("Please enter valid numbers!")
        return [], 0, 0, 0, 0
