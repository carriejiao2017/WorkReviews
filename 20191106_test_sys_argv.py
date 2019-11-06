from sys import argv
# scritpName, first, sec = argv
# print('here is argv', argv)
# print('this is script name', scritpName)
# print('Here is first',first,'sec is' ,sec)


# def func(a, b):
#     c = a + b
#     return c


# print('chunchun is smart')

# if __name__ == "__main__":
#     ans = func(1, 2)
#     print(ans)

# 设计函数10种传参方式
def read_book(books,days):
    print("I spent %d days reading %d books!" % (books, days))
    print("Great!\n")
    
#直接传数值给参数
read_book(100,10)

#通过变量赋值传参
book = 100
day = 10
read_book(book,day)

#通过变量赋值再做算式传参
read_book(book + 10, day - 2)

#通过用户输入传参
print("请输入你读书的数量：")
book_1 = int(input())
print("请输入你读书的时间：")
day_1 = int(input())
read_book(book_1, day_1)