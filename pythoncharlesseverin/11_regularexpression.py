

import re 	
	
hand = open('mbox-short.txt') 	
for line in hand: 	
    line = line.rstrip()	
    if  re.search('^From:', line)  : 	
        print line 
   
    if re.search('^X.*:', line): 
        print line	
 
    if re.search('^X-\S+:', line):
        print line


x =  'From: Using the :  character'	
y = re.findall('\S+@\S+ ',x)
print y 


lin =  'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 ' 
y = re.findall('^From .*@([^ ]*) ',lin) 
print y


hand = open('mbox-short.txt')
numlist = list() 
for line in hand:
    line = line.rstrip()
    stuff =  re.findall('^X-DSPAM-Confidence:  ([0-9.]+)', line)
    if len( stuff) != 1 :  continue 
    num = float( stuff[0] )
    numlist.append(num) 
print  'Maximum: ', max(numlist)
