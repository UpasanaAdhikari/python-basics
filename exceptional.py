from function import multiple
multiple(20,10,'a','b',name="ram") #yesma multiple arg and arbitrary Keyword Arguments 


a={'name':'Upasana','age':21,'city':'kathmandu'}
print(a['name'])
print(a.get('name'))

#tara name ko satta nam lekhda euta ko eroor auxa arko le none dinxa

print(a['nam']) #yesle error dinxa
print(a.get('nam')) #yesma chai none auxa 


a=int(input("enter the the number to be multiplied "))
b=int(input("Enter the number upto  which it has to be multiply "))
for i in range(1,b):
    print(i*a)



#################### EXCEPTIONAL HANDLING ##################################

try:
    a=20
    print(b)
except:
    print("error is coming")

print("i am kind hearted person")




############################# CLASSES ########################################

class Student:
    def __init__(self):   #constructer
        print("Hello My name is Upasana Adhikari.GIVE ME JOB !!!!!!!!!!!!!!!!!!!")
object = Student()


class Student:
    def __init__(self,name):   #constructer
        self.name = name
        print("My Name Is : ",self.name)
object = Student('Upasana')
object1 = Student('Adhikari')



















