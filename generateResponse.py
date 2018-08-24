import json

# Idea behind this algorithm:
# Print all the objects from a Dependency Tree in a given order. The order is the following:
# 1. Subject (incl. possession modifier / determiner)
# 2. (Presposition)
# 3. (Object)
# 4. (Auxiliary)
# 5. ROOT

paths = ['1.json', '2.json', '3.json', '4.json', '5.json', '6.json', 'tree.json']
response = []

def resetVars():
    response = []
    result = ''
    data = ''

# Print a Dependency Tree (outdated - not the right order)
def printChild(child):
    for word in child['modifiers']:
        if(word['modifiers'] == []):
            print(word['word'], word['arc'])
        else:
            printChild(word)
            print(word['word'], word['arc'])

# Replace 1st person with 2rd person for a given input
def invertPerson(obj):
    if "my" in obj:
        return obj.replace("my","your")
    elif "I" in obj:
        return obj.replace("I","you")
    else:
        return obj

# 1. Print poss/det from child if available
# 2. Print self (clausal subject / clausal passive subject / nominal subject / passive nominal subject)
# 3. Print prep from child if available 
def printSubj(child):
    for word in child['modifiers']:
        if 'subj' in word['arc']:
            printDetPoss(word)
            printComp(word)
            response.append(invertPerson(word['word']))
            printPrep(word)

# 1. Print self (prepositional modifier / prepositional clausal modifier)
# 2. Print obj from child if available
def printPrep(child):
    for word in child['modifiers']:
        if 'prep' in word['arc']:
            response.append(word['word'])
            printObj(word)

# 1. Print self (componound of an object / subject)
def printComp(child):
    for word in child['modifiers']:
        if 'compound' in word['arc']:
            printComp(word)
            response.append(word['word'])

# 1. Print poss/det from child if available
# 2. Print self (direct object / indirect object / object of a preposition)
def printObj(child):
    for word in child['modifiers']:
        if 'obj' in word['arc']:
            printDetPoss(word)
            printComp(word)
            response.append(word['word'])

# 1. Print self (invert to 2nd person if necessary)
def printDetPoss(child):
    for word in child['modifiers']:
        if 'det' in word['arc'] or 'poss' in word['arc']:
            response.append(invertPerson(word['word']))

# 1. Print self (auxiliary / passive auxiliary)
def printAux(child):
    for word in child['modifiers']:
        if 'aux' in word['arc']:
            response.append(word['word'])

# 1. Print the ROOT of the Dependency Tree
def printRoot(child):
    response.append(child['word'])

def isSubjectQuestion(child):
    for word in child['modifiers']:
        if 'attr' in word['arc']:
            return(False)
        else:
            return(True)

for path in paths:
    response = []
    with open(path) as json_file:  
        data = json.load(json_file)
        #printChild(data)
        printSubj(data)
        printAux(data)
        printRoot(data)
        printObj(data)
        if(isSubjectQuestion(data)):
            response.append('at')
        response.append('309 N Pastoria Ave.')
        result = ' '.join(response)
        print(result)