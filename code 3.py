# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from math import pi, sqrt
class Geo_Form(metaclass = ABCMeta):
    @abstractmethod
    def perimetre():
        pass

    @abstractmethod
    def surface():
        pass
    
    def decris_toi(self):
        print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(self.nom_figure, self.perimetre(), self.surface()))
        
class Rectangle(Geo_Form):
    try:
        def __init__(self,nom_figure, longue, large):
            self.nom_figure = nom_figure
            self.longue = longue
            self.large = large
        def perimetre(self):
            return 2*self.longue + 2*self.large
        
        def surface(self):
            return self.longue*self.large
    except:
        print("Données non pris en charge")

class Cercle(Geo_Form):  
    try:
        def __init__(self, nom_figure, rayon):
            self.nom_figure = nom_figure
            self.ray = rayon
        def perimetre(self):
            return 2*pi*self.ray
        def surface(self):
            return  pi*(self.ray**2)
    except:
        print("Données non pris en charge")

class Triangle(Geo_Form):
    try:
        def __init__(self,nom_figure, cote_1,cote_2,cote_3):
            self.nom_figure = nom_figure
            self.cote_2 = cote_2
            self.cote_1 = cote_1
            self.cote_3 = cote_3
        def perimetre(self):
            return self.cote_2 + self.cote_1 + self.cote_3

        def surface(self):
            p = self.perimetre()/2
            aire = sqrt(p*(p - self.cote_1)*(p - self.cote_2)*(p - self.cote_3))
            aire = aire.real
            return aire
    except:
        print("Données non pris en charge")
class Carre(Rectangle):
    try:
        def __init__(self,nom_figure, cote):
            Rectangle.__init__(self, nom_figure, cote, cote)
    except:
        print("Données non pris en charge ")

class TriangleRectangle(Triangle):
    try:
        def __init__(self,nom_figure, base, hauteur):
            hyp = sqrt(base**2+hauteur**2)
            Triangle.__init__(self, nom_figure, base, hauteur, hyp)
    except:
        print("Données non pris en charge ")

class GeoFig():  
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        def decris_toi(self):
            for g in self.gGeo_rep:
                print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(g.nom_figure, g.perimetre(), g.surface()))
    except:
        print("Données non pris en charge")