# data.py

headers = {
    "Content-Type": "application/json"
}

def get_user_body(first_name):
    return {
        "firstName": first_name,
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    }
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

product_ids = {
    "ids": [1, 2, 3]
}
