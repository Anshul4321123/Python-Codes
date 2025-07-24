import req

url = "http://127.0.0.1:8000/user/"  

data = {
    "username": "newuser",
    "password": "mypassword"
}

response = req.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
