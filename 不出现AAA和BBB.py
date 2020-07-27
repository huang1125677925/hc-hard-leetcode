def find(a,b):
    import math
    if a%2==0:
        al=['aa']*(a//2)
    else:
        al=['aa']*(math.ceil(a//2-1))+['a']
        
    if b%2==0:
        bl=['bb']*(b//2)
    else:
        bl=['bb']*(math.ceil(b//2-1))+['b']
    
    i,j=len(al),len(bl)
    if a==0 and b<3:
        return 'b'*b
    if b==0 and a<3:
        return 'a'*a
    
    if a==0 or b==0:
        return ''
    
    
    while i-j>1:
        temp=bl.pop(0)
        if len(temp)==2:
            bl.extend(['b','b'])
        else:
            return ''
        j=len(bl)
        
        
    while j-i>1:
        temp = al.pop(0)
        if len(temp) == 2:
            al.extend(['a', 'a'])
        else:
            return ''
        i = len(al)
        
    
    if len(al)>=len(bl):
        key=len(bl)
    else:
        key=len(al)
    r=''
    for i in range(key):
        r+=(al[i]+bl[i])
        
    if len(al)>=len(bl):
        r+=''.join(al[key:])
    else:
        r+=''.join(bl[key:])
        
    print(r)
    
    
find(1,3)