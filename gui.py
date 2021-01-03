# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:14:09 2020

@author: minel
"""
# -*- coding: utf-8 -*-

import matplotlib.image as pltimg
import graphviz
from sklearn.tree import export_graphviz
from subprocess import call
import collections
import pickle
import tkinter as tk
from tkinter import ttk
from PIL import Image as imagee
from PIL import *
from PIL import ImageTk
from tkinter import *
import untitled0
from HoverInfo import HoverInfo
#import pyautogui
import urllib.parse
import io
import descriptionGui

#GUI -----------------------------------------------------------------


class obesityGui:
    def __init__ (self, win):
        
        self.win =win 
        win.title('Obesity Prediction')
        win.wm_geometry("800x550")
        
        self.left_frame = tk.Frame(win, width=200, height=400, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.right_frame = tk.Frame(win, width=650, height=400)
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)
        self.tipwindow = None
        
        self.raw_data = urllib.request.urlopen("https://wallpapercave.com/wp/wp2067516.jpg").read()
        self.im = imagee.open(io.BytesIO(self.raw_data))
        self.resized = self.im.resize((500, 500), imagee.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label1 = Label(self.left_frame, image=self.image)
        self.label1.grid(row=0, sticky=W)
        
        self.label2 = Label(win, text= "Welcome to Body Mass Calculator!", font='Helvetica 10 bold' )
        self.label2.place(x=550, y=40)
        
        #Column 1 
        self.gender = ttk.Label(self.right_frame, text= 'Gender')
        self.gender.grid(row=0,column=0,sticky=tk.W)
        self.comboGender = ttk.Combobox(self.right_frame,width=16)
        self.comboGender['values']= ("Male", "Female")
        self.gender_var = self.comboGender
        self.comboGender.grid(row=0, column=1)
        #Column 2
        self.age=ttk.Label(self.right_frame,text="Age")
        self.age.grid(row=1,column=0,sticky=tk.W)
        self.age_var=tk.DoubleVar()
        self.age_entrybox=ttk.Entry(self.right_frame,width=19,textvariable=self.age_var)
        self.age_entrybox.grid(row=1,column=1)
        #Column 3
        self.height=ttk.Label(self.right_frame,text="Height")
        self.height.grid(row=2,column=0,sticky=tk.W)
        self.height_var=tk.DoubleVar()
        self.height_entrybox=ttk.Entry(self.right_frame,width=19, textvariable=self.height_var)
        self.height_entrybox.grid(row=2,column=1)
        #Column 4 
        self.weight=ttk.Label(self.right_frame,text="Weight")
        self.weight.grid(row=3,column=0,sticky=tk.W)
        self.weight_var=tk.DoubleVar()
        self.weight_entrybox=ttk.Entry(self.right_frame,width=19, textvariable=self.weight_var)
        self.weight_entrybox.grid(row=3,column=1)
        #Column 5
        self.family_hist=ttk.Label(self.right_frame,text="Family_History")
        self.family_hist.grid(row=4,column=0,sticky=tk.W)
        self.comboFamily = ttk.Combobox(self.right_frame,width=16)
        self.comboFamily['values']= ("Yes", "No")
        self.family_hist_var = self.comboFamily
        self.comboFamily.grid(row=4, column=1)
        #Column 6
        self.favc=ttk.Label(self.right_frame,text="Favc")
        self.favc.grid(row=5,column=0,sticky=tk.W)
        self.comboFavc = ttk.Combobox(self.right_frame,width=16)
        self.comboFavc['values']= ("Yes", "No")
        self.favc_var = self.comboFavc
        self.comboFavc.grid(row=5, column=1)
        self.hoverFavc = HoverInfo(self.favc, 'Frequent consumption of high caloric food')
        #Column 7
        self.fcvc=ttk.Label(self.right_frame,text="Fcvc")
        self.fcvc.grid(row=6,column=0,sticky=tk.W)
        self.comboFcvc = ttk.Combobox(self.right_frame,width=16)
        self.comboFcvc['values']= ("Seldom", "Sometimes", "Frequently", "Usually" "Always")
        self.fcvc_var = self.comboFcvc
        self.comboFcvc.grid(row=6, column=1)
        self.hoverFcvc = HoverInfo(self.fcvc, 'Frequency of consumption of vegetables')
        #Column 8
        self.ncp=ttk.Label(self.right_frame,text="Ncp")
        self.ncp.grid(row=7,column=0,sticky=tk.W)
        self.ncp_var=tk.DoubleVar()
        self.ncp_entrybox=ttk.Entry(self.right_frame,width=19, textvariable = self.ncp_var)
        self.ncp_entrybox.grid(row=7,column=1)
        self.hoverNcp = HoverInfo(self.ncp, 'Number of main meals')
        #Column 9
        self.caec=ttk.Label(self.right_frame,text="Caec")
        self.caec.grid(row=8,column=0,sticky=tk.W)
        self.comboCaec = ttk.Combobox(self.right_frame,width=16)
        self.comboCaec['values']= ("Never", "Sometimes", "Frequently", "Always")
        self.caec_var = self.comboCaec
        self.comboCaec.grid(row=8, column=1)
        self.hoverCaec = HoverInfo(self.caec, 'Consumption of food between meals')
        #Column 10
        self.smoke=ttk.Label(self.right_frame,text="Smoke")
        self.smoke.grid(row=9,column=0,sticky=tk.W)
        self.comboSmoke = ttk.Combobox(self.right_frame,width=16)
        self.comboSmoke['values']= ("Yes", "No")
        self.smoke_var = self.comboSmoke
        self.comboSmoke.grid(row=9, column=1)
        #Column 11
        self.ch20=ttk.Label(self.right_frame,text="CH20")
        self.ch20.grid(row=10,column=0,sticky=tk.W)
        self.comboch20 = ttk.Combobox(self.right_frame,width=16)
        self.comboch20['values']= ("Seldom", "Sometimes", "Frequently", "Usually", "Always")
        self.ch20_var = self.comboch20
        self.comboch20.grid(row=10, column=1)
        self.hoverCh20 = HoverInfo(self.ch20, 'Consumption of water daily')
        #Column 12
        self.scc=ttk.Label(self.right_frame,text="SCC")
        self.scc.grid(row=11,column=0,sticky=tk.W)
        self.comboSCC = ttk.Combobox(self.right_frame,width=16)
        self.comboSCC['values']= ("Yes", "No")
        self.scc_var = self.comboSCC
        self.comboSCC.grid(row=11, column=1)
        self.hoverScc = HoverInfo(self.scc, 'Calories consumption monitoring')
        #Column 13
        self.faf=ttk.Label(self.right_frame,text="FAF")
        self.faf.grid(row=12,column=0,sticky=tk.W)
        self.comboFAF = ttk.Combobox(self.right_frame,width=16)
        self.comboFAF['values']= ("Never", "Seldom", "Sometimes", "Frequently", "Usually", "Always")
        self.faf_var = self.comboFAF
        self.comboFAF.grid(row=12, column=1)
        self.hoverFAF = HoverInfo(self.faf, 'Physical activity frequency')
        #Column 14
        self.tue=ttk.Label(self.right_frame,text="TUE")
        self.tue.grid(row=13,column=0,sticky=tk.W)
        self.comboTUE = ttk.Combobox(self.right_frame,width=16)
        self.comboTUE['values']= ("Never", "Seldom", "Sometimes", "Frequently", "Always")
        self.tue_var = self.comboTUE
        self.comboTUE.grid(row=13, column=1)
        self.hoverTUE = HoverInfo(self.tue, 'Time using technology devices')
        #Column 15
        self.calc=ttk.Label(self.right_frame,text="CALC")
        self.calc.grid(row=14,column=0,sticky=tk.W)
        self.comboCalc = ttk.Combobox(self.right_frame,width=16)
        self.comboCalc['values']= ("Never", "Sometimes", "Frequently", "Always")
        self.calc_var = self.comboCalc
        self.comboCalc.grid(row=14, column=1)
        self.hoverCalc = HoverInfo(self.calc, 'Consumption of alcohol')
        #Column 16
        self.mtrans=ttk.Label(self.right_frame,text="MTRANS")
        self.mtrans.grid(row=15,column=0,sticky=tk.W)
        self.comboTrans = ttk.Combobox(self.right_frame,width=16)
        self.comboTrans['values']= ("Automobile", "Motorbike", "Public Transportation", "Bike", "Walking")
        self.mtrans_var = self.comboTrans
        self.comboTrans.grid(row=15, column=1)
        self.hoverTrans = HoverInfo(self.mtrans, 'Transportation used')

        self.DF = untitled0.pd.DataFrame(columns=['Gender','Age','Height','Weight','Family_History',
                               'Favc','Fcvc','Ncp','Caec', 'Smoke', 'CH20', 'SCC',
                               'FAF','TUE','CALC','MTRANS'])
        
        self.Predict_entrybox=ttk.Entry(win,width=25)
        self.Predict_entrybox.place(x=616, y=450)
        
        
        self.Predict_button=ttk.Button(win,text="Predict",command=lambda: self.Output())
        self.Predict_button.place(x=520, y=450)
        
        self.Description_button=ttk.Button(win,text="Show Parameter Descriptions",command=lambda: self.DescriptionWindow())
        self.Description_button.place(x=570, y=490)
        


    global DB
    
    def actionDB(self):
      
        GENDER=self.maleOrFemaleComboBox(self.gender_var)
        #print(GENDER)
        self.DF.loc[0,'Gender']=GENDER
        AGE=self.age_var.get()
        self.DF.loc[0,'Age']=AGE
        HEIGHT=self.height_var.get()
        self.DF.loc[0,'Height']=HEIGHT
        WEIGHT=self.weight_var.get()
        self.DF.loc[0,'Weight']=WEIGHT
        FAMILY_HIST=self.yesOrNoComboBox(self.family_hist_var)
        self.DF.loc[0,'Family_History']=FAMILY_HIST
        FAVC=self.yesOrNoComboBox(self.favc_var)
        self.DF.loc[0,'Favc']=FAVC
        FCVC=self.vegetableAndWaterFrequencyComboBox(self.fcvc_var)
        self.DF.loc[0,'Fcvc']=FCVC
        NCP=self.ncp_var.get()
        self.DF.loc[0,'Ncp']=NCP
        CAEC=self.frequencyComboBox(self.caec_var)
        self.DF.loc[0,'Caec']=CAEC
        SMOKE=self.yesOrNoComboBox(self.smoke_var)
        self.DF.loc[0,'Smoke']=SMOKE
        CH20=self.vegetableAndWaterFrequencyComboBox(self.ch20_var)
        self.DF.loc[0,'CH20']=CH20
        SCC=self.yesOrNoComboBox(self.scc_var)
        self.DF.loc[0,'SCC']=SCC
        FAF=self.physicalActivityFrequencyComboBox(self.faf_var)
        self.DF.loc[0,'FAF']=FAF
        TUE=self.technologyDeviceComboBox(self.tue_var)
        self.DF.loc[0,'TUE']=TUE
        CALC=self.frequencyComboBox(self.calc_var)
        self.DF.loc[0,'CALC']=CALC
        MTRANS=self.transportationComboBox(self.mtrans_var)
        #print(MTRANS)
        self.DF.loc[0,'MTRANS']=MTRANS
        DB= self.DF  
        return DB
    


    def yesOrNoComboBox(self, comboBox):
        a = comboBox.get()
        if(a == 'Yes'):
           return 1
        else:
           return 0
       
    #def hoverMsg(self, x, y, text):
        #mouse = pyautogui.position()
        #if(x == mouse[0] and y ==  mouse[1]):
            #return HoverInfo(self.fcvc, text)
            
       
    def transportationComboBox(self, comboBox):
        a = comboBox.get()
        if(a == 'Automobile'):
           return 0
        elif(a == 'Motorbike'):
           return 1
        elif(a == 'Public Transportation'):
           return 2
        elif(a == 'Bike'):
           return 3
        else:
           return 4
       
    def vegetableAndWaterFrequencyComboBox(self, comboBox):
        a = comboBox.get()
        if(a == 'Seldom'):
           return 1
        elif(a == 'Sometimes'):
           return 1.5
        elif(a == 'Frequently'):
           return 2
        elif(a == 'Usually'):
           return 2.5
        else:
           return 3
       
    def technologyDeviceComboBox(self, comboBox):
        a = comboBox.get()
        if(a == 'Never'):
           return 0
        elif(a == 'Seldom'):
           return 0.5
        elif(a == 'Sometimes'):
           return 1
        elif(a == 'Frequently'):
           return 1.5
        else:
           return 2
       
    def physicalActivityFrequencyComboBox(self, comboBox):
        a = comboBox.get()
        if(a== 'Never'):
            return 0
        elif(a == 'Seldom'):
           return 1
        elif(a == 'Sometimes'):
           return 1.5
        elif(a == 'Frequently'):
           return 2
        elif(a == 'Usually'):
           return 2.5
        else:
           return 3
       
    def frequencyComboBox(self, comboBox):
        a = comboBox.get()
        if(a == 'Never'):
           return 0
        elif(a == 'Sometimes'):
           return 1
        elif(a == 'Frequently'):
           return 2
        else:
           return 3
       
    def maleOrFemaleComboBox(self, comboBox):
        a = comboBox.get()
        if(a == 'Female'):
           return 1
        else:
           return 0
      
    result = ""
    
    def Output(self):
        DB = self.actionDB()    
        output = untitled0.classifier.predict(DB)
        print(DB)
        print(output)
        self.Predict_entrybox.delete(0,'end')
        if output == 0:
            result = 'Insufficient_Weight'
        elif output == 1:
            result = 'Normal_Weight'
        elif output == 2:
            result = 'Obesity_Type_I'
        elif output == 3:
            result = 'Obesity_Type_II'
        elif output == 4:
            result = 'Obesity_Type_III'
        elif output == 5:
            result = 'Overweight_Level_I'
        else:
            result = 'Overweight_Level_II'
        
        self.Predict_entrybox.insert(0,str(result))
        
               
    def DescriptionWindow(self):
        descriptionGui.toplevel()
        
        

win = tk.Tk()
obesityGuiCall = obesityGui(win)
win.mainloop()
