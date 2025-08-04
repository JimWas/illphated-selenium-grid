from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def start_browser():
    options = Options()
    options.add_argument("--headless=new")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--enable-javascript")

    return webdriver.Chrome(options=options)

def main():
    driver = start_browser()
    
    try:
        while True:
            print("Loading illphated.com...")
            driver.get("https://illphated.com")
            print("Page title:", driver.title)

            # Optional screenshot every reload
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            driver.save_screenshot(f"illphated_{timestamp}.png")
            print(f"Screenshot saved as illphated_{timestamp}.png")

            # Wait 20 minutes (1200 seconds)
            print("Waiting 20 minutes before reload...")
            time.sleep(1200)  

            print("Reloading page...")
            driver.refresh()

    except KeyboardInterrupt:
        print("Stopping browser loop...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
