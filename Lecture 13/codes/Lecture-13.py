def pairwise_div(Lnum, Ldenom):
    """Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    
    Returns a new list whose elements are the pairwise
    division of an element in Lnum by the elemnent in Ldenom
      
    Raise a ValueError Ldenom contains 0. """

    L = []
    #L = [Lnum[i] / Ldenom[i] for i in range(len(Lnum))]
    if 0 in Ldenom:
        raise ValueError("Denominator list contains zero(s)")
    assert len(Lnum) == len(Ldenom), "Lists must be of equal length"
    assert len(Lnum) > 0 and len(Ldenom) > 0, "Lists must be non-empty"

    for i in range(len(Lnum)):
        try:
            L.append(Lnum[i] / Ldenom[i])
        except: 
            raise ValueError("nice message")
    return L
        