#    linguistic-extractor
#    Copyright (C) 2022  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import yaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
    
    

from tkinter import *
from tkinter.ttk import *

import tkinter 
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox

from TBXTools import *

import codecs

def select_corpus():
    infile = askopenfilename(initialdir = ".",filetypes =(("text files", ["*.txt"]),("All Files","*.*")),
                           title = "Choose an input file.")
    E1.delete(0,END)
    E1.insert(0,infile)
    E1.xview_moveto(1)
    
def select_output_file():
    outfile = asksaveasfilename(initialdir = ".",filetypes =(("text files", ["*.txt"]),("All Files","*.*")),
                           title = "Choose a output file to store the term candidates.")
    E2.delete(0,END)
    E2.insert(0,outfile)
    E2.xview_moveto(1)
    
def go():
    stream = open('config-linguistic-extractor.yaml', 'r',encoding="utf-8")
    config=yaml.load(stream,Loader=Loader)
    project_name=config['project_name']
    lang=config['lang']
    patterns=config["POS_patterns"]
    min_freq=int(config["min_freq"])
    show_frequency=config["show_frequency"]
    
    entrada=codecs.open(patterns,"r",encoding="utf-8")
    n_min=1000000
    n_max=0
    
    for linia in entrada:
        linia=linia.rstrip()
        camps=linia.split(" ")
        nactual=len(camps)
        if nactual<n_min: n_min=nactual
        if nactual>n_max: n_max=nactual
    
    extractor=TBXTools()
    extractor.create_project(project_name,lang,overwrite=True)
    corpus=E1.get()
    extractor.load_sl_tagged_corpus(corpus)
    extractor.load_linguistic_patterns(patterns)
    extractor.tagged_ngram_calculation(nmin=n_min,nmax=n_max,minfreq=min_freq)
    extractor.linguistic_term_extraction(minfreq=min_freq)
    outfile=E2.get()
    extractor.save_term_candidates(outfile, minfreq=min_freq, show_frequency=show_frequency)


top = Tk()
top.title("Linguistic Extractor")

B1=tkinter.Button(top, text = str("Corpus file"), borderwidth = 1, command=select_corpus,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E1.grid(row=0,column=1)

B2=tkinter.Button(top, text = str("Candidates file"), borderwidth = 1, command=select_output_file,width=14).grid(row=1,column=0)
E2 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E2.grid(row=1,column=1)

B5=tkinter.Button(top, text = str("GO!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=2,column=0)

top.mainloop()
