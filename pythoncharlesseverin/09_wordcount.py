

counts  =  dict()


print 'Enter a line of text:' 
line =  raw_input('')

words = line. split()

print 'Words:', words 

print 'Counting...'
for  word  in words:
    counts [word] = counts .get (word,0) + 1

counts = sorted(counts.items()) 

print 'Counts',  counts 


counts2 = { 'chuck' : 1 , 'fred'  : 42, 'jan': 100} 

counts2  = { 'chuck' : 1 , 'fred'  : 42, 'jan': 100} 
for  key  in counts2: 
    print key , counts2 [key] 
