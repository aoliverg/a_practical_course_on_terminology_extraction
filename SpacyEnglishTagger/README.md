# Spacy English Tagger

## 1. Introduction

This is a simple tagger able to POS tag text files (it is recommended that the text file are segmented). It uses Spacy and the Spacy model en_core_web_sm. The model should be located in the sambe folder as the program.

The Python version is distributed. You can download to a Windows executable version from http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/SpacyEnglishTagger.zip 

Download and unzip it and it is ready to use.

If you use the Python version you need a Python v3 interpreter installed in your computer (https://www.python.org/) and you need to install the following prerequisites:

```sudo pip3 install PyYAML spacy```

## 2. Use

The Spacy English Tagger has two tagging modes:

* **Coarse**: uses the Universal POS tags

```
POS	DESCRIPTION	EXAMPLES
ADJ	adjective	*big, old, green, incomprehensible, first*
ADP	adposition	*in, to, during*
ADV	adverb	*very, tomorrow, down, where, there*
AUX	auxiliary	*is, has (done), will (do), should (do)*
CONJ	conjunction	*and, or, but*
CCONJ	coordinating conjunction	*and, or, but*
DET	determiner	*a, an, the*
INTJ	interjection	*psst, ouch, bravo, hello*
NOUN	noun	*girl, cat, tree, air, beauty*
NUM	numeral	*1, 2017, one, seventy-seven, IV, MMXIV*
PART	particle	*’s, not,*
PRON	pronoun	*I, you, he, she, myself, themselves, somebody*
PROPN	proper noun	*Mary, John, London, NATO, HBO*
PUNCT	punctuation	*., (, ), ?*
SCONJ	subordinating conjunction	*if, while, that*
SYM	symbol	*$, %, §, ©, +, −, ×, ÷, =, :), 😝*
VERB	verb	*run, runs, running, eat, ate, eating*
X	other	*sfpksdpsxmsa*
SPACE	space
```
* fine**: uses a more detailed tag set:
```
	POS	POS_Description	Fine-grained Tag	Description	Morphology	EXAMPLE
0	ADJ	adjective	AFX	affix	Hyph=yes	The Flintstones were a **pre**-historic family.
1	ADJ	adjective	JJ	adjective	Degree=pos	This is a **good** sentence.
2	ADJ	adjective	JJR	adjective, comparative	Degree=comp	This is a **better** sentence.
3	ADJ	adjective	JJS	adjective, superlative	Degree=sup	This is the **best** sentence.
4	ADJ	adjective	PDT	predeterminer	AdjType=pdt PronType=prn	Waking up is **half** the battle.
5	ADJ	adjective	PRP$	pronoun, possessive	PronType=prs Poss=yes	**His** arm hurts.
6	ADJ	adjective	WDT	wh-determiner	PronType=int rel	It’s blue, **which** is odd.
7	ADJ	adjective	WP$	wh-pronoun, possessive	Poss=yes PronType=int rel	We don’t know **whose** it is.
8	ADP	adposition	IN	conjunction, subordinating or preposition		It arrived **in** a box.
9	ADV	adverb	EX	existential there	AdvType=ex	**There** is cake.
10	ADV	adverb	RB	adverb	Degree=pos	He ran **quickly**.
11	ADV	adverb	RBR	adverb, comparative	Degree=comp	He ran **quicker**.
12	ADV	adverb	RBS	adverb, superlative	Degree=sup	He ran **fastest**.
13	ADV	adverb	WRB	wh-adverb	PronType=int rel	**When** was that?
14	CONJ	conjunction	CC	conjunction, coordinating	ConjType=coor	The balloon popped **and** everyone jumped.
15	DET	determiner	DT	determiner		**This** is **a** sentence.
16	INTJ	interjection	UH	interjection		**Um**, I don’t know.
17	NOUN	noun	NN	noun, singular or mass	Number=sing	This is a **sentence**.
18	NOUN	noun	NNS	noun, plural	Number=plur	These are **words**.
19	NOUN	noun	WP	wh-pronoun, personal	PronType=int rel	**Who** was that?
20	NUM	numeral	CD	cardinal number	NumType=card	I want **three** things.
21	PART	particle	POS	possessive ending	Poss=yes	Fred**’s** name is short.
22	PART	particle	RP	adverb, particle		Put it **back**!
23	PART	particle	TO	infinitival to	PartType=inf VerbForm=inf	I want **to** go.
24	PRON	pronoun	PRP	pronoun, personal	PronType=prs	**I** want **you** to go.
25	PROPN	proper noun	NNP	noun, proper singular	NounType=prop Number=sign	**Kilroy** was here.
26	PROPN	proper noun	NNPS	noun, proper plural	NounType=prop Number=plur	The **Flintstones** were a pre-historic family.
27	PUNCT	punctuation	-LRB-	left round bracket	PunctType=brck PunctSide=ini	rounded brackets **(**also called parentheses)
28	PUNCT	punctuation	-RRB-	right round bracket	PunctType=brck PunctSide=fin	rounded brackets (also called parentheses**)**
29	PUNCT	punctuation	,	punctuation mark, comma	PunctType=comm	I**,**me and myself.
30	PUNCT	punctuation	:	punctuation mark, colon or ellipsis		colon **:** is a punctuation mark
31	PUNCT	punctuation	.	punctuation mark, sentence closer	PunctType=peri	Punctuation at the end of sentence**.**
32	PUNCT	punctuation	”	closing quotation mark	PunctType=quot PunctSide=fin	“machine learning**”**
33	PUNCT	punctuation	“”	closing quotation mark	PunctType=quot PunctSide=fin	**””**
34	PUNCT	punctuation	“	opening quotation mark	PunctType=quot PunctSide=ini	**”**machine learning”
35	PUNCT	punctuation	HYPH	punctuation mark, hyphen	PunctType=dash	ML site **-** machinelearningknowledge.ai
36	PUNCT	punctuation	LS	list item marker	NumType=ord	
37	PUNCT	punctuation	NFP	superfluous punctuation		
38	SYM	symbol	#	symbol, number sign	SymType=numbersign	This is hash**#** symbol.
39	SYM	symbol	$	symbol, currency	SymType=currency	Dollar **$** is the name of more than 20 curre…
40	SYM	symbol	SYM	symbol		this is a symbol **$**
41	VERB	verb	BES	auxiliary “be”		Let it **be**.
42	VERB	verb	HVS	forms of “have”		I**’ve** seen the Queen
43	VERB	verb	MD	verb, modal auxiliary	VerbType=mod	This **could** work.
44	VERB	verb	VB	verb, base form	VerbForm=inf	I want to **go**.
45	VERB	verb	VBD	verb, past tense	VerbForm=fin Tense=past	This **was** a sentence.
46	VERB	verb	VBG	verb, gerund or present participle	VerbForm=part Tense=pres Aspect=prog	I am **going**.
47	VERB	verb	VBN	verb, past participle	VerbForm=part Tense=past Aspect=perf	The treasure was **lost**.
48	VERB	verb	VBP	verb, non-3rd person singular present	VerbForm=fin Tense=pres	I **want** to go.
49	VERB	verb	VBZ	verb, 3rd person singular present	VerbForm=fin Tense=pres Number=sing Person=3	He **wants** to go.
50	X	other	ADD	email		example@gmail.com
51	X	other	FW	foreign word	Foreign=yes	Hello in spanish is **Hola**
52	X	other	GW	additional word in multi-word expression		
53	X	other	XX	unknown		
54	SPACE	space	_SP	space		
55		NIL	missing tag			
```
