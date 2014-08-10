

data  = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008' 	
atpos = data .find ( '@') 	
print  atpos	
#21	
spacepos = data .find ( ' ', atpos) # first space after atpos 	
print  spacepos	
#31	
host  = data [atpos+1 :  spacepos]	
print  host 	
#uct.ac.za
