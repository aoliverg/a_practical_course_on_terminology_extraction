# POSPatternLearner

## 1. Introduction

This program allows learning a set of POS patterns for term representation from a tagged corpus and a list of known terms. The program is distributed as Pyhton version 3 code (in this repository). A windows executable version is available en the following link:

http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/POSPatternLearner-win.zip

## 2. Use of POSPatternLearner

When the program is started a simple GUI interface is shown:

![](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/blob/main/POSPatternLearner/POSPatterLearner.PNG)

* With the button **Tagged corpus** the corpus containing the tagged corpus can be selected.
* To select the list of known terms you should click the button **Term list**. The term list should be a text file with one term per line.
* To select the output file that will contain the learnt POS patterns, click the button **POSP pattenrs file*.
* TO start the process of learning the POS patterns click the button GO!.

Before performing this process you may want to cnfigure the tool editing the file *config-POSPatternsLearner.yaml*.

```
project_name: learnPOSpatterns.sqlite
lang: en
n_min: 2
n_max: 3
show_frequency: False
   # True of False
representativity: 95
   # a percent between 0 and 100
```

* The **project_name** is the name of the sqlite file that will contain the data. You can keep the default name, but it will be overwritten every time you run the program.
* The lang is the ISO code for the language.
* **n_min** is the minimum *n* for the learnt POS patterns. If we fix it to 2, for example, the lower number of elements of a POS pattern will be 2, regardless the actualm minimum *n* of the terms in the term list file.
*  **n_max** is the maximum *n* for the learnt POS patterns. If we fix it to 3, for example, the upper number of elements of a POS pattern will be 3, regardless the actualm maximum *n* of the terms in the term list file.
*  With the paramenter **show_frequency** we can tell the program to show the frequencies of each POS pattern (if set to True),  or to hide this information (if set to False). If you plan to use the learnt patterns directly into a linguistice terminology extraction program, set it to False.
*  With the parameter **representativity** we can set the percent of the terms of the list present in the tagged corpus that should be represented by the learnt POS patterns. Setting a value lower than 100% avoids to learn POS patterns that represent very few terms.

Once we run the program, in the output file we get something like (this example is for English using a Spacy tagger with coarse tags):

```
|#|ADJ |#|NOUN
|#|ADJ #||NOUN
|#|NOUN |#|ADP |#|NOUN
|#|NOUN #||NOUN
|#|NOUN |#|NOUN
|#|ADJ |#|NOUN |#|NOUN
#||NOUN |#|ADP |#|NOUN
|#|NOUN |#|ADP #||NOUN
#||VERB |#|ADJ |#|NOUN
#||NOUN |#|ADP #||NOUN
|#|ADJ |#|NOUN #||NOUN
```

Please, note that this is a raw list and that we may want to refine it. For example, the first learnt patter (|#|ADJ |#|NOUN) is the same as the second one (|#|ADJ #||NOUN) but the first one lemmatizest the NOUN.
