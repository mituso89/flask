a = list(range(1,100))
b= 0
for i in a:
    if (i%3  and i%5)==False:
        print (i)
        b= b+i

print (b)        
