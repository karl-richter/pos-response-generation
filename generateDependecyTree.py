import spacy
import json
from spacy.lang.en.examples import sentences
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Give me the car location")

trees = doc.print_tree()
dict = trees[0]
json = json.dumps(dict)
f = open("tree.json","w")
f.write(json)
f.close()
print(doc.text)

#Displacy to create a graph out of the text https://spacy.io/usage/visualizers
#options = {'compact': True, 'bg': '#09a3d5', 'color': 'white', 'font': 'Source Sans Pro'}
#displacy.serve(doc, style='dep', options=options)