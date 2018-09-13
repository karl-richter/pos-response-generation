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

## Implementation
### Syntactic Analysis
#### Part-of-speech-tagging
### Word Classification
Algorythmic Approach
AI Approach
Text-Vectorization
### Text Generation
#### Template-based-text-generation

## Evaluation

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