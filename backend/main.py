

print("hello backend!")

import requests
user_responce = renpy.fetch("https://itch.io/api/1/me/me")
print(f"responce: {user_responce}")
user_info = user_responce.json()
print(f"info: {user_info}")
user_id = user_info.get("id")
print(f"user id: {user_id}")


