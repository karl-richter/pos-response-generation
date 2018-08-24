import spacy
from spacy.lang.en.examples import sentences
from spacy import displacy

def invertPerson(obj):
    if "my" in obj:
        return obj.replace("my","your")
    else:
        return obj

nlp = spacy.load('en_core_web_sm')
doc = nlp("The Google")

print(doc.text)
#for token in doc:
#    if(token.pos_ == 'VERB' or token.pos_ == 'NOUN'):
#        print(token.text,  "Index:",token.i,  "Pos:",token.pos_,  "Norm:",token.norm_,  "Dep:",token.dep_,  "Shape:",token.shape_, "TokenIsAlpha:", token.is_alpha, "TokenIsStop:", token.is_stop)


for ent in doc.ents:
    print(ent.text, ent.label_)
    #for token in ent:
        #print(token.text)

# Next week DATE
# Madrid GPE

#for chunk in doc.noun_chunks:
#     print(chunk.text, "RootText:", chunk.root.text, "RootDep:", chunk.root.dep_, "RootHeadText:", chunk.root.head.text)

#trees = doc.print_tree()
#print(trees[0])

#Displacy to create a graph out of the text https://spacy.io/usage/visualizers
#options = {'compact': True, 'bg': '#09a3d5', 'color': 'white', 'font': 'Source Sans Pro'}
#displacy.serve(doc, style='dep', options=options)