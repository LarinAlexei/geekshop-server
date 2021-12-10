import json

data = {
    "user_login": {
        "name": "Larina Liza",
        "city": "Briansk",
        "status": "Gold"
    }
}

with open("new_user.json", "w") as write_file:
    json.dump(data, write_file)

with open("new_user.json", "r") as read_file:
    data = json.load(read_file)

print(type(data))
print(data)

print(data.get("user_login"))

res = {}
res = data.get("user_login")
print(type(res))
for i, j in res.items():
    print(i, j)


def user_info(name):
    with open("new_user.json", "r") as read_file:
        data_user = json.load(read_file)
    return data_user.get(name)


user = user_info("user_login")

print(user)
