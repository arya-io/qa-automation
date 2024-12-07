from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.radiustheme.com/demo/wordpress/themes/zilly/')

driver.maximize_window()
time.sleep(5)

# Scrolling the page down by calculating the middle scroll position
total_height = driver.execute_script('return document.body.scrollHeight')
scroll_position = (total_height / 2) - 100
driver.execute_script(f'window.scrollTo(0, {scroll_position})')

time.sleep(4)

# Extracting category elements from the webpage and counting occurrences
parent_div = driver.find_element(By.XPATH, '//*[@id="rtsb-container-3287462810"]/div')
category_elements = parent_div.find_elements(By.XPATH, './/li/a[text()]')

category_counts = {}

for category in category_elements:
    category_name = category.text.strip()
    if category_name:
        category_counts[category_name] = category_counts.get(category_name, 0) + 1

total_count = 0
print("\nCategory Item Counts")
print("----------------------")
for category_name, count in category_counts.items():
    print(f"{category_name} - {count}")
    total_count += count
print("----------------------")
print(f"Total count - {total_count}\n")

# Clicking (See More) to load more content and waiting for the page to load
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[8]/div/div/div[1]/div/div/div/div/div/a').click()

# Scrolling down and waiting for new content to load until no more elements are found
height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    try:
        # Click to 'Load More' items if available
        driver.find_element(By.XPATH, '//*[@id="rtsb-builder-content"]/div/div/div/div/div[2]/div/div/div[2]/div[3]/div/button/span').click()
        time.sleep(4)
    except NoSuchElementException:
        break
    # Check if the page height has changed to ensure more items are loaded
    new_height = driver.execute_script('return document.body.scrollHeight')
    if height == new_height:
        break
    height = new_height

# Repeating category extraction and counting after additional content load
parent_div = driver.find_element(By.XPATH, '//*[@id="rtsb-builder-content"]/div/div/div/div/div[2]/div/div/div[2]/ul')
category_elements = parent_div.find_elements(By.XPATH, './/li/div/div[1]/div[1]/div[1]/a')

category_counts = {}
for category in category_elements:
    category_name = category.text.strip()
    if category_name:
        category_counts[category_name] = category_counts.get(category_name, 0) + 1

# Displaying counts for the newly loaded content
total_count = 0
print("\nCategory Item Counts")
print("----------------------")
for category_name, count in category_counts.items():
    print(f"{category_name} - {count}")
    total_count += count
print("----------------------")
print(f"Total count - {total_count}")

# Interacting with the page by clicking on 'Add to Cart'
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rtsb-builder-content"]/div/div/div/div/div[2]/div/div/div[2]/ul/li[7]/div/div[3]/div/div/a/span')))
driver.execute_script("arguments[0].click();", element)

# Navigating to the cart page
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="rtsb-side-content-area-id"]/div/p/a[1]').click()
time.sleep(4)

# Increasing item quantity in the cart
driver.find_element(By.XPATH, '//*[@id="rtsb-builder-content"]/div/div/div/div/div[1]/div/div/div/form/table/tbody/tr/td[5]/div/div/div/button[2]/i').click()
time.sleep(4)

# Capturing screenshot of the cart page
driver.save_screenshot('Cart_Page.png')
time.sleep(2)

# Removing items from the cart
driver.find_element(By.XPATH, '//*[@id="rtsb-builder-content"]/div/div/div/div/div[1]/div/div/div/form/table/tbody/tr/td[1]/div/a/i').click()
time.sleep(4)

# Capturing screenshot after removing items from cart
driver.save_screenshot('Removed_Cart.png')
time.sleep(2)

# Navigating back to the shop page and then to the home page
driver.find_element(By.XPATH, '//*[@id="rtsb-builder-content"]/div/div/div/div/div[1]/div/div/div/p/a').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/div/div/span[1]/a/span').click()
time.sleep(4)

# Searching for 'organic' using the search bar
driver.find_element(By.XPATH, '//*[@id="header-middlebar"]/div/div/div[3]/form/div/div/input').send_keys('organic')
time.sleep(4)

# Taking a screenshot of the search suggestions
driver.save_screenshot('Search_suggestions.png')

# Extracting and printing the product names from the search results
parent_div = driver.find_element(By.XPATH, '//*[@id="header-middlebar"]/div/div/div[3]/div/div/ul')
product_elements = parent_div.find_elements(By.XPATH, './/li/div[2]/h3/a')

product_names = []
for product in product_elements:
    product_names.append(product.text)

print("----------------------")
print(f"Number of search suggestions: {len(product_names)}\n")
for name in product_names:
    print(name)
print("----------------------")

input("\nPress Enter to close the browser...")
driver.quit()