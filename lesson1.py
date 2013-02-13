#!/usr/bin/python
from __future__ import unicode_literals

def wait():
    raw_input('\nPress Enter to continue...\n\n')

def simple_types():
    
    # Standard string
    test_string = 'Strings start with \' and end with \'.'
    print test_string
    
    # Let's wait a moment before moving on
    wait()
    
    # Escape characters are needed occassionally
    escapes = 'Notice the escape character is \\.'
    print escapes
    
    # Let's wait a moment before moving on
    wait()

    # Combine strings
    test_string = 'Python cannot combine strings and numbers'
    test_string2 = '...but it can combine strings with \'+\'.'
    print test_string + test_string2
    
    # Let's wait a moment before moving on
    wait()

    # Look at numbers
    test_number = 10
    
    # Try catch - if you expect possible failures
    test_string = 'My test number is '
    try:
        print test_string + test_number
    except:
        print 'I told you.'
        
    # Let's wait a moment before moving on
    wait()

    # But you can cast values
    print test_string + str(10) + '.'
    
    # Let's wait a moment before moving on
    wait()

    # Or, we can use .format to accomplish all casting for all types
    print '{0}{1}.'.format(test_string, test_number)
    
    # Let's wait a moment before moving on
    wait()

    # Play with .format - it will be used a lot
    print '{0}{1} and {1} x {1} = {2}.'.format(test_string, test_number,
        test_number*test_number)

    # Let's wait a moment before moving on
    wait()

    # Let's look at lists
    test_list = []
    test_list.append(test_number)
    test_list.append(test_string)
    test_list.append(test_string2)
    
    # Indexed from zero
    print test_list[0]    
    print test_list[1]    
    print test_list[2]    

    # Let's wait a moment before moving on
    wait()

def for_loops():
    
    # Let's get something to loop through
    test_list = ['Another', 'way', 'to', 'create', 'lists']
    for item in test_list:
        print item
    
    # Let's wait a moment before moving on
    wait()

    # Let's use a for loop to combine the items in the list to a single string
    test_string = ''
    for item in test_list:
        test_string += item + ' '
        
    print test_string + '.'
    
    # Let's wait a moment before moving on
    wait()

    # You noticed the trailing space.  That's not good.
    test_string = ' '.join(test_list) + '.'
    print test_string
    
    # Let's wait a moment before moving on
    wait()

def advanced_types():
    
    # Constants are always ALL_CAPS
    LOCATION = "here"
    TIME = "now"
    
    # Tuples are immutable sequences
    CHOICES = (LOCATION, TIME)
    
    for choice in CHOICES:
        print choice
    
    # Let's wait a moment before moving on
    wait()
    
    # All container types can be embedded
    CHOICES = (
        (LOCATION, 'Here'),
        (TIME, 'Now'),
    )
    
    for choice in CHOICES:
        print choice[1]
        
    # Let's wait a moment before moving on
    wait()
    
    # Avoid "magic numbers"
    CHOICE_VALUE = 1
    for choice in CHOICES:
        print choice[CHOICE_VALUE]

    # Let's wait a moment before moving on
    wait()
    
    # Dictionaries are arguably the most powerful container in Python
    test_dict = {}
    CHOICE_CONSTANT = 0
    for choice in CHOICES:
        test_dict[choice[CHOICE_CONSTANT]] = choice[CHOICE_VALUE]

    # Notice there is no certain order when going through a dictionary
    for item in test_dict:
        print 'test_dict[{0}] = {1}'.format(item, test_dict[item])
        
    # Let's wait a moment before moving on
    wait()
    
    # More with dictionaries
    first_name = 'Rico'
    last_name = 'Cordova'
    phone = '720-984-1569'
    test_dict = {
        'First Name': first_name,
        'Last Name': last_name,
        'Phone': phone,
    }
    
    for item in test_dict:
        print 'test_dict[{0}] = {1}'.format(item, test_dict[item])
        

if __name__ == '__main__':
    
    wait()    
    
    # Simple types
    simple_types()
    
    # Learn to use for loops
    for_loops()
    
    # More advance types
    advanced_types()
