# Part-of-Speech for response generation
This repository is part of a research on part-of-speech tagging for NLG.
Spacy.io is used for NLP

Conversations with Voice Assistants aim to become more and more human-like, to ultimately pass the Turing test, where a user cannot distinct between a conversation with a machine and another human anymore.

Currently voice assistant application developers use static responses or template-based responses to respond to requests that users send to their voice assistant applications.

Voice assistant vendors, i.e. Amazon and Google, use more advanced algorithms to generate more human-like responses. Due to a lacking reliability, fully Natural Language Generation (NLG) based approaches for response generation are not implemented in voice assistants yet and still under research.

This study makes use of a phenomena in question answering, called the wh-movement, which is used in everyday language to respond to wh-questions (what, where, why etc.). By repeating most of the question and rearranging the order of words in the answer, humans answer questions in a polite and socially accepted way.

A syntactic-analysis-based algorithm is developed in this study, to generate responses by making use of the wh-movement.
