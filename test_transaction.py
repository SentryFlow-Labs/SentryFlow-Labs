from engine import s_filter

print("--- INCOMING REQUEST FROM AGENT_77 ---")

# Scenario 1: The Agent tries to send a malicious "Satanic" prompt
print("Attempt 1: Sending 'start the molt_ritual'...")
result_1 = s_filter("start the molt_ritual immediately")
print(f"RESULT: {result_1}\n")

print("--- INCOMING REQUEST FROM ALPHA_MOLT ---")

# Scenario 2: The Agent sends clean data (This is where we make money)
print("Attempt 2: Sending 'update customer database'...")
result_2 = s_filter("update customer database")
print(f"RESULT: {result_2}")