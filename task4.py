 # 1.To create odd and even list
list=[10,501,22,37,100,999,87,351]

evenlist=[]
oddlist=[]

for n in list:
   
    if n % 2 == 0:
       evenlist.append(n)

    else:
        oddlist.append(n)

print(evenlist)
print(oddlist)


# 2. To count prime numbers

list=[10,501,22,37,100,999,87,351]

primelist=[]

for i in list:
   
  if i > 1 : 
    for j in range(2,i):
      if i % j == 0:
       break
    else:
       primelist.append(i)
    
    
print(primelist)  
print(len(primelist))  


# 3. Happy numbers









# 4.sum of first and last integer

number = int(input("Enter number"))
first_num=int(str(number)[0])
last_num=int(str(number)[-1])
sum= first_num + last_num
print(sum)


# 5.





# 6. Duplicates in the list

list1=[10,501,22,37,100]
list2=[1,501,2,7,10]
list3=[100,52,10,307,20]

duplicate=[]

for i in range(len(list1)): 
  for j in range(len(list2)):
   if list1[i] == list2[j]:
       
     for k in range(len(list3)):
       if list1[i] == list3[k]:
        duplicate.append(list1[i])
        
print(duplicate)



# 7. First non repeating element in a given list of integers.

list=[100,501,22,87,100,999,87]

for i in list:
 if list.count(i) == 1:
    print(i)
    break  


# 8.      
     
