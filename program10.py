# Function to simulate connecting to a secure service
def connect_to_service(username, password, jwt_token):
    if username == "admin" and password == "your_password_here" and jwt_token == "your_jwt_token_here":
        return "Connected to the secure service!"
    else:
        return "Failed to connect."

# Call the function with the JWT token
print(connect_to_service("admin", "your_password_here", "your_jwt_token_here"))

# Secrets
password = "your_password_here"
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiYWRtaW4iLCJleHAiOjE3MTIzNDU2Nzh9.mDxSJq-4iL80QDdJItuXAUWJTX\_Qt5NJfN5lUdKL7is"
print(f"Password: {password}")
print(f"JWT Token: {jwt_token}")
