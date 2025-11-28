import sys

correct_password = 'HTW'
max_attempts = 5
curr_attempts = 0

while curr_attempts < max_attempts:
    pass_try = input('Enter your password:')
    if pass_try == correct_password:
        print('Welcome Chris!')
        sys.exit(0)
    print('Incorrect')
    curr_attempts += 1

print('Too many login attempts')