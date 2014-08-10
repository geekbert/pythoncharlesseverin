
counts  =  dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for  name in names:
     if name not in  counts : 
         counts [name]  = 1
     else:
         counts [name]  =  counts [name]  + 1
print counts

print""

print"GET METHOD - not understood"

if name in  counts:
    x = counts [name] 	
else: 	
    x = 0	

x =  counts .get ( name,  0) 	

print x

print""

counts  =  dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for  name in names :
    counts [name]  =  counts .get(name,  0) + 1
print counts


