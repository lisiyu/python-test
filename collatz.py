#第一种写法
while True:
    def collatz(number):
        global num
        if (number % 2) ==0:
            number = (number / 2)
            print(int(number))
            num = number
        elif (number % 2) ==1:
            number = 3 * number +1
            print(int(number))
            num = number
    try:
        num = int(input())
        while True:
            collatz(num)
            if num == 1:
                break
    except ValueError:
        print('请输入一个整数')
