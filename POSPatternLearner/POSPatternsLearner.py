#    PosPatternLearner
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

def select_corpus():
    infile = askopenfilename(initialdir = ".",filetypes =(("text files", ["*.txt"]),("All Files","*.*")),
                           title = "Choose a tagged corpus file.")
    E1.delete(0,END)
    E1.insert(0,infile)
    E1.xview_moveto(1)
    
def select_term_list():
    infile = askopenfilename(initialdir = ".",filetypes =(("text files", ["*.txt"]),("All Files","*.*")),
                           title = "Choose a term list file.")
    E2.delete(0,END)
    E2.insert(0,infile)
    E2.xview_moveto(1)
    
def select_output_file():
    outfile = asksaveasfilename(initialdir = ".",filetypes =(("text files", ["*.txt"]),("All Files","*.*")),
                           title = "Choose an output file to store the learnt POS patterns.")
    E3.delete(0,END)
    E3.insert(0,outfile)
    E3.xview_moveto(1)
    
def go():
    global project_name
    global n_min
    global n_max
    global show_frequency
    global representativity
    
    extractor=TBXTools()
    extractor.create_project(project_name,lang,overwrite=True)
    corpus=E1.get()
    extractor.load_sl_tagged_corpus(corpus)
    termlist=E2.get()
    extractor.load_evaluation_terms(termlist,nmin=n_min,nmax=n_max)
    extractor.tagged_ngram_calculation(nmin=n_min,nmax=n_max,minfreq=1)
    outfile=E3.get()
    extractor.learn_linguistic_patterns(outfile,representativity=representativity, showfrequencies=show_frequency)
    

top = Tk()
top.title("POSPatternsLearner")

B1=tkinter.Button(top, text = str("Tagged corpus"), borderwidth = 1, command=select_corpus,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E1.grid(row=0,column=1)

B2=tkinter.Button(top, text = str("Term list"), borderwidth = 1, command=select_term_list,width=14).grid(row=1,column=0)
E2 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E2.grid(row=1,column=1)

B3=tkinter.Button(top, text = str("POS patterns file"), borderwidth = 1, command=select_output_file,width=14).grid(row=2,column=0)
E3 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E3.grid(row=2,column=1)

B5=tkinter.Button(top, text = str("GO!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=3,column=0)


stream = open('config-POSPatternsLearner.yaml', 'r',encoding="utf-8")
config=yaml.load(stream,Loader=Loader)
project_name=config['project_name']
lang=config['lang']
n_min=int(config["n_min"])
n_max=int(config["n_max"])
show_frequency=config["show_frequency"]
representativity=config["representativity"]

top.mainloop()
