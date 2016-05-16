spam = ['apples', 'bananas', 'to', 'cats', '5', 'go']


def add_comma(lists=None):
    if lists is None:
        lists = []
    for i in range(len(lists) - 1):
        lists.insert(i + i + 1, ',')
    lists.insert(len(lists) - 1, 'and')
    for x in range(len(lists)):
        string = ''
        string = string + lists[x]
        print(string, end='')


add_comma(spam)
