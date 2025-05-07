# Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called") 
        func()  
    return wrapper  

# Apply decorator using @

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
