# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
# where every other element of the input tuple is copied, starting with the first one. 
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
# then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    """aTup: a tuple
    returns: tuple, every other element of aTup.
    """
    i = 0
    secondTuple = ()
    for index in aTup:
        if i % 2 == 0:
            secondTuple += (index,)
        i += 1

    return secondTuple

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))
