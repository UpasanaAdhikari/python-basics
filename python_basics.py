x=[1,3,5,7,9,10,2,4,12]
sum=0
for i in x:
    if i%2==0:
        sum += i
        
    else:
        pass
print(sum)



x=[1,3,5,7,9,10,2,4,12]

def add(x):
    sum=0
    for i in x:
        if i % 2 == 0:
            sum += i
    return sum
       
     
result = add(x)
print(f'the answer is :{result}')



        