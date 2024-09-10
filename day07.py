#Write a Python program to get the smallest number from a list.

#min
x=[2,4,10,15,6]
i=0
minimum=x[0]
while i<len(x):
    print(x[i])
    if minimum>x[i]:
       minimum=x[i]
    i+=1
print(f"min:{minimum}")

#max
Write a Python program to get the largest number from a list.
x=[2,4,6,8,10]
i=0
max=0
while i<len(x):
    if max<x[i]:
     max=x[i]
    i+=1
print(f"max:{max}")

#sum
#Write a Python program to sum up all the items in a list.
x=[1,2,3,4,5,6]
i=0
sum=0
while i<len(x):
    print(x[i])
    sum+=x[i]
    i+=1
    print(f"Total :{sum}")



#extend
mark=[10,20,15,25,20,30,45]
mark2=[1,2,3]
mark2.extend(mark)
print(mark2)

#reverse
mark=[10,20,15,25,20,30,45]
mark.reverse()
print(mark)


#count of occurence
sample=[3,2,3,4,3,5,3]
num=int(input("enter a number:"))
i,count=0,0
while i<len(sample):
    if num ==sample[i]:
        count+=1
    i+=1
if count==0:
    print("item not exist")
else:
    print(f"count of {num} is {count}")


sample2=[4,2,4,5]
print(sample2.count(4))
print(sample2.count(10))


mark=[10,20,15,25,20,30,45]
mark.append(99)
print(mark)#[10, 20, 15, 25, 20, 30, 45, 99]
mark.insert(3,88)
print(mark)#[10, 20, 15, 88, 25, 20, 30, 45, 99]
mark.remove(20)
print(mark)#[10, 15, 88, 25, 20, 30, 45, 99]
mark.pop()
print(mark)#[10, 15, 88, 25, 20, 30, 45] 
mark.pop(3)
print(mark)#[10, 15, 88, 20, 30, 45]
mark.sort()
print(mark)#[10, 15, 20, 30, 45, 88]
mark.sort(reverse=True)
print(mark)#[88, 45, 30, 20, 15, 10]

mark2=[1,2,3]
print(mark+mark2)#[88, 45, 30, 20, 15, 10, 1, 2, 3]
mark2.extend(mark)
print(mark2)#[1, 2, 3, 88, 45, 30, 20, 15, 10]
mark2.reverse()
print(mark2)#[10, 15, 20, 30, 45, 88, 3, 2, 1]
