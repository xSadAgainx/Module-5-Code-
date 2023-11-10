import time
# name of list
slist = []

# Printed commmands for user
print('Commands: \n '
      'check / c - Checks current list \n'
      'remove / r - Remove an Item from the list \n'
      'Quit / q - Quit & Exit Script \n'
      '[Anything else you type will be added to the list]')

# While Loop statement for List function and to add items of any kind with the included function to check the list

while True:
    addlist = input('\n >>> ')
    slist.append(addlist)

    # - Check Function
    if addlist == 'check':
        slist.remove('check')
        for element in slist:
            print('- ', element)
    elif addlist == 'c':
        slist.remove('c')
        for element in slist:
            print('- ', element)
    # - Check Function

    # - Remove Function
    elif addlist == 'remove':
        slist.remove('remove')
        for element in slist:
            print('- ', element)
        Remove = input('Remove item and Item \n'
                       '>>> ')
        if Remove in slist:
            slist.remove(Remove)
        else:
            print('This Items does not seem to be in your list')
    elif addlist == 'r':
        slist.remove('r')
        for element in slist:
            print('- ', element)
        Remove = input('Remove item and Item \n'
                       '>>> ')
        if Remove in slist:
            slist.remove(Remove)
    elif addlist =='quit':
        print('Quiting Program, Goodbye ...')
        time.sleep(3)
    else:
        print('This Items does not seem to be in your list')
    # - Remove Function