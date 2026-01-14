def greet_names():
    names = ["Rubeen", "Muri", "William", "Negus", "Byron"]
    greetings = []

    for name in names:
        greetings.append(f"Hello, {name}")

    return greetings

for greeting in greet_names():
    print(greeting)