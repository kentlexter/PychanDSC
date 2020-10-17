def greet(name):
    print(f"Hi {name}")  # Locked to printing in a terminal, not reusable

# 1 - Perform a task
# 2 - Return a value


# round(1.9)

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Kent")  # Reusable, we can do whatever we want.
print(message)

print(greet("Kent"))
