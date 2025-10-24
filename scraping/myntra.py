import logging
from scraping.selenium_utils import *
from datastructures import Product

def scrape_myntra(query, max_results=10):
    products = []
    driver = setup_driver()
    query = query.replace(" ", "-")
    url = f"https://www.myntra.com/{query}"
    logging.info(f"🔍 Scraping Myntra: {url}")
    driver.get(url)

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.product-base"))
        )
        soup = smart_scroll(driver, scroll_count=8, pause=2)
        items = soup.select("li.product-base")[:max_results]

        for item in items:
            try:
                name_tag = item.select_one("h4.product-product")
                name = name_tag.text.strip() if name_tag else "N/A"

                link_tag = item.select_one("a")
                link_href = link_tag.get("href", "") if link_tag else ""
                if link_href.startswith("/"):
                    link = "https://www.myntra.com" + link_href
                elif link_href.startswith("http"):
                    link = link_href
                else:
                    link = "https://www.myntra.com/" + link_href

                price_tag = item.select_one("span.product-discountedPrice")
                price = parse_price(price_tag.text.strip() if price_tag else "N/A")

                original_price_tag = item.select_one("span.product-strike")
                discount = "N/A"
                if original_price_tag:
                    old_price = parse_price(original_price_tag.text.strip())
                    if old_price != "N/A" and price != "N/A" and old_price > price:
                        discount = f"{round(((old_price-price)/old_price)*100)}% off"

                rating_tag = item.select_one("div.product-ratingsContainer span")
                rating = rating_tag.text.strip() if rating_tag else "N/A"

                if name != "N/A" and price != "N/A":
                    products.append(Product(name, price, discount, rating, link, "Myntra"))

            except Exception:
                continue

    finally:
        driver.quit()
    return products[:max_results]