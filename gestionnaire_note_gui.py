from tkinter import *
from tkinter import messagebox

class Gestion:
    def __init__(self, FRAME):
        self.root = FRAME    
        
        # ANALYSE 2
        Label(FRAME, text="ANALYSE 2:").pack(pady=5 , anchor='w')
        self.analyse = Entry(FRAME)
        self.analyse.pack(anchor='w')

        # ALGEBRE 2
        Label(FRAME, text="ALGEBRE 2:").pack(pady=5 ,anchor='w')
        self.algebre = Entry(FRAME)
        self.algebre.pack(anchor='w')

        # ALGORITHME ET PROGRAMMATION C 2L
        Label(FRAME, text="ALGORITHME ET PROGRAMMATION C 2:").pack(pady=5 ,anchor='w')
        self.algo = Entry(FRAME)
        self.algo.pack(anchor='w')

        # PROGRAMMATION WEB 1
        Label(FRAME, text="PROGRAMMATION WEB 1:").pack(pady=5 ,anchor='w')
        self.web = Entry(FRAME)
        self.web.pack(anchor='w')

        # python 2
        Label(FRAME, text="PYTHON 2:").pack(pady=5 ,anchor='w')
        self.python = Entry(FRAME)
        self.python.pack(anchor='w')

        # TRAITEMENT DE SIGNAL
        Label(FRAME, text="TRAITEMENT DE SIGNAL :").pack(pady=5 ,anchor='w')
        self.trm = Entry(FRAME)
        self.trm.pack(anchor='w')

        # DIGITAL SKILLS
        Label(FRAME, text="DIGITAL SKILLS:").pack(pady=5 ,anchor='w')
        self.dg = Entry(FRAME)
        self.dg.pack(anchor='w')
        # bouton calculer 
        btn1 = Button(FRAME , text="Calculer ",command=self.action_bouton ,bg="green" ,fg="white")
        btn1.pack(pady = 5 ,anchor='w')
        # bouton initialiser 
        btn2 = Button(FRAME , text="initialiser ", command=self.reset ,bg="green" ,fg="white")
        btn2.pack(pady = 5 ,anchor='w')
        # afichage de moyenne et les notes 
        self.label_resultat = Label(root, text="", font=("Arial", 12, "bold") ,bg="#3D5F72" ,fg="black" ,bd=2)
        self.label_resultat.pack()
    # methode pour calculer le moyenne
    def caclculer_moyenne(self):
        try :
            d = {}
            module =["analyse 2 ","algebre 2 ","algorithme et prgrammation c 2","programmation web 1 ","programmation python 2 ","traitement de sighal ","digital de skils" ]
            if (0<=float(self.analyse.get()) <= 20 and 0<=float(self.algebre.get()) <= 20 and 0<=float(self.algo.get()) <= 20 and 0<=float(self.trm.get()) <= 20 and 0<=float(self.web.get()) <= 20 and 0<=float(self.python.get()) <= 20 and 0<=float(self.dg.get()) <= 20):
                note = []
                n_analyse = float(self.analyse.get())
                n_algebre = float(self.algebre.get())
                n_algo = float(self.algo.get())
                n_trm = float(self.trm.get())
                n_python = float(self.python.get())
                n_dg = float(self.dg.get())
                n_web = float(self.web.get())
                total = n_analyse + n_algebre + n_algo + n_trm + n_python + n_dg + n_web
                m = total/7
                note.append(n_analyse)
                note.append(n_algebre)
                note.append(n_algo)
                note.append(n_web)
                note.append(n_python)
                note.append(n_trm)
                note.append(n_dg)
                for i in range(len(module)):
                    d[module[i]] = note[i]
                affichage = ""
                s ="V"
                for i in d :
                    if d[i]<5 :
                        etat = "NV"
                    elif 5<=d[i]<10 :
                        etat = "AC"
                    else :
                        etat = "V"
                    affichage += f"{i}: {d[i]} || {etat}\n"
                    if (d[i]<5 and m >= 10) or (m<10) :
                        s = "NV"
                        continue
                resultat_final = affichage + f"\n----------------\nLe moyenne est = {m:.2f} et semstre {s}"
                self.label_resultat.config(text=resultat_final)
            else :
                messagebox.showerror("Error", "sahbi dakhal no9ta shiha !")
        except:
            messagebox.showerror("Error", "Dkhl ar9am shiha b rojola!")
    
    
    # pour rinialiser les champ
    def reset(self):
        self.analyse.delete(0, END)
        self.algebre.delete(0, END)
        self.algo.delete(0, END)
        self.trm.delete(0, END)
        self.web.delete(0, END)
        self.python.delete(0, END)
        self.dg.delete(0, END)
        self.label_resultat.config(text="")
    # les commandes pours les bouton
    def action_bouton(self):
        self.caclculer_moyenne()
if __name__ == "__main__":
    root = Tk()
    root.title("Gestionnaire de note S2")
    root.geometry("720x600") 
    root.configure(bg="#27F5D3")
    main_frame = Frame(root, bg='#CCF527', bd=1)
    main_frame.pack(side=LEFT ,anchor='nw', padx=10, pady=10)
    app = Gestion(main_frame)
    root.mainloop()