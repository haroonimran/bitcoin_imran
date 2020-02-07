class MyList:
    
    def __init__(self,integer,count = 0,flag = False):
        self.integer = integer
        self.count = count
        self.flag = flag 


a = [1,1,3,44,2,3,22,44,2]
print(a)

print(len(a))   

b = list()

for i in range(len(a)+1):
    b[i] = MyList(a[i],0,False)

print(a)
print(b)
