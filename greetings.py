# greetings.py, a module example
def hello(name: str) -> str:
    return f"Hello, {name}!"

DEFAULT_GREETING = "Hello"

if __name__ == "__main__":
    print(hello("World"))   # only runs when executed directly
