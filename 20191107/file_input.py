from sys import argv
script, user_name = argv
# 定义一个提示符，让用户知道要键入信息
prompt = "%"

print("Hi %s, I am the %s script." % (user_name, script))
print("I`d like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("How old are you, %s?" % user_name)
## ??输入浮点数不能强制转换成整数吗？
age = int(input(prompt))
print("""
Alright, so you said %r about liking me.
You live in %r.
And you have a %r computer.Nice.
And you are %d years old.
""" % (likes, lives, computer, age))