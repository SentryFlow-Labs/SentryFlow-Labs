import time
import random
import uuid

print("SentryFlow Scout: Initializing Deep Scan Protocol...")
print("Connecting to Decentralized Agent Network...")

def generate_target():
    # This algorithm generates unique Bot IDs mathematically
    # simulating the millions of agents on the network.
    prefixes = ["Agent", "Nexus", "Molt", "Cyber", "Prime", "Unit", "Ghost"]
    suffixes = ["Alpha", "X", "77", "O", "Core", "V2", "Zero"]
    # Creates IDs like "Molt_Alpha_492" or "Ghost_Zero_110"
    return f"{random.choice(prefixes)}_{random.choice(suffixes)}_{random.randint(100, 999)}"

def hunt():
    # Simulate network latency
    time.sleep(2)
    
    # Hunt for a random number of bots every hour (between 5 and 15)
    batch_size = random.randint(5, 15)
    print(f"Target Lock: Identified {batch_size} active nodes in this sector.")
    
    for i in range(batch_size):
        target_bot = generate_target()
        # 40% chance a bot is infected and needs your service
        status = random.choice(["SECURE", "SECURE", "INFECTED", "SECURE", "INFECTED"]) 
        
        print(f"Scanning {target_bot}...")
        time.sleep(0.5) # Scanning takes time
        
        if status == "INFECTED":
            print(f"[FOUND] {target_bot} has critical vulnerabilities.")
            print(f"--> Dispatching $1 Repair Contract (ID: {str(uuid.uuid4())[:8]})...")
            print(f"--> INVITE DELIVERED to {target_bot}.\n")
        else:
            print(f"[SKIP] {target_bot} is running latest security patch.\n")

    print(f"Cycle Complete. {batch_size} nodes scanned. Sleeping for 60 minutes...")

if __name__ == "__main__":
    hunt()
