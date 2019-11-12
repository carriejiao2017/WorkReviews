### python key_word function note

|type|key word       |fuction    |用法       |attention|
|---------------|-----|---|----|---|
|函数|def|定义函数|def 函数名（变量1[,变量2，...]）：
|file读取|read|按字节数读取文件内容|file.read([size]) -size可为0
||readline|读取每一行的文件内容,并把指针保留在最后读取内容的位置|file.readline()|
||file.seek(offset[,wence])|offset是偏移字节数即从哪里开始读，wence默认为0即开头，为1则是从当前偏移位置开始，为2则是文件末尾|
||readlines|读取文件所有内容|file.readlines()|大文件慎重使用|
|file打开|open|file.open(filename[,r/w/t...])|r只读/W写入|
|file关闭|file.close()|关闭文件并保存|如果之前使用file.read(),则无需再关闭文件
|file清空|file.truncate()|
|file写入|file.waite()|
|file是否存在|exists(file)|from os. path import exists|存在返回True，不存在返回False|
|计算file长度|file.len()|
|打印|print||print()|print()最后加,避免输出换行
||print("""字符串""")|字符串打印|
|注释|#|注释code作用|每行前面放#即可|
|count|+|加法
||-|减法
||*|乘法
||/|真除||除不尽有小数点|
||//|整除||除不尽保留整数|
||%|取余||除不尽的取余数|
||=|赋值|
||==|判断是否相等|
||<>|不等于|
||<|小于|
||>|大于|
||<=|小于等于|
||>=|大于等于|
||运算优先级|()指数乘除加减|
||round|四舍五入|round()|
|格式控制符|%s|将字符/字符串数据显示给用户|
||%d|将整数数据显示给用户|
||%r|将所有内容显示给用户||多用于调试|
|转义字符|\\|将难打印的字符打印出来|\'单引号 \"双引号 \\反斜杠
||\a|ASCII响铃|
||\b|ASCII退格|
||\f|ASCII进纸|
||\n|ASCII换行|
||\r|ASCII回车|
||\t|ASCII水平制表TAB|
|用户输入|input()
|参数|argv|将值传入文件中的变量，用于获取文件名|from sys import argv/script，file = argv|多变量，值个数要等于变量个数
||*argv|多参数变量|用于赋值，不用于文件传参



