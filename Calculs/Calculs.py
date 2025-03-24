import numpy as np
import matplotlib.pyplot as plt
#import requests
#import panda as pd
import csv


avogadroConstant = 6.02214076e23
gazParfaitsConstant = 8.31446261815324
gravityConstant = 9.81

FichierBilanMasse = "Bilandemasse.csv"
masseTotale = 0 #kg

temperatureAmbiante = 20 #°C
temperatureAmbiante+=273.15 #K
pression = 1.01325e5 #Pa

masseAtomique = 4.002602 * 1.6605402e-27 #kg



masseMolaireAir = (28.0134 * 0.7808 + 31.9988 * 0.2095 + 39.948 * 0.0093 + 20.1797 * 0.000018 + 44.0095 * 0.0004 + 16.0425 * 0.00000187)*(10**-3)
print(masseMolaireAir)

masseVolumiqueAir = (masseMolaireAir * pression)/(gazParfaitsConstant * temperatureAmbiante) #kg/m3

dicTotal = {}
with open(FichierBilanMasse, newline="", encoding="utf-8") as fichier:
    bilanMasse = csv.DictReader(fichier)
    
    for ligne in bilanMasse:
        for labels in ligne.keys() :
            if ligne[labels] == "None" or labels == "label" or ligne["label"] == "ballast" :
                None
                #print(ligne["label"])
            elif ligne[labels] == "calc" :
                if labels == "Masse (kg)" :
                    ligne[labels] = float(ligne["masse volumique (kg/m3)"]) * float(ligne["Volume (m3)"])
                if labels == "masse volumique (kg/m3)" :
                    ligne[labels] = float(ligne["Masse (kg)"]) / float(ligne["Volume (m3)"])
                if labels == "Volume (m3)" :
                    ligne[labels] = float(ligne["Masse (kg)"]) / float(ligne["masse volumique (kg/m3)"])
            else :
                ligne[labels] = float(ligne[labels])
        #print(ligne["Masse (kg)"],ligne["nombre"])
        if ligne["label"] != "ballast" :
            masseTotale+= ligne["Masse (kg)"] * ligne["nombre"]
        #print(ligne)
        dicTotal[ligne["label"]] = ligne

#print(masseTotale)

masseAirDeplace = masseVolumiqueAir * dicTotal["envellope"]["Volume (m3)"]

masseRestante = masseAirDeplace - masseTotale

print("Masse utilisé : ", masseTotale, "\nMasse d'air déplacé : ", masseAirDeplace, "\nMasse restante pour les ballasts : ", masseRestante)