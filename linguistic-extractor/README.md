
# Linguistic extractor

## 1. Introduction

This is a simple program to test the capabilities of linguistic term extraction. The program has a very simple GUI interface and it is easily configured using a yaml file. The program is distributed in Python version 3 code and in an executable version for Windows. The executable version works in any computer with a recent version of Windows with any other requirement. 

The Windows exe can be downloaded from: [http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/linguistic-extractor-win.zip](http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/linguistic-extractor-win.zip)]

(copy the link and paste into your browser).

The Python version works in any computer (Windows, Linux and Mac) with a Python version 3 interpreter installed (https://www.python.org/). For the Python version the following requirements are necessary:

* nltk
* PyYAML

The TBXTools.py file should be placed in the same directory as the statistical-extractor.py program.

These requirements can be installed with pip3

```pip3 install nltk PyYAML```

## 2. Use of the program

The terminology extraction can be done using a text file corpus. It's recommended, but not mandatory, that the corpus is segmented. The corpus should be POS tagged. You can use any POS-tagger but it's recommended to use one of the postaggers provided in this course material:

* SpacyEnglishTagger: [https://github.com/aoliverg/a_practical_course_on_terminology_extraction/tree/main/SpacyEnglishTagger](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/tree/main/SpacyEnglishTagger]
* SpacySpanishTagger: [https://github.com/aoliverg/a_practical_course_on_terminology_extraction/tree/main/SpacySpanishTagger](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/tree/main/SpacySpanishTagger)
* SpacyCatalanTagger: [https://github.com/aoliverg/a_practical_course_on_terminology_extraction/tree/main/SpacyCatalanTagger](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/tree/main/SpacyCatalanTagger)

You also need a list of POS patterns, as the ones in this example:

```
|#|NOUN |#|NOUN
|#|ADJ |#|NOUN
|#|NOUN |#|NOUN |#|NOUN
|#|ADJ |#|NOUN |#|NOUN
|#|ADJ |#|ADJ |#|NOUN
|#|NOUN of|of|ADP |#|NOUN
```

Please note that the post patterns are dependent on the language and on the tag set used by the tagger.

Before using the program, it should be configured editing (in any text editor) the config-linguistic-extractor.yaml file. This file has the following contents:

```
project_name: linguistic.sqlite
lang: en
min_freq: 2
POS_patterns: POS-patterns.txt
show_frequency: True
   # True of False
```

The **project_name** is the name of the sqlite file that will contain the data. You can keep the default name, but it will be overwritten every time you run the program. 

The **lang** is the ISO code for the language. 

The **POS_patterns** is the path and name of the file containing the list of POS patterns.

Set **show_frequency** to True if you want to have the frequency values in the list of candidates. False otherwise.

Once we have edited the configuration file we can start the statistical-extractor program and the following interface will show up:

![](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/blob/main/linguistic-extractor/linguistic-extractor.PNG)

With the button **Corpus file** the file containing the corpus to use should be selected.

With the button **Candidates file** the path an name of the file that will contain the term candidates should be selected.

To start the extraction process click on the button **GO!**

At the end of the process, the candidates file will contain the term candidates. The frequency of the candidates will be shown it the option **show_frequency** is set to True in the configuration file.

```
14	world record
13	cell line
12	eicosatetraenoic acid
11	prostate cancer
11	cancer cell
9	external link
9	percent rule
8	second barrier
8	prostate cancer cell
7	arachidonic acid
7	human prostate
6	hepoxilin a3
6	side effect
6	human prostate cancer
5	eicosatrienoic acid
...
```
