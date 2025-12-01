def make_ordered_list(n):
    """n is a positive int
    Returns a list containing all ints in order
    from 0 to n (inclusive)
    """
    ordered_list = []
    for i in range(n + 1):
        ordered_list.append(i)
    return ordered_list
#print(make_ordered_list(5))  # Example usage    # Output: [0, 1, 2, 3, 4, 5]

def remove_elem(L,e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e
    """
    remove_elem_list = []
    for element in L:
        if element != e:
            remove_elem_list.append(element)    
    return remove_elem_list


#L = [1,2,2,2]
#print(remove_elem(L,2))  # Example usage    # Output: [1]

def count_words(sen):
    """ sen is a string representing  a sentence
    Returns how many words are in a (i.e. a word is a
    a sequence of characters between spaces. """
    
    words = sen.split()
    return len(words)

#print(count_words("Hello it's me"))   # Example usage    # Output: 3    

def sort_words(sen):
    """ sen is a string representing  a sentence
    Returns a list containing all the words in sen but
    sorted in alphabetical order."""

    words = sen.split()
    words.sort()
    return words

#print(sort_words("look at this photograph"))   # Example usage    # Output: ['at', 'look', 'photograph', 'this']
