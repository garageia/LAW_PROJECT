import os
import csv
import pytesseract
import pandas as pd
from PIL import Image
import dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader


#extraction de texte des fichiers jpg

# Définir le chemin du dossier contenant les fichiers
dossier_data = 'C:/Users/lenovo/Desktop/jfk_project/data'

# Définir le chemin du fichier CSV de sortie
fichier_csv = 'fichier2.csv'

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
        elif extension == '.pdf':
            pass
# Chemin d'accès au fichier CSV
csv_file = 'fichier2.csv'

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(csv_file)

# Afficher toutes les lignes du DataFrame sans troncature
pd.set_option('display.max_rows', None)
print(df)

df.head()

#extraction de texte des fichiers jpg


# Écrire les résultats dans le fichier CSV
with open(fichier_csv, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Texte'])  # Écrire l'en-tête du fichier CSV
    for resultat in resultats:
        writer.writerow([resultat])




# Charge le fichier .env avec votre clé d'API OPENAI_API_KEY
dotenv.load_dotenv()

#fichier csv
loader = CSVLoader("fichier2.csv", csv_args={"delimiter": ','}, encoding="utf-8")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1400, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Clé d'API OpenAIEmbeddings
openai_api_key = "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"  # Remplacez "your_api_key" par votre véritable clé d'API

# Crée l'objet OpenAIEmbeddings et l'index FAISS
openai_embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
faissIndex = FAISS.from_documents(docs, openai_embeddings)
faissIndex.save_local("faiss_midjourney_docs")
