import os
from pdf2image import convert_from_path

def convert_pdf_to_jpg(pdf_folder, output_folder):
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parcourir tous les fichiers PDF dans le dossier source
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            images = convert_from_path(pdf_path)

            # Enregistrer les images dans le dossier de sortie avec le même nom de fichier
            for i, image in enumerate(images):
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_page_{i+1}.jpg")
                image.save(output_path, "JPEG")

# Exemple d'utilisation
pdf_folder = "source"
output_folder = "dataaa"

convert_pdf_to_jpg(pdf_folder, output_folder)
