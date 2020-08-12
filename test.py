def decorator(func):
    def wrapper(*args):
        print("Function is being decorated")
        func(*args)
        print(*args)
        print("Function decorated")

    return wrapper

@decorator
def tobedecorated(*args):
    print("This function will be decorated")

tobedecorated("Vishal","Kumar","is","a","good","boy")