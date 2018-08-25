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

docs = [
nlp("where is my car"),
nlp("where is my car located"),
nlp("where is my car parked"),
nlp("where did I park"),
nlp("what is the location of my car"),
nlp("where is my car"),
nlp("where did I park my car"),
nlp("where is my benz"),
nlp("give me the car location"),
nlp("where is my car"),
nlp("could you please tell me where my car is"),
nlp("where is my car"),
nlp("where are you"),
nlp("where did i park my car"),
nlp("where is my car"),
nlp("where do I find my car"),
nlp("give me the location of my car"),
nlp("where is my car parked"),
nlp("where is my car"),
nlp("where did i park"),
nlp("where did I left my car"),
nlp("where did I park my ride"),
nlp("where did my brother leave my car"),
nlp("where is my car"),
nlp("where is my car"),
nlp("what is the address of my car"),
nlp("where is my car"),
nlp("where is my car by"),
nlp("which address did I park my car at"),
nlp("what is the car location"),
nlp("where did I park my car"),
nlp("where is the car parked"),
nlp("where is the car located"),
nlp("where did I left my car")]

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
        treeIsUnique = True
        for tree in trees:
            if tree.text == to_nltk_tree(sent.root):
                treeIsUnique = False
                tree.foundDublicate(sent.text)
        # If a tree does not exist yet - add tree to trees
        if treeIsUnique:
            trees.append(TreeObject(to_nltk_tree(sent.root), 1, sent.text))

# Print all objects in trees (unique detected trees)
for tree in trees:
    print('')
    tree.text.pretty_print()
    print('Count: ', tree.count)
    for example in tree.examples:
        print('Example: ', example)
    print('String: ', tree.text)
    print('')
    print('----------------------------')

print('Total number of questions:', len(docs))
print('Number of unique questions:', len(trees))