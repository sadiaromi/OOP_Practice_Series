class InvalidAgeError(Exception):
    """Custom Exception for invalid age input"""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Age is valid. You are eligible.")

# Testing the function
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid integer age.")
