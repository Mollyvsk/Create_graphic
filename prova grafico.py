import wx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Creagrafico:
    def __init__(self,tipo="pie"):
        """"""  
        self.tipo=tipo
    
    def scegliFile(self):
        f=wx.Frame(None,title="esempio")
        self.pannello=wx.Panel(f,pos=(0,0), size=(600,600))
        bottone_seleziona=wx.Button(self.pannello,label="Scegli", pos=(340, 400))
        #button.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_PLUS, wx.ART_MENU))
        bottone_seleziona.Bind(wx.EVT_BUTTON,self.scegli_file)
        f.SetInitialSize()
        f.Show()
        
        
    
    def scegli_file(self, event):
        """"""
        openFileDialog = wx.FileDialog(self.pannello,"Open", "", "", "CSV FILES (*.csv)|*.csv |All files (*.*)|*.*",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        nome_file=openFileDialog.GetPath()
        openFileDialog.Destroy()
        self.leggi_file(nome_file)
    
    def leggi_file(self,nome_file):
        self.dataframe=pd.read_csv(nome_file)
    
    def disegna(self):
        lista=[]
        for col in self.dataframe.columns:
            lista.append(col)
        colonna1=lista[0]
        colonna2=lista[1]
        labels=self.dataframe[colonna1].tolist()
        print(labels)
        print(lista)
        x=colonna1
        y=colonna2
        dati_numerici=colonna2
        didascalia=colonna1
        print(y)
        if self.tipo == "plot":
            self.dataframe.plot(x,y)
            
        elif self.tipo == "pie":
            self.dataframe.plot.pie(y=y,labels=labels)
            plt.legend()
        plt.show()
            
            
app=wx.App()
c=Creagrafico()
c.leggi_file(prova.csv)
c.disegna()
app.MainLoop()