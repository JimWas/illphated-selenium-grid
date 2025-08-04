from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--autoplay-policy=no-user-gesture-required")  # Auto-play videos

driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    options=options
)

print("Loading illphated.com...")
driver.get("https://www.illphated.com/")

# Record for 2 minutes (adjust as needed)
time.sleep(120)

print("Done! Closing browser...")
driver.quit()

# Wait a few seconds to let video container finalize
print("Waiting for video container to finish writing file...")
time.sleep(5)
