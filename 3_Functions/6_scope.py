message = "a"  # Global, dont use this!
# Create functions with params & local variables


def greet(name):
    message = "c"  # Local


def send_email(name):
    message = "b"


def change_global(name):
    global message  # bad practice
    message = "z"


greet("Kent")
print(message)
