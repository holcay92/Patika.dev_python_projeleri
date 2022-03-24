# h.halil olcay
def flatten( list ):
    for item in list:
        if type( item ) == list:
            flatten( item )       # recursive function
        else:
            result.append( item )


if __name__ == '__main__':
    result = []
    flatten( [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5] )
    print( result )