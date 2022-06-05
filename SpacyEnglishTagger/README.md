# Spacy English Tagger

## 1. Introduction

This is a simple tagger able to POS tag text files (it is recommended that the text file are segmented). It uses Spacy and the Spacy model en_core_web_sm. The model should be located in the sambe folder as the program.

The Python version is distributed. You can download to a Windows executable version from http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/SpacyEnglishTagger.zip 
(copy the link and paste into your browser)

Download and unzip it and it is ready to use.

If you use the Python version you need a Python v3 interpreter installed in your computer (https://www.python.org/) and you need to install the following prerequisites:

```sudo pip3 install PyYAML spacy```

## 2. Use

The Spacy English Tagger has two tagging modes:

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

```
0	ADJ	adjective	AFX	affix
1	ADJ	adjective	JJ	adjective
2	ADJ	adjective	JJR	adjective, comparative
3	ADJ	adjective	JJS	adjective, superlative
4	ADJ	adjective	PDT	predeterminer
5	ADJ	adjective	PRP$	pronoun, possessive
6	ADJ	adjective	WDT	wh-determiner
7	ADJ	adjective	WP$	wh-pronoun, possessive
8	ADP	adposition	IN	conjunction, subordinating or preposition
9	ADV	adverb	EX	existential there
10	ADV	adverb	RB	adverb
11	ADV	adverb	RBR	adverb, comparative
12	ADV	adverb	RBS	adverb, superlative
13	ADV	adverb	WRB	wh-adverb
14	CONJ	conjunction	CC	conjunction, coordinating
15	DET	determiner	DT	determiner
16	INTJ	interjection	UH	interjection
17	NOUN	noun	NN	noun, singular or mass
18	NOUN	noun	NNS	noun, plural
19	NOUN	noun	WP	wh-pronoun, personal
20	NUM	numeral	CD	cardinal number
21	PART	particle	POS	possessive ending
22	PART	particle	RP	adverb, particle
23	PART	particle	TO	infinitival to
24	PRON	pronoun	PRP	pronoun, personal
25	PROPN	proper noun	NNP	noun, proper singular
26	PROPN	proper noun	NNPS	noun, proper plural
27	PUNCT	punctuation	-LRB-	left round bracket
28	PUNCT	punctuation	-RRB-	right round bracket
29	PUNCT	punctuation	,	punctuation mark, comma
30	PUNCT	punctuation	:	punctuation mark, colon or ellipsis
31	PUNCT	punctuation	.	punctuation mark, sentence closer
32	PUNCT	punctuation	”	closing quotation mark
33	PUNCT	punctuation	“”	closing quotation mark
34	PUNCT	punctuation	“	opening quotation mark
35	PUNCT	punctuation	HYPH	punctuation mark, hyphen
36	PUNCT	punctuation	LS	list item marker
37	PUNCT	punctuation	NFP	superfluous punctuation
38	SYM	symbol	#	symbol, number sign
39	SYM	symbol	$	symbol, currency
40	SYM	symbol	SYM	symbol
41	VERB	verb	BES	auxiliary “be”
42	VERB	verb	HVS	forms of “have”
43	VERB	verb	MD	verb, modal auxiliary
44	VERB	verb	VB	verb, base form
45	VERB	verb	VBD	verb, past tense
46	VERB	verb	VBG	verb, gerund or present participle
47	VERB	verb	VBN	verb, past participle
48	VERB	verb	VBP	verb, non-3rd person singular present
49	VERB	verb	VBZ	verb, 3rd person singular present
50	X	other	ADD	email
51	X	other	FW	foreign word
52	X	other	GW	additional word in multi-word expression
53	X	other	XX	unknown
54	SPACE	space	_SP	space
55		NIL	missing tag			
```

To configure the tagger, the file config-spacy-tagger.yaml should be edited in any text editor:

```
mode: coarse
#one of coarse (Universal POS tags) or fine (detailed tags)
```

If you want to use the fine tagset, change the mode to fine.


Once the tagset is chosen, you can start the program and the following GUI inteface appears:

![](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/blob/main/SpacyEnglishTagger/SpacyEnglishTagger.PNG)

The use is very easy:

* With the button **Input file** select the text file to POS tag.
* With the button **Output file** select the path and name of the file that will store the tagged corpus.
* Click the button **POS TAG!** to start the tagging process.


