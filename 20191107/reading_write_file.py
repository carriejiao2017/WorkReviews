from sys import argv
script, filename = argv

print("We are going to erase %r." % filename)
print("If you don`t want that, hit CTRL-C.")
print("If you do want that, hit ENTER")

input(">")

print("Opening the file...")
#增加w，是为了在安全环境中写入文件，如无w，则不可写入
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate() #truncate()用法如果用w打开文件，是否还需要用truncate

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I`m going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#可以多段直接写入，采用print的形式利用格式化字符和转义符
target.write("This is lin1: %r\nThis is line2: %r\nthis is line3: %r\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()
