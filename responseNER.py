import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
adv = nlp("where is my car located")
attr = nlp("what is the car location")
dative = nlp("give me the vehicle position")

advLocation = 'located'
advCar = 'car'
attrLocation = 'location'
attrCar = 'car'
dativeLocation = 'location'
dativeCar = 'car'

for node in adv:
    print(node.text, node.dep_, node.pos_)
    if(node.pos_ == 'VERB' and node.dep_ == 'ccomp'):
        advLocation = node.text
    elif(node.pos_ == 'NOUN' and node.dep_ == 'nsubjpass'):
        advCar = node.text
print('---------------------')

for node in attr:
    print(node.text, node.dep_, node.pos_)
    if(node.pos_ == 'NOUN' and node.dep_ == 'nsubj'):
        attrLocation = node.text
    elif(node.pos_ == 'NOUN' and (node.dep_ == 'pobj' or node.dep_ == 'compound')):
        attrCar = node.text
print('---------------------')

for node in dative:
    print(node.text, node.dep_, node.pos_)
    if(node.pos_ == 'NOUN' and node.dep_ == 'dobj'):
        dativeLocation = node.text
    elif(node.pos_ == 'NOUN' and (node.dep_ == 'pobj'or node.dep_ == 'compound')):
        dativeCar = node.text
print('---------------------')
print('Your', advCar, 'is', advLocation, 'at...')
print('The', attrLocation, 'of your', attrCar, 'is...')
print('The', dativeLocation, 'of your', dativeCar, 'is...')