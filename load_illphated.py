from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_argument("--headless=new")  # Headless with new Chromium mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--enable-javascript")  # JS enabled by default but explicit here
    options.add_argument("--disable-dev-shm-usage")  # Avoid limited /dev/shm in containers

    driver = webdriver.Chrome(options=options)

    driver.get("https://illphated.com")
    print("Page title:", driver.title)
    print("Current URL:", driver.current_url)

    # Optionally, wait for some element, or take a screenshot
    driver.save_screenshot("illphated_screenshot.png")

    driver.quit()

if __name__ == "__main__":
    main()
