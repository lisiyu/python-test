while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password(letters and numbers only,At least 6 characters):')
    password = input()
    if password.isalnum() and len(password) > 5:
        break
    print('Password can only have letters and numbers.')
