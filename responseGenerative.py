import spacy

nlp = spacy.load('en')
doc = nlp("where is my car parked")

# Print Adv
def printAdv(tree):
    for node in tree:
        if(node.dep_ == 'ROOT'):
            printSubject(node.children)
            printVerbPass(node.children)
            print(node.dep_, node.text)
            print('-------')
            printVerb(node.children)
            printObject(node.children)
            printPrep(node.children)

# Print Attr
def printAttr(tree):
    for node in tree:
        if(node.dep_ == 'ROOT'):
            printSubject(node.children)
            printVerbPass(node.children)
            print(node.dep_, node.text)
            print('-------')
            printVerb(node.children)
            printObject(node.children)
            printPrep(node.children)

# Print Dative
def printDative(tree):
    for node in tree:
        if(node.dep_ == 'ROOT'):
            printObject(node.children)
            printPrep(node.children)
            
# Print Subject
def printSubject(tree):
    for node in tree:
        if(node.dep_ == 'nsubj' or node.dep_ == 'nsubjpass' or (node.dep_ == 'compound' and node.pos_ == 'NOUN') or (node.dep_ == 'amod' and node.head.pos_ == 'NOUN')):
            printDetPoss(node.children)
            printSubject(node.children)
            print(node.dep_, node.text)
            print('-------')
            printPrep(node.children)
        elif(node.dep_ == 'ccomp'):
            printSubject(node.children)

# Print Verb
def printVerb(tree):
    for node in tree:
        if(node.dep_ == 'ccomp' or node.dep_ == 'acl'):
            print(node.dep_, node.text)
            print('-------')
        elif(node.dep_ == 'nsubj' or node.dep_ == 'nsubjpass'):
            printVerb(node.children)

# Print Verb
def printVerbPass(tree):
    for node in tree:
        if(node.dep_ == 'auxpass' or node.dep_ == 'aux'):
            print(node.dep_, node.text)
            print('-------')

# Print Object
def printObject(tree):
    for node in tree:
        if(node.dep_ == 'pobj' or node.dep_ == 'dobj'):
            printDetPoss(node.children)
            print(node.dep_, node.text)
            print('-------')
            printPrep(node.children)

# Print Det/Poss
def printDetPoss(tree):
    for node in tree:
        if(node.dep_ == 'det' or node.dep_ == 'poss'):
            print(node.dep_, node.text)
            print('-------')

# Print Prep
def printPrep(tree):
    for node in tree:
        if(node.dep_ == 'prep'):
            print(node.dep_, node.text)
            print('-------')
            printObject(node.children)

def printResponse(doc):
    for node in doc:
        if(node.dep_ == 'adv' or node.dep_ == 'advmod'):
            print('Mode: Adv')
            printAdv(doc)
        elif(node.dep_ == 'attr'):
            print('Mode: Attr')
            printAttr(doc)
        elif(node.dep_ == 'dative'):
            print('Mode: Dative')
            printDative(doc)

printResponse(doc)

for node in doc:
    print(node.text, node.dep_, node.pos_,
          [child.dep_ for child in node.children])