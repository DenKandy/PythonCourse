#!/usr/bin/python3
#Name: Kandyba Denys
#Date: 04/02/2018
#Purpose: sorting letter in alphabetical order

#FUNCTION
def Sort( array ):
    """
    TODO: sorting number, algoritm 'bubble sort'
    ###* Argument *:
        type of array must be integer and length of array > 1
    ###* Return *:
        sorted list
    """
    length = len( array )
#---check to need sorting or not
    if length == 0 or length == 1:
      return array;
    for i in range(length - 1, 0, -1):
        for k in range(i):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array
def IsLetter(sym):
    """ 
    TODO: Check 'sym' is letter
    ###* Argument *:
        string length must be equal 1
    ###* Return *:
        ##### true: 
            if letter
        ##### false:
            if not letter   
    """
#---check is it symbol
    if len(sym) > 1:
    	return False
#---convert to byte
    code = ord(sym)
#---range [65-90] capital letter, [97-122] small
    if (code > 64 and code < 91) or (code > 96 and code < 123):
        return True
    else:
        return False
def ConvertTo( array, func ):
    """ 
    TODO: Convert array and return him
    ###* Argument *:
        func must return value and have one argument
    ###* Return *:
        array converted by 'func'
    """
#---length of array can be more then 0 if not return him else convert
    if len( array ) == 0:
        return array
    else:
        rlist = []
        for sym in array:
            rlist.append( func( sym ) )
    return rlist
def GetCount():
    """ 
    TODO: Ask user how many letters
    ###* Repeat *:
        if user enter not number or number is less then 2 return TODO again
    ###* Return *:
         integer
    """
#---get number and check
    while True:
       string = input( "Enter count of letters: ")
        try:   
            count = int( string )
#-----------count must be not equal 0 if equal repeat
            if count == 0 or count == 1:
                print("Count of letters can't be equal '%d'" %count)
                continue
#-----------count must be less then 0 if less repeat
            elif count < 0:
                print("Count of letters can't be negative '%d'" %count)
                continue
            return count
#-------if 'string' is not a number repeat
        except:
            print("It is '%s' not a integer" %string)
def GetSymbol( func ):
    """
    TODO: Get symbol which meet the requirements of a func
    ###* Argument *:
        func must return boolean value and have one argument
    ###* Return *:
       string
    ###*Repeat*:
        if symbol which not meet the requirements of a func
        repeat process
    """    
#---get symbol and check him
    while True:
        symbol = input("-> ")
#-------symbol must be length which equal 1 if not again request
        if len( symbol ) != 1:
            print("It is '%s' not one symbol" %symbol)
            continue
#-------symbol must be fill the bill function 'func' if not again request
        elif ( func( symbol ) ):
            return symbol
        else:
            print("It is '%s' not correct symbol" %symbol)
            continue
def IsRepeat():
    """ 
    TODO: Ask user should repeat
    ###* Return *:
        ##### true: 
            if user enter 'yes'
        ##### false:
            if user enter 'no'
    ###* Repeat *:
        if user enter neither 'yes' nor 'no' return TODO again
    """
    while True:
        answer = input("Do you want to repeat? Enter 'yes' or 'no' and press enter \n: ").strip()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("You should enter 'yes' or 'no' ")
#OUTPUT
print("Program wrote by Kandyba Denys\nDate created: 04/02/2018\nPurpose: sorting letters in alphabetical order")
#PROCESS
while True:
    #INPUT
#---get count of letters
    count = GetCount()
#---which letter
    pos = 0
#---array of letters
    beforeSort = []
#---get letters and append them to array
    while count != pos:
        print("Enter the " + str( pos + 1 ) +" letter:")
        letter = GetSymbol( IsLetter )
        beforeSort.append( letter )
        pos += 1
    #PROCESS
#---convert to byte sequence
    codes = ConvertTo( beforeSort, ord )
#---sorting in ascending order
    codes = Sort( codes )
#---convert to letter sequence
    afterSort = ConvertTo( codes, chr )
    #OUTPUT
#---print results
    print( "Before sorting: ")
    print( ", ".join( beforeSort ) )
    print( "After sorting: ")
    print( ", ".join( afterSort ) )
    #INPUT
#---ask should repeat or not
    if not IsRepeat():
        break;
#OUTPUT
print("exit")