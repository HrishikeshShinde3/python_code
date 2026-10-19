import math 

# find:

# Total number of requests
# Number of successful requests (200)
# Number of client errors (400–499)
# Number of server errors (500–599)
# Print "SERVER DOWN/RISK" whenever the status code is 500 or 503
# Calculate the percentage of successful requests

status_codes = [200, 200, 404, 500, 200, 403, 301, 500, 200, 404, 503, 200]

# Total number of requests
total_requests = 0

for status in status_codes:
    total_requests = total_requests +1
print("All requests on server are :",total_requests)

# Number of successful requests
successfull_requests = 0

for status in status_codes:
    if status == 200 :
        successfull_requests = successfull_requests + 1
print("All successful requests are:",successfull_requests)

# Number of client errors
client_errors = 0

for status in status_codes:
    if status == 400 or status == 499:
        client_errors = client_errors + 1
print("All client errors are :",client_errors)


# Number of server errors (500–599)
server_errors = 0

for status in status_codes:
    if status == 500 or status == 599:
        server_errors = server_errors + 1
print("All server errors are :",server_errors)

# print "Server down / Risk" for 500 or 503
6
for status in status_codes:
    if status == 500 or status == 503:

        print("Server down")

# % of successful reuests

for status in status_codes:
    percentage = ((successfull_requests / total_requests) * 100)
print("Percentage of successful requests are :",round(percentage),"%")










