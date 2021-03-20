n=int(input("enter no.of employees:"))
d={}
max=0
min=10**8
for i in range(n):
    key=input("enter Goodies :")
    value=int(input("Enter price :"))
    d[key]=value     #Intializing value to its key
[print(key,':',value) for key,value in d.items()]
print(d)
for  Key,Value in d.items():
     if value>max:   #finding the max values
         max=value
     if value<min:   #finding the min values
         min=value
print("the difference between the choosen goodies with highest price  and lowest price is",(max-min)) #sending goodies and prices to the dictionary
                                                     
                  
    