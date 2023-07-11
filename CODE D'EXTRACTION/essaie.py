import os
import csv
import pytesseract
from PIL import Image

# Définir le chemin du dossier contenant les fichiers
dossier_data = 'C:/Users/lenovo/Desktop/jfk_project/data'

# Définir le chemin du fichier CSV de sortie
fichier_csv = 'fichier3.csv'

# Configuration de pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Fonction pour extraire le texte d'une image
def extraire_texte(image_path):
    image = Image.open(image_path)
    texte = pytesseract.image_to_string(image, lang='fra')
    return texte.strip()

# Liste pour stocker les résultats
resultats = []

# Parcourir les fichiers du dossier data
for fichier in os.listdir(dossier_data):
    chemin_fichier = os.path.join(dossier_data, fichier)
    if os.path.isfile(chemin_fichier):
        extension = os.path.splitext(fichier)[1].lower()
        if extension == '.jpg' or extension == '.png':
            texte = extraire_texte(chemin_fichier)
            resultats.append(texte)

# Écrire les résultats dans le fichier CSV
with open(fichier_csv, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Texte'])  # Écrire l'en-tête du fichier CSV
    for resultat in resultats:
        writer.writerow([resultat])

import pandas as pd

# Chemin d'accès au fichier CSV
csv_file = 'fichier3.csv'

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(csv_file)

# Afficher toutes les lignes du DataFrame sans troncature
pd.set_option('display.max_rows', None)
print(df)

df.head()