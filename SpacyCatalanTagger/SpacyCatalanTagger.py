#    SpacyCatalanTagger
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


from tkinter import *
from tkinter.ttk import *

import tkinter 
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox

import yaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import spacy
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
    corpus=E1.get()
    outfile=E2.get()
    mode="coarse"
    POSmodel_spacy = spacy.load("./ca_core_news_sm")
    entrada=codecs.open(corpus,"r",encoding="utf-8")
    sortida=codecs.open(outfile,"w",encoding="utf-8")
    for linia in entrada:
        linia=linia.rstrip()
        taggedtokens = POSmodel_spacy(linia)
        ttsentence=[]
        for token in taggedtokens:
            form=token.text
            lemma=token.lemma_
            if mode=="fine":
                tag=token.tag_
            elif mode=="coarse":
                tag=token.pos_    
            ttsentence.append(form+"|"+lemma+"|"+tag)
        ttsentence=" ".join(ttsentence)
        sortida.write(ttsentence+"\n")
    entrada.close()
    sortida.close()


top = Tk()
top.title("Spacy Catalan Tagger")

B1=tkinter.Button(top, text = str("Input file"), borderwidth = 1, command=select_corpus,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E1.grid(row=0,column=1)

B2=tkinter.Button(top, text = str("Output file"), borderwidth = 1, command=select_output_file,width=14).grid(row=1,column=0)
E2 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E2.grid(row=1,column=1)

B5=tkinter.Button(top, text = str("POS TAG!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=2,column=0)



top.mainloop()
