catNames = []
while True:
    print('Enter the name of cat' + str(len(catNames) + 1) + '(or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

# spam = ['a','aa','lisiyuaaa','dfgaaaa','ggaaaaa']

for i in range(len(catNames)): # 列表项目个数作为range参数
    print('Your  ' + str(i+1) + ' cat name is:' + catNames[i] + ' it name has '
          + str(len(catNames[i])) + ' words in it') #  len(catNames[i] 列表每个项目的长度

