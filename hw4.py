#hw4.py, collaborator: Vi-Anh Nguyen


#-------------due Oct 11 11:59pm

#5.15
def vowels(vS):
    vSl = list(vS)#makes string into list
    for i in range(len(vSl)):
        if vSl[i] in 'aeiouAEIOU':
            print(i)
            
#5.16--needs work
def indexes(wdS,s):
	inLst=[]
	for i in range(len(wdS)):
		#print(i,wdS[i])
		if wdS[i]==s:
			inLst.append(i)
	return inLst
            
#5.18
def four_letter(wdLst):
    for j in range(len(wdLst)):
        for i in wdLst:
            if len(i) !=4:
                wdLst.remove(i)
    return wdLst

#5.26
def rps(p1,p2):
    p1=p1.upper()
    p2=p2.upper()
    if p1=='R':
        if p2=='R':
            return(0)
            
        elif p2=='P':
            return(1)
        else:
            return(-1)
    if p1=='P':
        if p2=='R':
            return(-1)
        elif p2=='P':
            return(0)
        else:
            return(1)
    if p1=='S':
        if p2=='R':
            return(1)
        elif p2=='P':
            return(-1)
        else:
            return(0)

#5.39--needs work
def exclamation(wd):
    n_wd=wd
    t=''
    for i in wd:#goes through the list
        if i in 'aeiouAEIOU':#look for the vowel
            if  wd.count(i)>4:
                t= t+i
                #wd=wd.replace(t,nv)
                #print('loop '+i)
            else:
                nv=i*4
                wd=wd.replace(i,nv)
    return wd+'!'

#doctest

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))

