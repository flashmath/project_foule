import tkinter as tk


class Root(tk.Tk):
    def __init__(self,map):

        tk.Tk.__init__(self)

        self.largeur = 600  # largeur et hauteur en pixels
        self.title('Déplacement')

        vue = FenetrePrincipale(self, self.largeur)
        self.modele = map
        vue.toile.modele = map

        vue.toile.initialisation_graphique()


class FenetrePrincipale(tk.Frame):
    """Fenetre principale qui contiendra le menu et la toile (canvas)"""

    def __init__(self, parent, largeur):
        tk.Frame.__init__(self, parent)
        #self.grid()
        self.parent = parent #la root

        self.toile = Toile(largeur, self)
        self.toile.grid(row=0,column=1, sticky = 'E')
        self.focus_set()

        #Menu du dessus
        menubar = tk.Menu(self.parent)
        editmenu = tk.Menu(menubar, tearoff=0)
        trucmenu = tk.Menu(menubar, tearoff=0)

        #editmenu.add_command(label = "Réinitialiser", command = (lambda:self.toile.reset(self)))

        editlabels = ["Charger", "Sauvegarder", "bouger"]

        #lie les items du menu avec la methode menu_appel ci dessous
        for lab in editlabels:
            editmenu.add_command(label = lab, command = (lambda lab = lab:self.menu_appel(lab)))


        self.menubar = menubar
        menubar.add_cascade(label="Édition", menu=editmenu)
        menubar.add_cascade(label="Trucs", menu=trucmenu)

        #montrer le menu
        self.parent.config(menu=menubar)


    def menu_appel(self, event):
        """methode a modifier pour les differents items du menu"""
        if event == "bouger":
            self.parent.modele.move()


class Element_vue:

    def __init__(self, toile, modele):
        self.observe = modele
        self.toile = toile

        xcentre, ycentre, cote = toile.conversion_coord(modele.pos)

        self.x = xcentre-cote
        self.y = ycentre-cote
        self.cote = 2*cote

        print(str(self.x)+' '+str(self.y))

        self.tk_cle = self.toile.create_oval(self.x,self.y,self.x+self.cote,self.y+self.cote, fill='red')
        modele.attach_observateur(self)



    def mise_a_jour(self):
        self.x = self.observe.pos.x-5
        self.y = self.observe.pos.y-5
        self.toile.update()

class Toile(tk.Canvas):
    def __init__(self, largeur, parent):
        tk.Canvas.__init__(self, width=largeur, height=largeur, bg="Gray80", confine=True)
        self.modele = None  #mis à jour par Root
        self.parent = parent  #fenetre principale
        self.cles_tk = []
        self.largeur = largeur

    def initialisation_graphique(self):
        """initialisation des carres initiaux
        On sauvegarde une liste des clés des objets polygones"""

        for c in self.modele.elements:
            self.cles_tk.append( Element_vue(self, c) )

    def conversion_coord(self, c):
        """conversion coordonnées modèle vers tk"""
        xcentre = c.x * self.largeur / 10.0
        ycentre = c.y * self.largeur / 10.0
        cote = self.largeur / 20
        return xcentre+cote, ycentre+cote, cote
