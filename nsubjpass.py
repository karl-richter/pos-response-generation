import spacy
from spacy.lang.en.examples import sentences
from spacy import displacy

def invertPerson(obj):
    if "my" in obj:
        return obj.replace("my","your")
    else:
        return obj

nlp = spacy.load('en_core_web_sm')
doc = nlp("Where is my car parked?")

 for chunk in doc.noun_chunks:
      print(chunk.text, "RootText:", chunk.root.text, "RootDep:", chunk.root.dep_, "RootHeadText:", chunk.root.head.text, chunk.root.head.pos_)
      if(chunk.root.dep_ == 'nsubjpass'):
          nsubjpass = chunk;
print(invertPerson(nsubjpass.text), nsubjpass.root.head.text, 'at ...')

#Displacy to create a graph out of the text https://spacy.io/usage/visualizers
#options = {'compact': True, 'bg': '#09a3d5', 'color': 'white', 'font': 'Source Sans Pro'}
#displacy.serve(doc, style='dep', options=options)