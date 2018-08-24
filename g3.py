import spacy
from nltk import Tree


nlp = spacy.load('en')
trees = []

class Object:
    text = ""
    count = 0
    examples = []
    def __init__(self, text, count, example):
        self.text = text
        self.count = count
        self.examples.append(example)
        print('Debug: ', example)
    def foundDublicate(self):
        self.count += 1

docs = [nlp("What is the location of my car"), 
        nlp("Where is my car parked"), 
        nlp("Where is my car"),
        nlp("is my car nearby"),  
        nlp("is my car nearby"),  
        nlp("is the car at home"),
        nlp("is the car at home")]

def tok_format(tok):
    return tok.dep_ + '(' + tok.pos_ + ')'

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(tok_format(node), [to_nltk_tree(child) for child in node.children])
    else:
        return tok_format(node)

for doc in docs:
    #print(doc)
    #[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
    for sent in doc.sents:
        treeAlreadyExists = False
        textInSent = sent.text
        for tree in trees:
            if tree.text == to_nltk_tree(sent.root):
                treeAlreadyExists = True
                tree.foundDublicate()
                print('Found dublicate:', textInSent)
        if not treeAlreadyExists:
            trees.append(Object(to_nltk_tree(sent.root), 1, textInSent))

for tree in trees:
    print(tree.count, ': ', tree.text)
    for example in tree.examples:
        print('Examples: ', example)