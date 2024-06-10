import json
import os
import shutil

# Chargement du fichier JSON de configuration
with open('./export.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Fonction pour extraire les chemins des fichiers depuis les sources
def extract_file_paths(config):
    file_paths = []
    for source in config.get('sources', []):
        if source['id'] == 'vlc_source':
            for item in source['settings'].get('playlist', []):
                file_paths.append(item['value'])
    return file_paths

# Copie des fichiers vers le dossier courant
def copy_files(file_paths, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for file_path in file_paths:
        if os.path.exists(file_path):
            shutil.copy(file_path, destination_folder)
        else:
            print(f"File not found: {file_path}")

# Extraction des chemins des fichiers
file_paths = extract_file_paths(config)

# Dossier de destination (dossier courant)
destination_folder = './copied_media_files'

# Copie des fichiers
copy_files(file_paths, destination_folder)

print("All files have been copied to:", destination_folder)
