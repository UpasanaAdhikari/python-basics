name="upa"
n1=20
print(name+n1) #two diffrent type ko data type concatinate garna mildaina
#but you can run it by adding  a string in front of the variable like this:
print(name+"n1")
#here "+" is used for concatenation



print(a) #yo garna mildaina 
a=20


name="upa"
print(type(name))#data type find garxa
print(name.upper())#upper case ma lanxa


name=input("enter the value ") #by default yesle string linxa
#change to diffrent data tyepe typecasting
name=int(name)#convert into integer
name2=input("Enter another value ")
name2=int(name2)
print(name+name2)



name=input("enter name ")
surname=input("enter surname ")
print(name+" "+surname) #concat string



##########################  LIST  #######################################


l1 = [1, 3, "ram", 'a']
print(type(l1))
print(l1)

l1.append(30)# last pos ma 30 add garxa
print(l1)

l1.insert(1, 'b')# desireable space ma  b add garxa
print(l1)
print(l1[3])

l1[3]='changed_value'#value change garna
print(l1)

print(l1[1:6:2]) #slicing kaha dekhi kaha samma print garne yesma last ma euta xodxa 2 chai step ho

l1 = [1, 2, 3, 40, 30, 50]
even = []
odd = []
for i in l1:
   if i%2==0:
      even.append(i)
      
   else:
      odd.append(i)
     
print(even)
print(odd)
print(even, odd) #you can also print like this


print(l1)

l1.pop(1)#pop le remove garna list bata location linxa
print(l1)

l1.remove(40)#remove le chai value linxa location hoina
print(l1)



##############   TUPLE ###################

l1=(2)  #yo integer ho
print(type(l1))
l2=(2,) #comma halne bitikai tuple hunxa
print(type(l2))












