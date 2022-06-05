# Spacy German Tagger

## 1. Introduction

This is a simple tagger able to POS tag text files (it is recommended that the text file are segmented). It uses Spacy and the Spacy model de_core_news_sm. The model should be located in the same folder as the program.

The Python version is distributed. You can download to a Windows executable version from http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/SpacyGermanTagger.zip 
(copy the link and paste into your browser)

Download and unzip it and it is ready to use.

If you use the Python version you need a Python v3 interpreter installed in your computer (https://www.python.org/) and you need to install the following prerequisites:

```sudo pip3 install PyYAML spacy```

## 2. Use

The Spacy German Tagger has two tagging modes:

* **Coarse**: uses the Universal POS tags

```
POS	DESCRIPTION
ADJ	adjective
ADP	adposition
ADV	adverb
AUX	auxiliary
CONJ	conjunction
CCONJ	coordinating conjunction
DET	determiner
INTJ	interjection
NOUN	noun
NUM	numeral
PART	particle
PRON	pronoun
PROPN	proper noun
PUNCT	punctuation
SCONJ	subordinating conjunction
SYM	symbol
VERB	verb
X	other
SPACE	space

```
**fine**: uses a more detailed tag set:


To configure the tagger, the file config-spacy-tagger.yaml should be edited in any text editor:

```
mode: coarse
#one of coarse (Universal POS tags) or fine (detailed tags)
```

If you want to use the fine tagset, change the mode to fine.


Once the tagset is choses, you can start the program and the following GUI inteface appears:

![](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/blob/main/SpacyGermanTagger/SpacyGermanTagger.PNG)

The use is very easy:

* With the button **Input file** select the text file to POS tag.
* With the button **Output file** select the path and name of the file that will store the tagged corpus.
* Click the button **POS TAG!** to start the tagging process.
