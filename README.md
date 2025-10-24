# 🧠 Choose‑better

## 📖 Overview  
**Choose‑better** is an intelligent Python project that merges **multi‑website web scraping** with **data‑driven algorithmic analysis**.  
It automatically collects product or deal data from top e‑commerce sites like **Amazon, Flipkart, ShopClues, Myntra, and Snapdeal**, and then processes that information using **optimization algorithms** (Greedy, Knapsack, Heap Sort, etc.) to help users *choose better* among competing options.

This project demonstrates how **real-world data scraping** and **classical algorithms** can work hand‑in‑hand for analytical and decision‑support systems.

---

## 🚀 Key Features  

### 🌐 Web Scraping Suite  
The `scraping/` folder includes separate scrapers for each major e-commerce platform:  
- 🛒 `amazon.py` — Extracts product names, prices, ratings, and links from Amazon.  
- 🏬 `flipkart.py` — Gathers detailed product listings from Flipkart, handling pagination and dynamic content.  
- 🛍️ `myntra.py` — Fetches fashion items and price data from Myntra.  
- 🧾 `shopclues.py` — Scrapes item names, discounts, and availability from ShopClues.  
- 💻 `snapdeal.py` — Captures product details and ratings from Snapdeal.  

Each scraper uses **BeautifulSoup** and/or **Selenium** depending on whether the page is static or dynamically loaded.

### ⚙️ Selenium Utilities  
Located in the `scraping/`:  
- Automates browser sessions (Chrome WebDriver).  
- Waits for elements to load using `WebDriverWait`.  
- Includes smart delays and retry logic to avoid detection.  
- Manages dynamic content rendering and JavaScript-heavy pages.

### 🧮 Algorithms & Data Structures  
After scraping, collected data is processed using algorithms from the root modules:  
- **`datastructures.py`** — Defines reusable structures for managing product and price data.  
- **`greedy.py`** — Implements greedy decision logic for selecting the best options under constraints.  
- **`heap_sort.py`** — Sorts large datasets efficiently based on user-defined metrics (like price or rating).  
- **`knapsack.py`** — Solves the 0/1 Knapsack problem for optimal budget allocation (maximize value under price limit).  
- **`utilities.py`** — Common helpers for data cleaning, formatting, logging, and visualization.  

### 🧩 Integration (main.py)  
`main.py` connects all modules — scraping, cleaning, and analysis — to produce actionable results like:  
- Sorted product lists by best price-to-rating ratio.  
- Optimal product combination under a fixed budget.  
- Cross-platform comparisons of the same item.

---

## 🏗️ Project Structure  
```
Choose-better/
│
├── scraping/
│   ├── amazon.py
│   ├── flipkart.py
│   ├── shopclues.py
│   ├── myntra.py
│   ├── snapdeal.py
│   └── selenium_utils.py      # Selenium setup and browser automation helpers
│
├── datastructures.py
├── greedy.py
├── heap_sort.py
├── knapsack.py
├── utilities.py
├── main.py
└── __pycache__/
```

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/Varunesh07/Choose-better.git
cd Choose-better
```

### 2️⃣ Install dependencies  
Make sure **Python 3.8+** is installed. Then run:  
```bash
pip install -r requirements.txt
```

**Typical dependencies include:**  
```
requests
beautifulsoup4
selenium
webdriver-manager
lxml
logging
math
```
*(If you don’t have a requirements file, you can manually install them using pip.)*

### 3️⃣ Configure Selenium (if using Chrome)  
Make sure Chrome browser and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) are installed.  
The `webdriver_manager` automatically handles driver setup.

### 4️⃣ Run the Project  
To scrape and process all data:  
```bash
python main.py
```

To test individual modules:  
```bash
python scraping/amazon.py
python greedy.py
python knapsack.py
```

---

## 🧠 Workflow Summary  
1. **Data Collection:**  
   Each scraper collects product data (price, rating, etc.) from its respective site.  
2. **Data Cleaning & Storage:**  
   Data is cleaned, filtered, and optionally saved to a CSV/JSON file.  
3. **Algorithmic Analysis:**  
   The main script uses sorting, greedy optimization, or knapsack methods to find the best product(s).  
4. **Results Display:**  
   Outputs a ranked list or optimal set of products with maximum value under a given constraint.

---

## 🧩 Example Use Cases  
- 🛍️ **Find Best Deals:** Compare same products across multiple platforms.  
- 💸 **Optimize Spending:** Select items that maximize value under a budget limit (Knapsack).  
- 📈 **Rank Products:** Sort by weighted metrics using Heap Sort.  
- ⚡ **Quick Picks:** Use Greedy heuristics for fast, near-optimal results.

---

## Main Contributors

<table> <tr>  <td align="center"> <a href="https://github.com/abhx12"> <img src="https://avatars.githubusercontent.com/u/195339058??v=4" width="100px;" alt="Nithiish SD"/> <br /> <sub><b>Abhishek J R</b></sub> </a> </td> <td align="center"> <a href="https://github.com/Varunesh07"> <img src="https://avatars.githubusercontent.com/u/205139899?v=4" width="100px;" alt="Varunesh S"/> <br /> <sub><b>Varunesh S</b></sub> </a> </td> <td align="center"> <a href="https://github.com/Monarch0703"> <img src="https://avatars.githubusercontent.com/u/118116807?v=4" width="100px;" alt="Harshith Shiva"/> <br /> <sub><b>Jithendra U</b></sub> </a> </td> </tr> </table>

