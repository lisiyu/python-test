name = ''
while name =='':
    print('enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = input()
numOfGuests = int(numOfGuests)
if numOfGuests != 0 : #(2)
    print('Be sure to have enough room for all your guests.') #(3)
print('Done')
