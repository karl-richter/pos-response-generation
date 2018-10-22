# Evaluating retrieval-based responses in closed-domain voice assistant applications

## Abstract
...

## Introduction
### Problem Scope
Contemporary voice assistants can undestand nearly every intent in natural human language. 
### Challenges
### Previous Approaches
### Overview of Approach
...
### Contributions
### Thesis Outline

## Theoretical Background
### Artificial Intelligence
### Machine Learning
### Neural Networks
### Voice Assistants
#### Speech Recognition (Speech-to-Text)
	Sound - Vectors - Phonetics - Words
#### Natural Language Understanding (Text-to-Intent)
	RNN
#### Natural Language Generation (Intent-to-Response)
#### Speech Synthesis (Response-to-Speech)
	Text - Normalized Text - Phonetics - Waves - Speech
### Linguistics
#### Morphology
Morphology is the study of the internal structure of words and how they are formed and modified. Morphology focuses on how the components within a word (stems, root words, prefixes, suffixes, etc.) are arranged or modified to create different meanings. English, for example, often adds "-s" or "-es" to the end of a noun to make it plural, and a "-d" or "-ed" to a verb to mark it as past tense. The Natural Language API uses morphological analysis to infer grammatical information about the words provided to it.
#### Syntax
Syntax is the study of how the invididual words in a sentence relate to each other. Syntax and morphology work together to convey grammatical relationships, with different languages dividing the labor between them differently. For example, English expresses the past tense morphologically, adding a "-d" or "-ed" to the end of most verbs, and expresses the future tense of a verb by syntactic means, adding the word "will" before a verb as in the sentence "I will get my umbrella." Other languages, however, may (and many do) modify the words directly to create future tense verbs.
#### Parts of Speech
#### Dependency trees
#### English Grammar
Yes/No questions
With question words
Subject/Object questions
https://nlp.stanford.edu/software/dependencies_manual.pdf


## Methodologies

## Related Work
### Generating Topic-Based Chatbot Responses (Swedish research paper 2017)

## Analysis
This paper analyzes two approaches to generate responses for a number of utterances of the intent 'getCarLocation'. The goal of this paper is to evaluate, whether a syntactic-analysis-based-approach for natural language response generation (NLG) in voice assistant applications archives better results, than a template-based approach. The template-based approach for NLG is currently state-of-the-art and used commercial speech applications such as the Google Assistant and Amazon Alexa. Although generating natural language by using a template does not correspond to the scientific definition of NLG (https://www.mitpressjournals.org/doi/pdfplus/10.1162/0891201053630291), that is supported by most linguists. The approach that was develop in this paper combines the stability that is needed for commercial applications and the individuality that comes with generated replies.

### Problem Analysis
Description of current Voice Assistant Response Generation
Provide an example of that
The underlying problem, that the developed syntactic-analysis-based approach aims to solve, is to make the communication between humans and voice assistant applications more natural. To expose the advanced technology that is used in current voice assistants, the 

### Hypothesis
The underlying hypothesis for this research is, that the number of grammatical different utterances for a specific intent are finite and all of these utteranes can be grammatically correct answered by rearranging the parts of speech of the utterance. Therefore, a limited number of people have been asked for different utterances for one specific intent, with the aim to collect a broad variety of different utterances for one intent and identify the grammatical structure of these utterances. These grammatical structures were then rearranged to generate gramatically correct answers and implemented into an algorythm. This algorythm was then tested by a high number of people to measure its accuracy

### Research Setup
#### Intent
The intent that was chosen to be analyzed in this research will be referred to as _GetCarLocation_. An example utterance of the intent can be "What is the location of my car?". The intent can be part of a Voice Assistant application that provides Connected Car services like the _MercedesMe_ skill on Amazon Alexa (reference). _GetCarLocation_ was chosen because the question expects the answer to contain a specific content, in this case an address of a car, that can be answered by a computer system by retrieved data from an API. Apart from that, the question expects the answer to have a certain level of complexity, that is higher than of a yes/no question, but lower than of a question that would require the computer system to understand implicit context. Last, the quesition is not too domain-specific and relevant in every-day life, which makes it easier for Studienteilnehmer to relate to the question and develop individual utterances.

#### User group
To collect a number of utterances to analyze, ... people were asked for each 5 utterances for the intent _GetCarLocation_. The two factors that can have an influence on how a user formulates an intent are the mother-tongue and the previous experience with Voice Assistants. The objects of research that were chosen for the paper had diverse experiences with Voice Assistants and mother-tongues. the befragten ... people, had ... different mother-tongues, including Spanish, German, Russian and Mandarin. \nThe total number of utterances that were collected during the research are 67, out of these ... questions were excluded from the analysis because the do no not match the intent of getting the address of a car, but can be categorized as yes/no questions etc. as yes or no would linguistically be the expected answer.

#### NLP Framework
The NLP Library that was used for this paper is SpaCy. SpaCy is a Python Library by Explosion.ai, a Berlin-based Start-up, that offers neural models for industry-standart NLP and is currently one of the fastest and most accurate syntactic parsers, according to Choi et al. (https://aclweb.org/anthology/P/P15/P15-1038.pdf). SpaCy features word-tagging, syntactic-parsing and named-entity-recognition (NER). The neural model that was used for this project is the small_en_core_web_ model with ... words and a part-of-speech accurcy of 97.04 percent (https://spacy.io/models/en#en_core_web_sm).

#### Evaluation Methodology
The methodology that was used in this paper is crowd-testing, which is an approach to recieve feedback from a high number of people

### Syntactic-analysis-based approach
The syntactic-analysis-based approach is based on syntactic language parsing. Syntax is the formal grammar of a language. In natural language, syntax provides the rules to put together words to form components of sentences and to put together these components to form sentences (http://l2r.cs.uiuc.edu/~danr/Teaching/CS598-05/Lectures/Roxana.pdf). Parsing is the process of analysing a string of symbols, confirming to the rules of a formal grammar (https://en.wikipedia.org/wiki/Parsing). In linguistics, parsing is used to understand the exact meaning of a specific sentence or a word. The methodology of syntactic parsing that is used for this approach is part-of-speech-tagging (POS), that assigns a tag to each word of the sentence, that contains the part (i.e. noun, verb, adverb etc.) and the role (i.e. subject, object etc.) of each word in a sentence.

#### Utterance analysis (create dependecy trees)
Each of the given sample utterances has been processed using SpaCy's syntactic parser. The results have been visualized using Dependency Trees. The processed and tagged version of the question "What is the location of my car?" looks the follwing:
<Image Parsed Sentence (Pos and Dep for each word)>
The dependency tree of the question looks like the following:
<Image Dependency Tree Question>

#### Create aggregated dependecy trees
To prove the underlying hypothesis of this paper, that the number of grammatical different utterances for a specific intent are finite, the generated dependecy trees that are similar have been aggregated into dependecy trees with optional nodes. The basis of these trees are the roles of the words, the words have been ignored and the different parts that a node with a role can have are limited to the options that have been used in the example utterances. The aggregated Dependecy Trees with optional nodes and example utterances are listed below:
<Image Dependecy Trees With Optional Nodes>
The Dependency Trees correlate with the different types of questions and can be identified by the role of the first node. The three different types of question that have been identified are:
- Type 1
- Type 2
- Type 3
The following utterances have been excluded from futher analysis due to Dependecy Trees, that do not correlate with English grammar and are gramatically not correct.
- Excluded Utterances

#### Analyze Question-Answer rearrangement
To prove the second hypothesis of this paper, that questions can be answered grammatically correct by rearrangement of the parts of speech of the question, the parts of speech of individual utterances have been rearranged to generate a valid response. An example of a question-answer pair can be seen in the follwoing:
<Example Question With POS and Answer With POS>
The knowledge that have been gained by rearranging individual utterances have been transferred to the aggregated Dependecy Trees, to develop a universal model for answer rearrangement.
The three developed POS-Answer-Templates can be seen in the following :
<Three POS Answer Templates>

#### Implementation
This chapter briefly summarizes, how the described syntactic-parsing-based approach has been implemented using the SpaCy library in Python.

Part-of-speech-tagging
The part-of-speech-tagging in SpaCy is executed by calling the function nlp(). Before using this this function, the SpaCy library needs to be imported and a language model needs to be loaded:
```import spacy
	nlp = spacy.load('en')
	doc = nlp("where is my car")
```
The tags of each node can then be accessed by the attributes of each node of the document.
```for node in doc:
		print(node.text, node.dep_, node.pos_)
```
Algorythmic Question classification (Type of question)
The four types of questions that are differentiated in this paper are Adverb-Question, Attribute-Question, Dative-Question and Dative-Object-Question. The function looks for the first node in a document that requires any of the arguments and then generates the response, based on the detected type of question.
for node in doc:
```	  if(node.dep_ == 'adv' or node.dep_ == 'advmod'):
            print('Mode: Adv')
            printAdv(doc)
        elif(node.dep_ == 'attr'):
            print('Mode: Attr')
            printAttr(doc)
        elif(node.dep_ == 'dative'):
            print('Mode: Dative')
            printDative(doc)
        elif(node.dep_ == 'dobj'):
            print('Mode: Dative Object')
            printDativeObj(doc)
```
Algorythmic Question-Answer rearrangement
The rearrangement of words of the question to generate a response depends on the detected type of question. For each type of question, the words are printed in a different order. The implementation uses recursive functions to also print child-nodes of nodes. The following function is an example of the implementation for the question-type Adverb-Question:
```def printAdv(tree):
    for node in tree:
        if(node.dep_ == 'ROOT'):
            printSubject(node.children)
            printVerbPass(node.children)
            print(node.dep_, node.text)
            reply.append(node.text)
            print('-------')
            printVerb(node.children)
            printObject(node.children)
            printPrep(node.children)
            print('MANUAL at')
            reply.append('at')
            print('-------')
```
The print functions for the parts of speech do in some cases also print nodes of themselfes, if available. An example of this is the function printObject():
```# Print Object
		def printObject(tree):
    	for node in tree:
        if(node.dep_ == 'pobj' or node.dep_ == 'dobj'):
            printDetPoss(node.children)
            print(node.dep_, node.text)
            reply.append(changePerson(node.text))
            print('-------')
            printPrep(node.children)
```
### Template-based Approach
The template-based approach is based on templates with slots, that are filled to generate a response. The templates are generated manually and need to fit the type of question that the user asks.

#### Slot identification (identify available slots)
The goal of the utterance analysis in the template-based approach is to idetify the available slots in the response, that are later filled with the appropriate content. The more slots a template contains, the less standardized a response seems, but at the same time the response is less  Each of the utterances has been analysed manually to detect slots that can later be filled with dynamic content. Two two slots that have been detected in the analysed utterances are _carSlot_ and _locationSlot_. Not every utterances does contain both of the slots. An example of an utterance with the identified slots can be seen in the follwoing:
<Image utterances with marked slots>

#### Template creation (for different utterances)
Based on the first hypothesis of this paper, that the number of grammatical different utterances for a specific intent are finite, the same aggregation of the utterances into types of questions have been transferred from the syntactic-analysis-based approach. The three different types of question that have been identified are:
- Type 1
- Type 2
- Type 3
For each of the three types of question, each one template has been created, that is a grammatically correct answer for each of the utterances. Then three templates that have been created are:
- Template 1
- Template 2
- Template 3
Due to the fact, that not every question contains both of the identified slots, univeral fallback values for both of the slots have been used for the implementation. The fallback values for both of the utterances are:
- Fallback Slot 1
- Fallback Slot 2

#### Implementation
Algorythmic slot identification (NER)
Ideally, a custom Named-Entity-Recognition model for the two slots would have been implemented. 

Algorythmic template selection (Type of question)
For the template selection, the same algorythm, that has been developed in the syntactic-analysis-based approach, was reused to select a template based on the type of question. The implementation of the algorithm looks like the following: 
```	  if(node.dep_ == 'adv' or node.dep_ == 'advmod'):
            print('Mode: Adv')
            printAdv(doc)
        elif(node.dep_ == 'attr'):
            print('Mode: Attr')
            printAttr(doc)
        elif(node.dep_ == 'dative'):
            print('Mode: Dative')
            printDative(doc)
        elif(node.dep_ == 'dobj'):
            print('Mode: Dative Object')
            printDativeObj(doc)
```

### Preparation for Evaluation
Host Python Backend on AWS Lambda
Recieve JSON Get-Requests from Website
Saven incoming Request-Body in Database (AWS S3)
Generate two Responses
Send Response back to Front-end
Recieve Follow-up with same Request ID from User (Which Response is better)
(requestID, question, questionType, responseSA, responseT, SAisBetterResponse)

FrontEnd in JS
Send and Recieve Calls from Backend on AWS

## Evaluation
#### Algorithm testing with given utterances
#### Evaluate algorithm based on new user question (2AFC)
-> use SWOT for result summary & conclusion

## Conclusion
...
### Outlook



---
## Definitions
### NLP
Refers to all systems that work together to handle end-to-end interactions between machines and humans in the preferred language of the human. In other words, NLP lets people and machines talk to each other “naturally.”
### NLU
Handle unstructured inputs that are governed by poorly defined and flexible rules and convert them into a structured form that a machine can understand and act upon.
---
### Hypothesis
Contemporary voice assistants use artificial intelligence and neural networks to retrieve the intent of a users question or command. Current voice assistant applications are build to respond with one predefined static response, based on the intent that the application receives. The subject of this research is to implement and evaluate a retrieval-based model that selects the best fitting response from a set of pre-defined responses based on the detected intent as well as the wording of the language of the user.

---
### Useful Links
https://cloud.google.com/natural-language/docs/morphology