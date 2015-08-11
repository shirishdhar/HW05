#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    
    try:
        value=float(raw_input('Enter an integer: '))

        
    except:
        print 'Enter only numerals ! '
    else:
        if value%1!=0:
            print 'Floats cannot be even or odd '
            return
        if (value%2==0):
            print 'Even Number! '
        else:
            print 'Odd Number! '
            


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for i in range(1,101):
        if i%10==0:
            print '\t', i, 
        else:
            print '\t', i, 
            


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count=0
    result=0
    check = True
    while check:
        
        try:
            num=raw_input('Enter a number: ')
            numf=float(num)
            result+=numf
            
        except:
            if num=='done':
                if count==0:
                    print "You haven't entered any number. "
                    return
                else:
                    print 'Average is: ' + str(result/count)
                    check = False
            else:
                print 'Wrong Input'
                check = False
            
        else:
            count+=1
    return

        
        
    

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    find_average()
if __name__ == '__main__':
    main()
