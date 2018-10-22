from __future__ import print_function
import time
from botocore.vendored import requests
import json

doc = []
reply = []
replyTwo = []

# BEGIN NLP with Google NLP API
def createDoc(input):
    url = "https://language.googleapis.com/v1/documents:analyzeSyntax?fields=tokens&key=AIzaSyCiKlJDOlJUoCrHoChThAKKKy44VD2SDpg"
    text = input
    payload = {'document':{'content':text,'language':'EN','type':'PLAIN_TEXT'},'encodingType':'UTF8'}
    headers = {'Content-Type':'application/json'}
    r = requests.post(url = url, data = json.dumps(payload), headers = headers) 
    data = r.json()
    i = 0
    for token in data["tokens"]:
        doc.append({'index': i, 'rel':token["dependencyEdge"]["headTokenIndex"], 'dep_': token["dependencyEdge"]["label"], 'pos_': token["partOfSpeech"]["tag"], 'text': token["text"]["content"], 'children': []})
        i = i + 1
    for node in doc:
        if not node["dep_"] == "ROOT":
            doc[node["rel"]]["children"].append(node)
# END NLP with Google NLP API

# BEGIN NLP with POS
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
        elif(node["dep_"] == 'NSUBJ' or node["dep_"] == 'NSUBJPASS'):
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
# END NLP with POS

# BEGIN NLP with NER
# Print Adv
def printAdvNER(tree):
    advLocation = "located"
    advCar = "car"
    for node in tree:
        if(node["pos_"] == 'VERB' and node["dep_"] == 'CCOMP'):
            advLocation = node["text"]
        elif(node["pos_"] == 'NOUN' and node["dep_"] == 'NSUBJPASS'):
            advCar = node["text"]
    replyTwo.append("Your " + advCar + " is " + advLocation + " at")

# Print Attr
def printAttrNER(tree):
    attrLocation = "location"
    attrCar = "car"
    for node in tree:
        if(node["pos_"] == 'NOUN' and node["dep_"] == 'NSUBJ'):
            attrLocation = node["text"]
        elif(node["pos_"] == 'NOUN' and node["dep_"] == 'NSUBJPASS'):
            attrCar = node["text"]
    replyTwo.append("The " + attrLocation + " of your " + attrCar + " is")

# Print Dative
def printDativeNER(tree):
    dativeLocation = "location"
    dativeCar = "car"
    for node in tree:
        if(node["pos_"] == 'VERB' and node["dep_"] == 'CCOMP'):
            dativeLocation = node["text"]
        elif(node["pos_"] == 'NOUN' and node["dep_"] == 'POBJ' or node["dep_"] == 'COMPOUND'):
            dativeCar = node["text"]
    replyTwo.append("The " + dativeLocation + " of your " + dativeCar + " is")
# END NLP with NER

def printResponse(doc):
    for node in doc:
        if(node["dep_"] == 'ADV' or node["dep_"] == 'ADVMOD'):
            print('Mode: Adv')
            printAdv(doc)
            printAdvNER(doc)
            break
        elif(node["dep_"] == 'ATTR'):
            print('Mode: Attr')
            printAttr(doc)
            printAttrNER(doc)
            break
        elif(node["dep_"] == 'DATIVE'):
            print('Mode: Dative')
            printDative(doc)
            printDativeNER(doc)
            break
        elif(node["dep_"] == 'DOBJ'):
            print('Mode: Dative Object')
            printDativeObj(doc)
            printDativeNER(doc)
            break


for node in doc:
    print(node["text"], node["dep_"], node["pos_"],
          [child["dep_"] for child in node["children"]])

print('-------')
print(' '.join(reply), '...')

def lambda_handler(event, context):
    createDoc(event["queryStringParameters"]['question'])
    time.sleep(0.5)
    printResponse(doc)
    answer = (' '.join(reply))
    answer = answer[0].title() + answer[1:] + ' 309 N Pastoria Avenue.'
    answerTwo = (' '.join(replyTwo)) + ' 309 N Pastoria Avenue.'
    reply.clear()
    replyTwo.clear()
    doc.clear()
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*", 
        },
        "body": json.dumps({"pos": answer, "ner": answerTwo})
    }