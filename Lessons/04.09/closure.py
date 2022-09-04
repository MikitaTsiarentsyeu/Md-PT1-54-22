def new_print():
    return print

my_print = new_print()

my_print(1,2,3,4,5,"test",sep=',',end='.\n')

def maker(n):
    def action(x):
        return x ** n
    return action

sq = maker(2)
cube = maker(3)
forth = maker(4)

for i in range(1,6):
    print(sq(i), cube(i), forth(i))


# def maker(n, flag):
#     def action():
#         action1()
#         action2()
#         if flag:
#             action3()
#         for i in n:
#             action4()
#     return action