#accumulateSearchIndex.py

#####midterm########## we're in 4th week currently
'''
midterm is week6
-here at usual time.


'''
###########hwqs

#duplicate 4.31
'''
0
>>>duplicate('in.txt')
print out file contents
a string
>>>>>

>>>>>duplicate(in.txt')
print contents without punctuation
>>>>>

>>>>>duplicate('in.txt')
print out contenets, lower case without punctioatio
>>>>>

>>>>>duplicate('in.txt')
>>>print out ist of words[word,word]

>>>duplicate('in)
>>>print out word per line
>>>here
>>>>is
>>>>a
>>>.....

>>>duplicate(.txt)
>>>here1
>>>>is 1
>>>>a1
>>>....
print out word with counts( NEED LIST.COUNT())


>>>>duplciate(.txt)
dulipcate2
dulipcate2

>>>print only duplicate words
>>>duplicate(txt)
duliate2
ducapte2

chaneg it to return True/False, wheter or not you printied someting in the previous
version
(THIS IS S A SEARCH FOR A DUPLICATE WORD, WE WILL TALK ABOUT LATER TONIGHT)
>>>duplicate('Duplicates.txt')
True
'''
#########review iteration
'''
(standard) iteration in python uses iterators, performs a "sequential
assignment"

for item in lst:
for char in string:
for i in range():

make this work:
>>>oddEven([22,33,44])
even
odd
even
'''
def oddEven(numlst):
    for num in numlst:
        if num%2==0:#even
            print('even')
        else:
            print('odd')


#why no use return
#because return terminates the function, hence all loops
#so you cant return multiple times
''' below is no good:
def oddEven(numlst):
    for num in numlst:##return makes things stop HERE, so an if/else with these don't work
        if num%2==0:#even
            return('even')
        else:
            return('odd')
'''

#MAKE SURE A RETURN IN A LOOP WORKS IN CONTEXT
#be caeful about returns in loops




######accumulation##########
'''
>>> #eliminating punctuation
>>> s = 'Hello, how, are you.!?'
>>> s
'Hello, how, are you.!?'
>>> #strings immutable!!!!!!!!!!!!!!
>>> s.replace(',', '' )
'Hello how are you.!?'
>>> s.replace(',', '' )
'Hello how are you.!?'
>>> #doesn't change 2
>>> s = s.replace(',', '' )
>>> a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
'Hello how are you.!?'
>>> #use a loop
>>> for punct in ".,;?!":#########<<==doesn't work if you use new variable
	s= s.replace(punct,'')#helps improve the s var. so this doesn't return to original variable

	
>>> s
'Hello how are you'
>>> for punct in ".,;?!":
	s= s.replace(punct,'')#helps improve the s var. so this doesn't return to original variable
	print(s)

	
Hello how are you
Hello how are you
Hello how are you
Hello how are you
Hello how are you
>>>

'''


##########accumulator pattern########you talk alot about patterns in software engineering

'''
accumulator-compute an accumulated value/statistic/container through iteration. Each
iteration computes a partial/running value for the portion of data already seen.

ex:
sum, product,count, max, min
return multiple item, list, str

four step process:-------------------------------------------------------------
0) set up iteration, visit all items of iterest, write "print"version fisrt
1) intitilaize running value before loop
2)accumulate in the loop
3)return after the loop
'''

'''
make this work:
>>>total([3,12,6,22])
43


running Total 0
3->3
12=>15
6=>22>21
22=>43
43
'''
def total(numlst):
    #step 1-intialize
    runningTotal = 0
    for num in numlst:
        #step 2-accumulate
        runningTotal += num
        # is equivalent to the following
        #runningTotal = runningTotal+num
        
        #print(num, runningTotal)-------didnt need this, just helps to see where you are
    #3-return after loop
    return runningTotal


#############aside: <op>=#############
'''
<var> <op>= <expr>

same as (short hand for)

<var> = <var> <op> <expr>

works with most to all operators

>>>>
in Java, C,C++
the following are equivalent
c=c+1
c+=1

c++ <<<not in python

'''

'''
make this work:
>>>>countNegs([2,-55,99,-23,44,2])
2

count:
'''

def countNegs(numlst):
    #1
    count=0
    #0
    for num in numlst:
        if num<0:
            #print(num)
            #2
            count+=1 #don't print, count!
    #3
    return count


'''
>>>negs([2,-55,99,-23,44,2])
[-55,-23]
'''

def negs(numlst):
    #1
    ans = []
    #0
    for num in numlst:
        if num<0:
            #print(num)
            #2
            ans.append(num)
            print(vars())#pretty useful because prints out ALL variables
            #something may be not what you think it is
    return ans




##########str example
'''
make this work:
>>> punctuation("How, are, you? ! . ")
",,?!."
'''

def punctuation(s):
    puncts = ""
    for char in s:
        #if punctuation
        if char in ".,;!?":
            #print(char)
            puncts +=char
    return puncts



######################counter/indexed/range iteration #########################
'''
idea: instead of iterating over the object directly, instead iterate over the indices of the
object, that is range(len(object))

range(len('apple )) is [0,1,2,3,4]
the range of indices for apple

#standard iteration(iterator)

**loops we've seen before of for i in list:
                                print(list)
    ****uses iterator
    *****much easier
    *****can't avlways avoid indexed iteration
    ****like when you need index/ location information
>>> #indexed ietration
>>> #iterate over indecies
>>> stg='apple'
>>> for i in range(len('apple')):
	print(i, stg[i])

	
0 a
1 p
2 p
3 l
4 e
>>> 

'''



##obvious example
'''
make this work:
>>> vowelIndices('hello, how are you?')
[1,4,...]
'''

###indexed accumulator
def vowelIndices(phrase):
    indicies = []
    for i in range(len(phrase)):
        #if vowel
        if phrase[i] in 'aeiou':
            #print(i, phrase[i])
            indices.append(i)
    return indices


##############search pattern#######
#not explicitly mentioned in book
'''
search pattern looks like the following: can quit(return) early if you find what you're
looking for but can only conclude you did not find it after completing the whole loop.
for
    if
        return
return



make this work:
>>>hasVowel("hello how are you?")
True
>>>>hasVowel("jkfj")
False
>>>>
'''


#search, not indexed
#location not important so index not needed

#v1-BAD, code is wrong because only 1 iteration is performed
#only looks at first character
def hasVowel( s):
    for char in s:
        if char in "aeiou": #found a vowel
            #print(char)
            return True
        else:
            return False

'''
>>> hasVowel('apple')
True
>>> hasVowel('ssss')
False
>>> hasVowel('pear')
False
>>> 
'''

#v2-GOOD version
#second return AFTER LOOP
def hasVowel( s):
    for char in s:
        if char in "aeiou": #found a vowel
            #print(char)
            return True
    #other return outside loop
    return False
        
'''
make this work: return first index of a vowel or -1 if none exists.

>>>firstVowel('hello, how are you')
1
>>>firstVowel('fsgdfgg')
-1
'''

#indexed search
def firstVowel(s):
    for i in range(len(s)):
        if s[i] in 'aeiou': #a vowel
        #print(i,s[i])
            return i
    return -1
    #computer looked through all the data and found nothing "prrof by exhaustion"




###################2d iteration###########
'''lst = [
	['apple','pear','kiwi'],
	['pizza','msg','salt'],
	['cereal, çhips', 'velveeta', 'cookies']
	]
>>> len(lst)
3
>>> lst[2]
['cereal, çhips', 'velveeta', 'cookies']
>>> lst[3][1]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    lst[3][1]
IndexError: list index out of range
>>> lst[1][1][2]
'g'
>>> for row in lst:
	print(row)

	
['apple', 'pear', 'kiwi']
['pizza', 'msg', 'salt']
['cereal, çhips', 'velveeta', 'cookies']
>>> for row in lst:
	#row item by item
	for item in row:
		print(item)

		
apple
pear
kiwi
pizza
msg
salt
cereal, çhips
velveeta
cookies
>>> for row in lst:
	#row item by item
	for item in row:
		print(item, end = ' ')

		
apple pear kiwi pizza msg salt cereal, çhips velveeta cookies 
>>> for row in lst:
	#row item by item
	for item in row:
		print(item, end = ' ')
	print()

	
apple pear kiwi 
pizza msg salt 
cereal, çhips velveeta cookies '''




'''
make this work
>>>contains('kiwi',lst)
True
>>>contains('KiWi,lst)
False
'''

#2d (nested)search
def contains(target,lst2d):
    for row in lst2d:
        for item in row:
            if item==target:
                #print(item)
                return True
    return False


