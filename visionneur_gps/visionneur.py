"""
Lycée Saint-André :: 1NSI
Mini-projet GPS/CSV
"""

# Librairies nécessaires
import csv
import math
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox  
import tkintermapview  # A installer : python3 -m pip install tkintermapview    

 

# Variable globale contenant toutes les données
fichier = fd.askopenfilename()
parcours = []
position_carte = []
latitude_max = -90.0
latitude_min = 90.0
longitude_max = -180.0
longitude_min = 180.0



"""  code """

# Lecture des données
with open(fichier) as csvfile:  # ouverture du fichier csv choisit
    reader = csv.DictReader(csvfile, delimiter=';') 
    for row in reader:  # séparation en listes 
        row['latitude'] = float(row['latitude'])
        row['longitude'] = float(row['longitude'])
        row['altitude'] = float(row['altitude'])
        row['cardio'] = float(row['cardio'])
        parcours.append(row)
        position_carte.append((row["latitude"], row["longitude"]))
    
    # recherche des max et min pour les latitudes et longitudes
    for position in parcours:
        position["latitude"]
        if position["latitude"] > latitude_max:
            latitude_max = position["latitude"]
        if position["latitude"] < latitude_min:
            latitude_min = position["latitude"]
        position["longitude"]
        if position["longitude"] > longitude_max:
            longitude_max = position["longitude"]
        if position["longitude"] < longitude_min:
            longitude_min = position["longitude"]


''' Calculs '''

# tableau latitude / longitude /  fréquence cardiaque / Altitude / heures
lat = []
long = []
card = []
alt = []
heures_entieres = []
for row in parcours:
    lat.append(float(row["latitude"]))
    long.append(float(row["longitude"]))
    card.append(int(row["cardio"]))
    alt.append(float(row["altitude"]))
    heures_entieres.append(row["heure"])


# calcul de temps
temps = []
for v in parcours:
    temps.append(v['heure'].split(":"))

temps_en_seconde = []
t = 0
for loop in temps:
    heures = int(temps[t][0]) * 3600
    minutes = int(temps[t][1]) * 60
    secondes = int(temps[t][2]) * 1
    temps_en_seconde.append(heures + minutes + secondes)
    t = t + 1


''' Graphique '''

# creer fenettre tkinter
root_tk = Tk()
root_tk.geometry(f"{1400}x{975}")   # taille de l'écran de la salle d'NSI
root_tk.title("map.py") # affichage de la carte

# creer map 
map_widget = tkintermapview.TkinterMapView(root_tk, width=1400, height=925, corner_radius=0)    # taille de la fenettre 
map_widget.grid(column=0, row=0)

# cadrer la carte
map_widget.fit_bounding_box((latitude_max, longitude_min), (latitude_min, longitude_max))   


# mettre un géomarqueur et tracer
marker = map_widget.set_marker(lat[0], long[0], text_color = "#000000", marker_color_circle = None, marker_color_outside = "#6600C5", text="Départ")    # géomarqueur
map_widget.set_path(position_carte, width = 2,color ="#6600C5")     # tracer


# gérer le curseur
def gerer_curseur(evenement):
    position = int(evenement)
    p = position
    marker.set_position(lat[p],long[p])
    

    # calcul de distance
    distance_tot = 0
    for curseur in range(1,p):
        dist = 6378 * math.acos(math.sin(math.radians(lat[curseur-1]))* math.sin(math.radians(lat[curseur])) \
            + math.cos(math.radians(lat[curseur - 1]))* math.cos(math.radians(lat[curseur])) \
            * math.cos(math.radians(long[curseur - 1]) - math.radians(long[curseur])))
        distance_tot = distance_tot + dist

    #calcul de vitesse
    vitesse = distance_tot/((temps_en_seconde[p]-temps_en_seconde[0])/3600)

    # calcul de calories
    # exemple  de Viktor Röthlin (172cm/60kg/48 ans )
    calories = distance_tot * 60 * 1.036

    # calcul d'intensité
    FCmax = 207 - (0.7 * 48) 
    intensite = (card[p] / FCmax) * 100

    # création du text à afficher
        # données du csv et données calculés
    txt = " Heure : " + str(heures_entieres[p]) \
        + "\n Cardio : " + str(card[p]) + "bpm" \
        + "\n Altitude : " + str(alt[p]) + "m" \
        + "\n Distance parcourue : " + str(round(distance_tot,2)) + "Km" \
        + "\n Vitesse : " + str(round(vitesse,2)) + "Km/h" \
        + "\n Calorie : " + str(round(calories,2)) + "kcal" \
        + "\n Intensité : " + str(round(intensite,2)) + "%"
    marker.set_text(txt)    # afficher le text au dessus du marker
    
# Gérer le curseur avec un slider
curseur = Scale(
    root_tk,
    orient = HORIZONTAL,
    from_ = 0,
    to=len(lat)-1,
    command = gerer_curseur,
    length=1000,
    )

curseur.grid(column=0, row=1)   # prosition du slider
root_tk.mainloop()