import spacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"What is the location of my car")

for token in doc:
    print( token.dep_, token.head.text, token.head.pos_,
          [child for child in token.children])

verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)

def printChildren(token):
    for child in token.lefts:
            printChildren(child)
            print(child.text, 'L')
    for child in token.rights:
            printChildren(child)
            print(child.text, 'R')

for token in doc:
    if token.dep_ == 'ROOT':
        for child in token.lefts:
            printChildren(child)
        print(token.text)
        for child in token.rights:
            printChildren(child)
