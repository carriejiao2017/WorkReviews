from sys import argv

script, input_file = argv
#read([size])从当前位置起读取size个字节，如无size则读完整文件，作用对象是字符串
def print_all(f):
    print(f.read())
#file.seek(offset[, whence]);offset是偏移字节数，whence默认为0——从文件开头读
#whence为1，从当前偏移位置读起；wence为2，从文件末尾读起
#操作成功，返回新的文件位置，失败则返回-1
def rewind(f):
    f.seek(0)
#readline()输出函数中每一行，
#该方法每次读取一行内容，并把指针保留在读完语句的位置。返回对象是字符串,占用内存小
#readlines()则是读取所有行，保存在一个列表中，读取大文件时慎用
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let`s print the whole file:",)

print_all(current_file)

print("Now let`s rewind, kind of like a tape.")

rewind(current_file)

print("Let`s print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

