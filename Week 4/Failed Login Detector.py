login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]
# track failure counts
user_failures = {}

print("Checking login attemppts...")

for attempt in login_attempts:
    username = attempt[0]
    status = attempt[1]

    #ignoring any "success" logins and only focusing on the failures
    if status == "failed":

        #If we have seen this user fail before, add 1 to their count. If this is their first failure, set their count to 1
        if username in user_failures:
            user_failures[username] = user_failures[username] + 1
        else:
            user_failures[username] = 1

for user in user_failures:
    count = user_failures[user]
    
    #check against our securrity threshold
    if count >= 3:
        print(f"ALERT: User '{user}' has {count} failed login attempts")

print("Security check complete")