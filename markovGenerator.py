# coding: utf-8
#
# the top line, above, is important -- 
# in ensures that Python will be able to use this file,
# even in the case you paste in text with unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# hUEY
#


# Sample input:
# d = createDictionary('t.txt')
# generateText(d,#)

# fuction 1:
# creating our dictionary
def createDictionary( filename ):
    """ creating our Dictionary of words from a text file
    """
    f = open(filename)
    text = f.read()
    f.close()

    #create our list of words
    LoW = text.split()
    print("Successfully created dictionary!")
    print("There are", len(LoW), "words.")

    #initialize our dictionary & opening key
    d = {}
    pw = '$'

    #iterate through the new words
    for nw in LoW:
        if pw not in d: d[pw] = [nw]
        else:           d[pw] += [nw]

        #check if the sentence ended there
        if nw[-1] in '!.?':
            pw = '$'
        else:
            pw = nw 

    return d



# fuction 2:
# generating our text
def generateText(d,N):
    
    #initialize to sentence start
    pw = '$'
    import random
    s = ''

    #randomly pick the next word
    for i in range(N):
        nw = random.choice(d[pw])
        s += nw + ' '

        #new sentence case
        if nw[-1] in '!.?':
            pw = '$'
        else:
            pw = nw

    return s