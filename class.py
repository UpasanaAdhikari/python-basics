class class_name:
    def __init__(self , name,age):  #consructor
        self.name=name
        self.age=age
    
    def myfunc(self):  ##method
        print(f"Hello I am {self.name} and my age is {self.age}")

name=input("enter your name ")
age=int(input("enter your age "))

person=class_name(name,age)
person.myfunc()


class ATM:
    def __init__(self,name):
        self.name = name

person=ATM('upa')
print(person.name)



class class_name:
    def __init__(self , name,age):  #consructor
        self.name=name
        self.age=age
    
    def myfunc(self):  ##method
        print(f"Hello I am",self.name,"and my age is",self.age)


person=class_name('upa',22)
person.myfunc()





class song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
        
    def sing_me_a_song(self):
        print(self.lyrics)


happy_bday = song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])  #list
happy_bday.sing_me_a_song()




class ATM:
    def __str__(self):
        return "ram"

person=ATM()
print(person)


class lunch:
    def __init__(self,menue):
        self.menue=menue
    def menue_price(self):
        if self.menue == 'menu 1':
            print("Price 12.00")
        elif self.menue == 'menu 2':
            print('Price 13.40')
        else:
            print("enter again")

Paul=lunch("menu 1")
Paul.menue_price()




class calculator:
        def __init__(self):
              pass
           
        def addition(self,num1,num2):
            return num1+num2
        def multiplication(self,num1,num2):
            return num1*num2
        def division(self,num1,num2):
     
            return num1/num2
        def  subtraction(self,num1,num2):
             return num1-num2
problem=calculator()
while(True):
    try:
        value=int(input("enter 1>add  2>mul   3>div   4>sub   5>exit "))

        if value == 1:
            num1 = int(input("Enter your number :"))
            num2 = int(input("Enter your number :"))
            
            result =  problem.addition(num1,num2)
        elif value == 2:
            num1 = int(input("Enter your number :"))
            num2 = int(input("Enter your number :"))
            
            result =   problem.multiplication(num1,num2)     
        elif value == 3:
            num1 = int(input("Enter your number :"))
            num2 = int(input("Enter your number :"))
                      
            result =  problem.division(num1,num2)     
        elif value == 4:
            num1 = int(input("Enter your number :"))
            num2 = int(input("Enter your number :"))
                            
            result =  problem.subtraction(num1,num2)  
        elif value == 5:
            print("thank u!!!")
            break
        else:
             print(f"Invalid input {value}")

        print(f"The result is {result}")

    except:
        print("An exception occurred")














