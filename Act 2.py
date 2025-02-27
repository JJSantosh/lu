l1=[12,3,78,456,9,200,461,789,999]
print(l1)

sum=0
for i in l1:
    sum=sum+i
print("sum:",sum)

avg=sum/len(l1)
print("avg:",avg)

l1.sort()
print("sorted list",l1)
print("The least number is:",l1[0])
print("The highest number is:",l1[-1])
