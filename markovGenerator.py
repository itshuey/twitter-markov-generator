# coding: utf-8
#
# hUEY
#


# Sample input:
# d = createDictionary('t.txt')
# generateText(d,#)

# fuction 1:
# creating our dictionary
def createDictionary( filename ):
    """ creating our Dictionary from a .txt file
    """
    f = open(filename)
    text = f.read()
    f.close()

    #create our list of words
    wordlist = text.split()
    print("Successfully created dictionary!")
    print("There are", len(wordlist), "words.")

    #initialize our dictionary & opening key
    d = {}
    key = '$'

    #iterate through the new words
    for word in wordlist:
        if key not in d: d[key] = [word]
        else:            d[key] += [word]

        #check if the sentence ended there
        if word[-1] in '!.?':
            key = '$'
        else:
            key = word 

    return d



# fuction 2:
# generating our text
def generateText(d,N):
    
    #initialize to sentence start
    key = '$'
    import random
    output = ''

    #randomly pick the word word
    for i in range(N):
        word = random.choice(d[key])
        output += word + ' '

        #new sentence case
        if word[-1] in '!.?':
            key = '$'
        else:
            key = word

    return output