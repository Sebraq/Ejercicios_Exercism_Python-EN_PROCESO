rhymes=["the house that Jack built.",
        "the malt that lay in ",
        "the rat that ate ",
        "the cat that killed ",
        "the dog that worried ",
        "the cow with the crumpled horn that tossed ",
        "the maiden all forlorn that milked ",
        "the man all tattered and torn that kissed ",
        "the priest all shaven and shorn that married ",
        "the rooster that crowed in the morn that woke ",
        "the farmer sowing his corn that kept ",
        "the horse and the hound and the horn that belonged to "]
def the_verse(c):
    return 'This is '+''.join([rhymes[i] for i in range(c-1,-1,-1)])
def recite(start_verse,end_verse):
    return [the_verse(i) for i in range(start_verse,end_verse+1)]

#print(the_verse(3))
#print(''.join([rhymes[i] for i in range(4-1,-1,-1)]))
    