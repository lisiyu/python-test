#初学Python 3.5
1、	input函数获取键盘输入数字需要用int()函数转义。
2、	不能TAB和空格混用做代码对齐不然会出现错误：IndentationError: unindent does not match any outer indentation level错误的使用缩进量。（导致“IndentationError：unexpected indent”、“IndentationError：unindent does not match any outer indetation level”以及“IndentationError：expected an indented block”）
3、	While True循环下面一定要break跳出。
4、	Continue是跳回循环起点不是往下继续的意思。
5、	忘记在 if , elif , else , for , while , class ,def 声明末尾添加 ：（导致 “SyntaxError ：invalid syntax”）
6、	在字符串首尾忘记加引号（导致“SyntaxError: EOL while scanning string literal”）
7、	Python3的关键字有：and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield
8、	需要以管理员身份运行IDLE否则可能出现错误：IDLE's subprocess didn't make connection.  Either IDLE can't start a subprocess or personal firewall software is blocking the connection.
9、	留意import  xxx 和from xxx import * 的区别
10、忘记字符串加引号或者误把双引号当当引号报错eol while scanning literal
11、在python中以“0”为开始的所有文字被视为八进制数，仅数字0是允许的。其他含0的数字需要表示为”05”这样.否则报错为:  "SyntaxError: invalid token"
12、TypeError: object of type 'int' has no len() 整数形变量没有长度.
13、交互模式中，最近一个表达式的值赋给变量 _。_变量对于用户是只读的。不要尝试给它赋值.
14、print语句默认的会在后面加上换行,加了逗号之后换行就变成了空格.多种不同类型的值之间也可以用逗号分隔. 例如print("Found " + 5)会报错.因为前一个值是字符串后一个值是整形.但是可以这样输出print("Foundr",5)或print("Found"+ str(5)).
15、a = a + 1 缩写成 a += 1的时候请注意+和=之间没有空格
16、字典中键为非整数时需要加引号。
17、安装第三方模块.到安装目录 C:\Users\ChalLee\AppData\Local\Programs\Python\Python35\Scripts 打开命令窗口输入 : pip install +模块名.例如:pip install beautifulsoup4 如果安装遇到报网络超时的错误请打开全局VPN翻墙. FUCK GFW
