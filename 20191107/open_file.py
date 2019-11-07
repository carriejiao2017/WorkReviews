from sys import argv
#将要取值的文件名通过参数传入
script, filename = argv
#打开文件
txt = open(filename)
#输出读入文件的文件名
print("Here`s your file %r:" % filename)
print (txt.read()) #读取文件内容
txt.close()

print("Type the filename again:")
#再次输入文件名，通过用户input方式
file_again = input(">")
#打开文件
#txt.again = open(file_again)
#读取文件
#print(txt.again.read())
#txt.again.close()

# 在输入时打开文件
print(file_again)
