import spacy
from nltk import Tree


nlp = spacy.load('en')
trees = []

class TreeObject:
    text = ""
    count = 0
    examples = []
    def __init__(self, text, count, example):
        self.text = text
        self.count = count
        self.examples = []
        self.examples.append(example)
    def foundDublicate(self, example):
        self.count += 1
        self.examples.append(example)

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

# Detect unique trees
for doc in docs:
    # Check whether a tree already exist in trees
    for sent in doc.sents:
        treeAlreadyExists = False
        for tree in trees:
            treeAlreadyExists = False
            if tree.text == to_nltk_tree(sent.root):
                treeAlreadyExists = True
                tree.foundDublicate(sent.text)
        # If a tree does not exist yet - add tree to trees
        if not treeAlreadyExists:
            trees.append(TreeObject(to_nltk_tree(sent.root), 1, sent.text))

# Print all objects in trees (unique detected trees)
for tree in trees:
    print('')
    tree.text.pretty_print()
    print('Count: ', tree.count)
    for example in tree.examples:
        print('Example: ', example)
    print('')
    print('----------------------------')

print('Total number of questions:', len(docs))
print('Number of unique questions:', len(trees))