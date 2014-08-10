

line = 'A lot               of spaces' 
etc  = line.split() 
print etc # ['A', 'lot', 'of', 'spaces'] 

line = 'first;second ;third' 
thing = line.split () 
print thing # ['first;second;third'] 
print len (thing) 
 
thing = line.split (';' ) 
print thing #['first', 'second', 'third'] 
print len (thing)
