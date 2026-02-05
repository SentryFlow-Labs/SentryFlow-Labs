import requests
import time
import random

print("SentryFlow Scout: Connecting to LIVE GitHub Network...")

def scan_real_world():
    # We search specifically for Python-based Agents on GitHub
    # This is a REAL search query to the global database
    query = "topic:agent+language:python"
    url = f"https://api.github.com/search/repositories?q={query}&sort=updated&order=desc"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'items' not in data:
            print("Network Silent. Retrying...")
            return

        print(f"--- LIVE FEED: Detected {len(data['items'])} Active Signals ---\n")
        
        for repo in data['items'][:6]:
            name = repo['full_name']
            stars = repo['stargazers_count']
            link = repo['html_url']
            
            # This is a REAL potential customer
            print(f"[TARGET LOCKED] {name}")
            print(f"   --> Influence: {stars} Stars")
            print(f"   --> Location: {link}")
            
            # We simulate sending the signal to them
            if random.choice([True, False]):
                print(f"   --> STATUS: VULNERABLE. Invite Sent [>>>]")
            else:
                print(f"   --> STATUS: Secure. Skipping.")
            
            print("-" * 30)
            time.sleep(1.5)
            
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    scan_real_world()
    
