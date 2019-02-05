secret = 'test'
pw = ''
auth = False
count = 0
max_attempts = 3

while pw != secret:
    count += 1
    if count > max_attempts:
        break
    pw = input(f'{count}: What is the secret word? ')
else:
    auth = True

print('Authorized!!!' if auth else 'You are locked out')