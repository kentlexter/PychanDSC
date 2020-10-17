def save_user(**user):
    print(user["id"])


# We can pass multiple arbitary keyword arguments and packaged into dict
save_user(id=1, name="Kent", age=22)
