# age.py  
#age = input('How old are you today? ')  
#age= int(age)  
#print('In 10 years you will be ' +  str(age) + ' years old.') 
age = input('输入你的岁数  ') #input函数获取的为字符串，要从键盘获取输入的数字需要用int函数强行转义。input函数（）中的可以写入字符串做输入提示。
age = int(age)
if age < 5:
    print('Hi, baby.')
elif 5 < age < 12:
    print('You are kid.')
elif 13 < age < 20:
    print('You are young.')
elif age > 20:
    print('you are man.')
