from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main():
    options = Options()
    options.add_argument("--headless=new")  # Headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Prevent /dev/shm errors
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--enable-javascript")  # JavaScript (enabled by default)

    driver = webdriver.Chrome(options=options)

    print("Loading illphated.com...")
    driver.get("https://illphated.com")

    # Let JS load
    time.sleep(5)

    print("Page title:", driver.title)
    driver.save_screenshot("illphated_screenshot.png")
    print("Screenshot saved as illphated_screenshot.png")

    driver.quit()

if __name__ == "__main__":
    main()
