def remove_all(L,e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    remove_list = L[:]  # Create a copy of L to iterate over
    L.clear()  # Clear the original list
    for n in remove_list:
        if e != n:
            L.append(n)


#L = [1, 2, 2, 2]
#remove_all(L,2)
#print(L)  # Example usage    # Output: [1]

def remove_all(L,e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    while e in L:
        L.remove(e)

def remove_all(L,e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    for elem in L:
        if elem == e:
            L.remove(e)
#L = [1, 2, 2, 2]
#remove_all(L,2)
#print(L)    #should print [1]   #INCORRECTLY prints: [1, 2]

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

#L1 = [10, 20, 30, 40]
#L2 = [10, 20, 50, 60]
#remove_dups(L1, L2)
#print(L1)  # Example usage    # Output should be: [30, 40]   #INCORRECTLY prints: [20, 30, 40]

def remove_dups(L1, L2):
    L1_copy = L1[:]  # Create a copy of L1 to iterate over
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

#L1 = [10, 20, 30, 40]
#L2 = [10, 20, 50, 60]
#remove_dups(L1, L2)
#print(L1)   # Example usage    # Output: [30, 40]