# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:56:25 2020

@author: minel
"""
import matplotlib.image as pltimg
import graphviz
from sklearn.tree import export_graphviz
from subprocess import call
import collections
import pickle
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image as imagee
from PIL import *
from PIL import ImageTk
from tkinter import *
import untitled0
from HoverInfo import HoverInfo
#import pyautogui
import urllib.parse
import io

def toplevel():
    
    top = Toplevel()
    top.title('Parameter Description')
    top.wm_geometry("400x300")
                    
    favc=ttk.Label(top,text="Favc = Frequent consumption of high caloric food ")
    favc.grid(row=0,column=0,sticky=tk.W)
                    
    fcvc=ttk.Label(top,text="Fcvc  Frequency of consumption of vegetables")
    fcvc.grid(row=1,column=0,sticky=tk.W)
                    
    ncp=ttk.Label(top,text="Ncp = Number of main meals")
    ncp.grid(row=2,column=0,sticky=tk.W)
                    
    caec=ttk.Label(top,text="Caec = Consumption of food between meals")
    caec.grid(row=3,column=0,sticky=tk.W)
                    
    ch20=ttk.Label(top,text="CH20 = Consumption of water daily")
    ch20.grid(row=4,column=0,sticky=tk.W)
                    
    scc=ttk.Label(top,text="SCC = Calories consumption monitoring")
    scc.grid(row=5,column=0,sticky=tk.W)
                    
    faf=ttk.Label(top,text="FAF = Physical activity frequency")
    faf.grid(row=6,column=0,sticky=tk.W)
                    
    tue=ttk.Label(top,text="TUE = Time using technology devices")
    tue.grid(row=7,column=0,sticky=tk.W)
                    
    calc=ttk.Label(top,text="CALC = Consumption of alcohol")
    calc.grid(row=8,column=0,sticky=tk.W)
    
    mtrans=ttk.Label(top,text="MTRANS = Transportation used")
    mtrans.grid(row=9,column=0,sticky=tk.W)
                    

        
        
        