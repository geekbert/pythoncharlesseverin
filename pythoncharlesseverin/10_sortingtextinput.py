

print "ENTER TEXT"
words = raw_input('')

exceptions = ['is', 'not', 'this']

# fhand =  open('romeo.txt')

counts  =  dict()
#for  line in fhand:
words =  words.split ()
for  word in words:
    if word not in exceptions:

        counts [word]  =  counts .get(word, 0 ) + 1

lst  =  list()
for  key, val  in counts .items ():
    lst .append( (val, key) )
lst .sort(reverse=True)
for  val, key  in lst [:10] :  # top 10 most common words
    print key , val
