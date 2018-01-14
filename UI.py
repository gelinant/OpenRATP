# CODE TRES FORTEMENT INSPIRÉ PAR https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
# FOR EDUCATING PURPOSES


import filemanager as fm
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

import run


LARGE_FONT= ("Verdana", 12)


class OpenRATP(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Projet OpenRATP")

        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Map, Histo):


            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Bienvenue dans le projet OpenRATP", font=LARGE_FONT)
        label2 = tk.Label(self, text="Projet réalisé par Elie HAIDAMOUS et Antoine GÉLIN dans le cadre du projet Opendata ESIEE Paris", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        label2.pack(pady=10,padx=10)


        if fm.checkfilesondisk() == []:
            button = ttk.Button(self, text="Voir l'histogramme",
                                command=lambda: controller.show_frame(Histo))
            button.pack(pady=10)

            button2 = ttk.Button(self, text="Voir la carte",
                                command=lambda: controller.show_frame(Map))
            button2.pack(pady=10)

            
            

        else:
            label1 = tk.Label(self, text="Les fichiers de données sont manquants. Vous devez les télécharger. \n cela peut prendre un certain temps \n Relancez l'application dès que 'Done' s'affiche dans le terminal ", font=LARGE_FONT)
            label1.pack(pady=10,padx=10)

            button3 = ttk.Button(self, text="Retélécharger les données",
                                command=lambda: fm.downloadmissing())
            button3.pack()







class Histo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Histogramme des stations", font=LARGE_FONT)
        label.pack(pady=10,padx=10)




        button02 = ttk.Button(self, text="Afficher histogramme petites stations semaine",
                            command=lambda: run.buildhisto('se1'))
        button02.pack()
        
        button03 = ttk.Button(self, text="Afficher histogramme grandes stations semaine",
                            command=lambda: run.buildhisto('se2'))
        button03.pack(pady=(0,10))

        button04 = ttk.Button(self, text="Afficher histogramme petites stations weekend",
                            command=lambda: run.buildhisto('we1'))
        button04.pack()
        
        button05 = ttk.Button(self, text="Afficher histogramme grandes stations weekend",
                            command=lambda: run.buildhisto('we2'))
        button05.pack()
        
        button1 = ttk.Button(self, text="Retourner à l'accueil",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10,padx=10)



        









class Map(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Carte des stations", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        button02 = ttk.Button(self, text="Afficher carte semaine",
                            command=lambda: run.buildmap('se'))
        button02.pack()
        
        button03 = ttk.Button(self, text="Afficher carte weekend",
                            command=lambda: run.buildmap('we'))
        button03.pack()

        button1 = ttk.Button(self, text="Retourner à l'accueil",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10,padx=10)       


