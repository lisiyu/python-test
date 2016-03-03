#考拉赫兹猜想第二种写法

while True:
    print('欢迎使用考拉赫兹猜想计算器')
    def collatz(number):
        if (number % 2) ==0:
            number = (number / 2)
            print(int(number))
            return number
        elif (number % 2) ==1:
            number = 3 * number +1
            print(int(number))
            return number
    def jisuan():
        num = int(input('请输入一个数字 '))
        while True:
            num = collatz(num)
            if num == 1:
                print('考拉赫兹猜想计算结束')
                break
    try:
        jisuan()
    except ValueError:
        print('请输入一个整数')# 
