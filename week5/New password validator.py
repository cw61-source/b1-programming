import random
import string

def check_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    return any(char.isprintable() and not char.isalnum() and not char.isspace() for char in password)

def validate_password(password):
    pass_dict = {
            'length': check_min_length(password),
            'upper': has_uppercase(password),
            'lower': has_lowercase(password),
            'digit': has_digit(password),
            'special': has_special_char(password),
            'is_valid': True
    }

    if not all(pass_dict.values()):
        pass_dict['is_valid'] = False

    return pass_dict

def formatResult(result):
    if result:
        return 'Met'
    return 'Not met'

user_word = input('Enter your password: ')
result = validate_password(user_word)

print('Analyzing provided password...')
print(f"Minimum length: {formatResult(result['length'])}")
print(f"Has uppercase: {formatResult(result['upper'])}")
print(f"Has lowercase: {formatResult(result['lower'])}")
print(f"Has digit: {formatResult(result['digit'])}")
print(f"Has special characters: {formatResult(result['special'])}")

if result['is_valid']:
    print('Strong password')
else:
    print('Weak password')
    hints = [
        "Try adding a number like 1 or 9",
        "Don't forget to use a Capital letter",
        "Special symbols like @ or ! make it safer"
    ]
    print("Hint: " + random.choice(hints))