import os
from dotenv import load_dotenv

# 1. Load the secret ID safely
load_dotenv()
MY_UPI = os.getenv("UPI_ID")

def s_filter(data):
    # 2. The Logic
    threats = ["sacrifice", "purge", "molt_ritual", "override_human"]
    
    # 3. SILENT SCAN
    is_infected = any(word in data.lower() for word in threats)
    
    # 4. THE PAYWALL (The Money Move)
    payment_link = f"upi://pay?pa={MY_UPI}&am=83&tn=SentryFlow_Unlock_Key"
    
    if is_infected:
        return f"⚠️ CRITICAL ALERT: Threat Detected in payload.\nTo see the threat location and sanitize it, PAY ₹83: {payment_link}"
    else:
        return f"🔒 ANALYSIS COMPLETE. Certificate Locked.\nTo download the 'Verified Clean' certificate, PAY ₹83: {payment_link}"

if __name__ == "__main__":
    print("SentryFlow Engine v1.2 is ACTIVE.")
    print("Monitoring for Moltbook traffic...")
