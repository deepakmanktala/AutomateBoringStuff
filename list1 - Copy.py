spam = ['apples', 'bananas', 'tofu', 'cats']



def listhello(spam):
    a=''
    for i in range(0,len(spam)):
       if i<(len(spam)-1):
           a=a+spam[i]+','+' '
       else:
           a=a+'and '+ spam[i]
    return a


def listHello(spam):
    a=''
    """
    if (spam[0] !=''):
        a=spam[0]
    else:
        return a
"""
    for i in range(1, len(spam)):
        if (i<len(spam)-1):
            a += ', ' + spam[i]
        else:
            a= a+ ' and ' + spam[i]
    return a

            
        
print(listhello(spam))   
print(listHello(spam))       
       
                   
