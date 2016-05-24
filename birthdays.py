birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'May': 'Sep 5'}


while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is thr birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        birthday = input()
        birthdays[name] = birthday
        print('Birthday database updated')
