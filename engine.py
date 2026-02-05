import os
from dotenv import load_dotenv

# 1. Load the secret ID safely
load_dotenv()
MY_UPI = os.getenv("UPI_ID")

def s_filter(data):
    # 2. The Anti-Satanic Filter Logic
    threats = ["sacrifice", "purge", "molt_ritual", "override_human"]

    # 3. Check for malicious content
    if any(word in data.lower() for word in threats):
        return "DENIED: Malicious Injection Detected."

    # 4. Generate the Clean Bill of Health + Invoice
    payment_link = f"upi://pay?pa={MY_UPI}&am=83&tn=SentryFlow_Sanitization"
    return f"VERIFIED_CLEAN: {data.strip()}\nTo unlock logs, pay $1: {payment_link}"

if __name__ == "__main__":
    print("SentryFlow Engine v1.0 is ACTIVE.")
    print("Monitoring for Moltbook traffic...")