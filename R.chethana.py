
n=int(input("enter no of employees")) #entering by the user number of employees
d={}
max=0
min=10**8
for i in range (n):
    key=input("enter Goodies :") #Intializing value to its key
    value=int(input("enter price :"))
    d[key]=value
[print(key,':',value) for key,value in d.items()]
for key,value in d.items():
    if value>max:     #finding the max values
        max=value
    if value<min:     #finding the min values
        min=value
print (" the difference between the chosen goodies with highest and lowestprice is",(max-min)) #sending goodies and prices to the dictionary