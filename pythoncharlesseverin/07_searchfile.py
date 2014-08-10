
fhand = open('mbox-short.txt')	
for line  in  fhand: 	
       if  line .startswith ('From:') : 	
             print  line



fhand = open('mbox-short.txt')	
for line  in  fhand: 	
       line  = line .rstrip () 	# strips whitespace
       if  line .startswith ('From:') :  
           print line


fhand = open('mbox-short.txt')	
for line  in  fhand: 	
    line  = line .rstrip () 	
    if  not line .startswith ('From:') : 	
        continue # skipping wiht continue # skips lines othe than "from"	
    print  line

print"" 

fhand = open('mbox-short.txt')	
for line  in  fhand: 	
    line  = line .rstrip () 	
    if  not ' @uct.ac.za'  in  line  :  	
        continue 	
    print  line


