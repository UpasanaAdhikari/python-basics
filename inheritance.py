# #inhertance
# #single

# class employee:
#     def __init__(self): #parent class
#         print("hello")


# class person(employee):  #child class
#     def show(self):
#         print("my name is upa")


# per=person()
# per.show()



# #multiple

# try:
#     class A:
#         def aa(self):
#             print("this is from class A")

#     class B:
#         def show(self):
#             print("this is from class B")

#     class C(A,B):
#         def show1(self):
#             print("this is from class C")

#     per = C()
#     per.show()
    
# except:
#     print("error")



# #multilevel
# try:
#         class A:
#             def met1(self):
#                 print("hello i am from class A")
        
#         class B(A):
#             def met2(self):
#                 print("hello i am from class B")

#         class C(B):
#             def met3(self):
#                 print("hello i am from class C")

#         obj1=C()
#         obj1.met1()
#         obj1.met2()
#         obj1.met3()

# except:
#     print("error")    



# #hierachial
# try:
#     class parent:
#         def meth1(self):
#             print("I am parent class")

#     class child1(parent):
#         def meth2(self):
#             print("I am child 1 class")

#     class child2(parent):
#         def meth3(self):
#             print("I am child 2 class")

#     obj = child1()
#     obj.meth1()
#     obj.meth2()
#     obj1 = child2()
#     obj1.meth1()
#     obj1.meth3()
# except:
#     print("error")



x = int(input("Enter number of days: "))
days = []
temp = []

for i in range(x):
    days1 = input("Enter day " )
    temp1 = int(input("Enter temperature for day "))
    days.append(days1)
    temp.append(temp1)











































