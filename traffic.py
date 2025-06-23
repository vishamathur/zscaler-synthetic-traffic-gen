import random
import time

def generate_traffic(use_case, count):
    logs = []
    base_urls = {
        "URL Filtering": ["http://example.com", "http://badsite.com"],
        "SSL Inspection": ["https://secure.example.com"],
        "App Control": ["https://youtube.com", "https://facebook.com"],
        "Threat Prevention": ["http://malicious-site.com"],
        "CASB Trigger": ["https://drive.google.com", "https://dropbox.com"],
        "DLP Violation": ["https://upload.example.com"]
    }
    
    user_agents = [
        "Mozilla/5.0", "Chrome/110.0", "Edge/91.0", "Safari/537.36"
    ]

    for _ in range(count):
        url = random.choice(base_urls.get(use_case, ["http://example.com"]))
        agent = random.choice(user_agents)
        logs.append({
            "url": url,
            "user_agent": agent,
            "timestamp": time.time()
        })
        time.sleep(0.1)  # Simulate delay

    return logs
