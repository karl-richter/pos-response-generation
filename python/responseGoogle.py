from __future__ import print_function
#import requests
from botocore.vendored import requests
import json


url = "https://language.googleapis.com/v1/documents:analyzeSyntax?fields=tokens&key=AIzaSyCiKlJDOlJUoCrHoChThAKKKy44VD2SDpg"
text = "what is the location of my car?"
payload = {'document':{'content':text,'language':'EN','type':'PLAIN_TEXT'},'encodingType':'UTF8'}
headers = {'Content-Type':'application/json'}
r = requests.post(url = url, data = json.dumps(payload), headers = headers) 
data = r.json()

doc = []
i = 0

for token in data["tokens"]:
    doc.append({'index': i, 'rel':token["dependencyEdge"]["headTokenIndex"], 'dep_': token["dependencyEdge"]["label"], 'pos_': token["partOfSpeech"]["tag"], 'text': token["text"]["content"], 'children': []})
    i = i + 1

for node in doc:
    if not node["dep_"] == "ROOT":
        doc[node["rel"]]["children"].append(node)


reply = []

# Print Adv
def printAdv(tree):
    for node in tree:
        if(node["dep_"] == 'ROOT'):
            printSubject(node["children"])
            printVerbPass(node["children"])
            print(node["dep_"], node["text"])
            reply.append(node["text"])
            print('-------')
            printVerb(node["children"])
            printObject(node["children"])
            printPrep(node["children"])
            print('MANUAL at')
            reply.append('at')
            print('-------')

# Print Attr
def printAttr(tree):
    for node in tree:
        if(node["dep_"] == 'ROOT'):
            printSubject(node["children"])
            printVerbPass(node["children"])
            print(node["dep_"], node["text"])
            reply.append(node["text"])
            print('-------')
            printVerb(node["children"])
            printObject(node["children"])
            printPrep(node["children"])

# Print Dative
def printDative(tree):
    for node in tree:
        if(node["dep_"] == 'ROOT'):
            printObject(node["children"])
            printPrep(node["children"])
            print('MANUAL at')
            reply.append('at')
            print('-------')

# Print Dative Object
def printDativeObj(tree):
    for node in tree:
        if(node["dep_"] == 'ROOT'):
            printObject(node["children"])
            printPrep(node["children"])
            print('MANUAL is')
            reply.append('is')
            print('-------')


# Invert the person from 1st to 2nd
def changePerson(word):
    if word == 'my':
        return 'your'
    elif word == 'I':
        return 'you'
    else:
        return word

# Print Subject
def printSubject(tree):
    for node in tree:
        if(node["dep_"] == 'NSUBJ' or node["dep_"] == 'NSUBJPASS' or (node["dep_"] == 'COMPOUND' and node["pos_"] == 'NOUN') or (node["dep_"] == 'AMOD' and node.head["pos_"] == 'NOUN')):
            printDetPoss(node["children"])
            printSubject(node["children"])
            print(node["dep_"], changePerson(node["text"]))
            reply.append(changePerson(node["text"]))
            print('-------')
            printPrep(node["children"])
        elif(node["dep_"] == 'CCOMP'):
            printSubject(node["children"])

# Print Verb
def printVerb(tree):
    for node in tree:
        if(node["dep_"] == 'CCOMP' or node["dep_"] == 'ACL'):
            print(node["dep_"], node["text"])
            reply.append(changePerson(node["text"]))
            print('-------')
        elif(node["dep_"] == 'nsubj' or node["dep_"] == 'NSUBJPASS'):
            printVerb(node["children"])

# Print Verb
def printVerbPass(tree):
    for node in tree:
        if(node["dep_"] == 'AUXPASS' or node["dep_"] == 'AUX'):
            print(node["dep_"], node["text"])
            reply.append(changePerson(node["text"]))
            print('-------')

# Print Object
def printObject(tree):
    for node in tree:
        if(node["dep_"] == 'POBJ' or node["dep_"] == 'DOBJ'):
            printDetPoss(node["children"])
            print(node["dep_"], node["text"])
            reply.append(changePerson(node["text"]))
            print('-------')
            printPrep(node["children"])

# Print Det/Poss
def printDetPoss(tree):
    for node in tree:
        if(node["dep_"] == 'DET' or node["dep_"] == 'POSS'):
            print(node["dep_"], changePerson(node["text"]))
            reply.append(changePerson(node["text"]))
            print('-------')

# Print Prep
def printPrep(tree):
    for node in tree:
        if(node["dep_"] == 'PREP'):
            print(node["dep_"], node["text"])
            reply.append(node["text"])
            print('-------')
            printObject(node["children"])

def printResponse(doc):
    for node in doc:
        if(node["dep_"] == 'ADV' or node["dep_"] == 'ADVMOD'):
            print('Mode: Adv')
            printAdv(doc)
        elif(node["dep_"] == 'ATTR'):
            print('Mode: Attr')
            printAttr(doc)
        elif(node["dep_"] == 'DATIVE'):
            print('Mode: Dative')
            printDative(doc)
        elif(node["dep_"] == 'DOBJ'):
            print('Mode: Dative Object')
            printDativeObj(doc)


for node in doc:
    print(node["text"], node["dep_"], node["pos_"],
          [child["dep_"] for child in node["children"]])

print('-------')
print(' '.join(reply), '...')

def lambda_handler(event, context):
    printResponse(doc)

    print('value1: ' + event['key1'])
    print('value2: ' + event['key2'])
    print('value3: ' + event['key3'])
    return event['key3']