import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from scraping.amazon import scrape_amazon
from scraping.flipkart import scrape_flipkart
from scraping.myntra import scrape_myntra
from scraping.shopclues import scrape_shopclues
from scraping.snapdeal import scrape_snapdeal
from utilities import  *
from heap_sort import *
from greedy import *
from knapsack import handle_budget_knapsack

def display_menu():
    print("\nChoose option:")
    print("1) Price (High to Low)")
    print("2) Price (Low to High)")
    print("3) Rating (High to Low)")
    print("4) Discount (High to Low)")
    print("5) Price Range Query (Greedy Top 10 by Rating-Price Recommendation)")
    print("6) Budget Knapsack DP (Maximize Score within Budget)") 
    print("7) Exit") 
    return input("Enter choice (1-7): ").strip()

def main():
    product_name = input("Enter product name to search: ").strip()
    logging.info(f"🔍 Searching for '{product_name}' across Amazon, Myntra, Snapdeal, ShopClues, and Flipkart...\n")

    # Store all scraped products in a Python list
    all_products = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_scraper = {
            executor.submit(scrape_amazon, product_name, 10): "Amazon",
            executor.submit(scrape_myntra, product_name, 10): "Myntra",
            executor.submit(scrape_snapdeal, product_name, 10): "Snapdeal",
            executor.submit(scrape_shopclues, product_name, 10): "ShopClues",
            executor.submit(scrape_flipkart, product_name, 10): "Flipkart"
        }
        for future in as_completed(future_to_scraper):
            try:
                products = future.result()
                all_products.extend(products)
                logging.info(f" {future_to_scraper[future]}: {len(products)} products scraped")
            except Exception as e:
                logging.error(f"Error in {future_to_scraper[future]}: {e}")

    if not all_products:
        print(" No products scraped.")
        return

    # Impute "N/A" ratings globally
    na_count, avg_rating = impute_na_ratings(all_products)
    print(f"\nImputed {na_count} 'N/A' ratings with average {avg_rating:.1f}")

    # Rating-Price Recommendation
    print("\n Rating-Price Recommendation (Top 10 Products)")
    print("="*60)
    top_products, valid_count = get_rating_price_recommendations(all_products)
    if not top_products:
        print("No products available for recommendation.")
    else:
        if len(top_products) < 10:
            print(f"Note: Only {len(top_products)} products available.")
        for i, product in enumerate(top_products, start=1):
            print(f"{i}. {product}Score: {product.score:.2f}")
    print(f"Total Valid Products: {valid_count}")
    print("="*60)

    print(f"\n🎯 Total Products Found: {len(all_products)}\n{'='*60}")

    # Menu-driven loop
    while True:
        choice = display_menu()
        if choice == "1":
            top_products = sort_by_price_desc(all_products)
            print("\nTop 10 Products Sorted by Price (High to Low):")
        elif choice == "2":
            top_products = sort_by_price_asc(all_products)
            print("\nTop 10 Products Sorted by Price (Low to High):")
        elif choice == "3":
            top_products = sort_by_rating(all_products)
            print("\nTop 10 Products Sorted by Rating (High to Low):")
        elif choice == "4":
            top_products = sort_by_discount(all_products)
            print("\nTop 10 Products Sorted by Discount (High to Low):")
        elif choice == "5":
            top_products, min_price, max_price = handle_range_query(all_products)
            if min_price is not None and max_price is not None:
                print(f"\nTop 10 Products in Price Range ₹{min_price:.2f} to ₹{max_price:.2f} (Greedy Top 10):")
        elif choice == "6":  
            top_products, total_score, total_cost, budget, max_items = handle_budget_knapsack(all_products)
            if top_products:
                print(f"\n BUDGET KNAPSACK DP RESULTS")
                print(f" Budget: ₹{budget} | 📦 Max Items: {max_items}")
                print(f" Selected: {len(top_products)} items | Total Cost: ₹{total_cost}")
                print(f" Total Score: {total_score:.2f}")
                print("="*60)
            else:
                print("\n No valid selection possible for given budget!")
                top_products = []
        elif choice == "7": 
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        # Display results
        if not top_products:
            print("No products available for this criterion.")
        else:
            if choice in ["1", "2", "3", "4"] and len(top_products) < 10:
                print(f"Note: Only {len(top_products)} products available.")
            for i, product in enumerate(top_products, start=1):
                score_text = f"Score: {product.score:.2f}" if hasattr(product, 'score') else ""
                # Handle temp_score for budget knapsack
                if choice == "6" and hasattr(product, 'temp_score'):
                    score_text = f"Score: {product.temp_score:.2f}"
                print(f"{i}. {product}{score_text}")

if __name__ == "__main__":
    main()