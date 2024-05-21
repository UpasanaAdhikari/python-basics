################ TUPLE  ############################

# The tuple t1 is defined with four elements: an integer 1, an integer 2, 
# a string "hello", and a float 4.5

t1 = (1, 2, "hello", 4.5)

# The first element of the tuple t1 (which is currently 1) is reassigned to 2

t1[0] = 2  # assigning the value 2 to index 1

# The updated tuple t1 is printed,which will show error

print(t1[1])

print(len(t1)) # shows total length in the tuple



##################### SET ####################################

s1={1,2,3,4}
print(s1)

s1.add(5) #adding value in set
print(s1)

s1.discard(5) #removing value in set
print(s1)

s1.add(4)  #again adding same value which was already there so it won't add again
print(s1)





####################### DICTIONARY ######################

d1 = {"name": "John",
      "age": 30,
      "city": ["New York","chicago","kathmandu"]} # dictionary have { key : value} format 
print(type(d1))
print(d1)  
# Accessing Value by Key
print("Accessing Value by Key: ", d1["name"])
# Updating Value by Key
d1["name"]="Jane"
print("\nUpdating Value by Key: ")
print(d1)

# Adding new item into Dictionary
d1["country"]="USA"
print("\nAdding new item into Dictionary")
print(d1)



l1 = [3,346346,4634,64,6,7,3]
print(l1.sort())


####################### work #################

a=int(input("enter the value of a "))
if a%5==0:
    if a>=5:
        print("correct value ")
else:
    print("incorrect value")


x=int(input("enter a value "))
y=int(input("enter second value "))
if x == y :
    print("they are equal")
elif  x < y:
    print("x is smaller")   
else :
    print("y is smaller")


############################# CONDITIONAL ###########################
l1 = [2, "ram", "a", 90, 10]
for i in l1:
    print(i)  # for loop synatax for i in range


for i in l1:
    if i=="ram":
        continue  #continue yesle ram lai chai skip garxa ani aru print garxa
    print(i)


for i in l1:
    if i=="a":  #break yesle condition meet vaye paxi  print garxa
        break
    print(i)



################# function ###################

def sum( x, y):
    return x + y


a=30
b=40
print(sum(a,b))



first = int(input("enter a number "))
second = int(input("enter second number "))
def multiple(x,y):
    return x+y

















