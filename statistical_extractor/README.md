# Statistical extractor

## 1. Introduction

This is a simple program to test the capabilities of statistical term extraction. The program has a very simple GUI interface and it is easily configured using a yaml file. The program is distributed in Python version 3 code and in an executable version for Windows. The executable version works in any computer with a recent version of Windows with any other requirement. 

The Windows exe can be downloaded from:http://lpg.uoc.edu/a_practical_course_on_terminology_extraction/statistical-extractor-win.zip

(copy the link and paste into your browser).

Two exe files are provided, one for 64 bits computers (statistical-extractor.exe) and another for 32 bits computers (statistical-extractor-32b.exe).

The Python version works in any computer (Windows, Linux and Mac) with a Python version 3 interpreter installed (https://www.python.org/). For the Python version the following requirements are necessary:

* nltk
* PyYAML
* jieba (only if you need to use the Chinese tokenizer)

The TBXTools.py file should be placed in the same directory as the statistical-extractor.py program.

These requirements can be installed with bapip3

```pip3 install nltk PyYAML jie```

## 2. Use of the program

The terminology extraction can be done using a text file corpus. It's recommended, but not mandatory, that the corpus is segmented. We need also a stop-word list (there are stop word list provided for English, Spanish, Catalan, French and German).

Before using the program, it should be configured editing (in any text editor) the config-statistical-extractor.yaml file. This file has the following contents:

```
project_name: statistical.sqlite
tokenizer: MTUOC_tokenizer_eng
   #tokenizer name or None
lang: en
n_min: 2
n_max: 3
min_freq: 2
stopwords: stop-eng.txt
   # stopwords file or None
inner_stopwords: inner-stop-eng.txt
   # inner stopwords file or None
case_normalization: False
   # True or False
nest_normalization: False
   # True of False
regexp_exclusion: None
   # exclusion file or None
show_frequency: True
   # True of False
```

The **project_name** is the name of the sqlite file that will contain the data. You can keep the default name, but it will be overwritten every time you run the program. 

The **lang** is the ISO code for the language. 

The **n_min** is the minimum order of the n-grams.

The **n_max** is the maximum order of the n-grams.

With the **stopwords** parameter you can specifyt the stop words list to be used. Is very important to indicate a list for the working language. Specify None if you don't want to use any stop words list.

With the **inner_stopwords** parameter you can specifyt the inner stop words list to be used. Specify None if you don't want to use any stop words list.
Set **case_normalization** to True if you want to perform this optional step. False otherwise.

Set **regexp_exclusion** if you want to perform this optional step. False otherwise.

Set **show_frequency** to True if you want to have the frequency values in the list of candidates. False otherwise.

Once we have edited the configuration file we can start the statistical-extractor program and the following interface will show up:

![](https://github.com/aoliverg/a_practical_course_on_terminology_extraction/blob/main/statistical_extractor/statistical_extractor_GUI_interface.PNG)

With the button **Corpus file** the file containing the corpus to use should be selected.

With the button **Candidates file** the path an name of the file that will contain the term candidates should be selected.

To start the extraction process click on the button **GO!**

At the end of the process, the candidates file will contain the term candidates. The frequency of the candidates will be shown it the option **show_frequency** is set to True in the configuration file.

```
3823	health care
2331	public health
2054	World Health
2008	mental health
1900	Health Organization
1813	World Health Organization
1722	Public Health
1581	blood pressure
1519	side effects
1463	clinical trials
1373	immune system
1328	New Zealand
1238	nervous system
1235	breast cancer
1122	commonly used
1072	Medical Center
1069	increased risk
1035	blood cells
965	Drug Administration
935	T cells
918	health insurance
902	risk factors
872	heart failure
857	quality of life
851	blood flow
832	years old
829	heart rate
828	same time
817	Ministry of Health
805	blood vessels
```
