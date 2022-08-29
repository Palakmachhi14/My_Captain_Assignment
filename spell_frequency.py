# defining function
#spell=str(input("Enter string: "))
def most_frequent(string):
    spell=dict()  # Creating dictionary named spell
    for n in sorted(string):
        #n for index
        if n not in spell:
            spell[n]=1
        else:
            spell[n]+=1
        
    print(spell)
#print(most_frequent("abbueguhsnLNI"))
most_frequent(input("Enter string: "))

    
    
    
