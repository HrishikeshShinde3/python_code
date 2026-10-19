# count login failed & login success attempts

attempts = ["success", "failed", "failed", "success", "failed", "success","success"]

count = 0

for attempt in attempts:
    if attempt == "failed":
        count = count + 1

print("Login failed", count, "times")

count = 0

for attempt in attempts:
    if attempt == "success":
        count = count + 1
print("Login success", count, "times")