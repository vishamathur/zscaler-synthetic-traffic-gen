from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import time
import random

def simulate_edge_traffic(use_case, count):
    base_urls = {
        "URL Filtering": ["http://example.com", "http://badsite.com"],
        "SSL Inspection": ["https://secure.example.com"],
        "App Control": ["https://youtube.com", "https://facebook.com"],
        "CASB Trigger": ["https://drive.google.com"],
        "DLP Violation": ["https://wetransfer.com"]
    }

    logs = []
    options = Options()
    options.add_argument("--headless")  # Run Edge in headless mode
    options.add_argument("--disable-gpu")

    # Update this path if msedgedriver is in a different location
    service = EdgeService(executable_path="msedgedriver")

    driver = webdriver.Edge(service=service, options=options)

    for _ in range(count):
        url = random.choice(base_urls.get(use_case, ["http://example.com"]))
        try:
            start_time = time.time()
            driver.get(url)
            time.sleep(2)  # wait for page to load
            logs.append({
                "url": url,
                "title": driver.title,
                "load_time": round(time.time() - start_time, 2),
                "timestamp": time.time()
            })
        except Exception as e:
            logs.append({
                "url": url,
                "error": str(e),
                "timestamp": time.time()
            })
        time.sleep(1)

    driver.quit()
    return logs

# Example usage:
if __name__ == "__main__":
    logs = simulate_edge_traffic("App Control", 3)
    for log in logs:
        print(log)
