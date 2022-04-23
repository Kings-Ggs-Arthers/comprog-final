def user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


user(id=1, name="John", age=22)
