# Author: Samarpita Sharma
# Mini SIEM Tool - Brute Force Detector

from collections import Counter

# sample log data - simulating real system logs
sample_logs = [
    "LOGIN SUCCESS user=sam",
    "LOGIN FAILED user=admin",
    "LOGIN FAILED user=admin",
    "LOGIN FAILED user=admin",
    "LOGIN SUCCESS user=john",
    "LOGIN FAILED user=root"
]

# write sample logs to file
with open("auth.log", "w") as f:
    for line in sample_logs:
        f.write(line + "\n")

# analyze logs
failed_users = []
successful_logins = 0

with open("auth.log", "r") as f:
    for line in f:
        if "FAILED" in line:
            user = line.split("user=")[1].strip()
            failed_users.append(user)
        elif "SUCCESS" in line:
            successful_logins += 1

counts = Counter(failed_users)

# report
print("=" * 40)
print("   mini siem - brute force detector")
print("=" * 40)
print(f"total failed logins  : {len(failed_users)}")
print(f"total successful logins : {successful_logins}")
print("\nfailed attempts per user:")
for user, count in counts.items():
    if count >= 2:
        print(f"  [!] {user} - {count} attempts - possible brute force")
    else:
        print(f"  [-] {user} - {count} attempt")
print("=" * 40)