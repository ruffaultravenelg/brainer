#!/bin/bash

# Installation de venv si nécessaire
if ! command -v python3 -m venv &> /dev/null
then
    echo "venv non trouvé, installation..."
    sudo apt update
    sudo apt install -y python3-venv
fi

# Création de l'environnement virtuel
python3 -m venv venv

# Activation de l'environnement virtuel
source venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt

# Execution du script python d'installation
python updateConf.py

# Ajouter l'ouverture automatique au bashrc
BASHRC="$HOME/.bashrc"
LINES=(
  "cd ~/brainer"
  "source venv/bin/activate"
  "clear"
  "python3 main.py -c configuration.yml"
)

# Fonction pour vérifier si une ligne existe déjà dans le .bashrc
line_exists() {
  grep -Fxq "$1" "$BASHRC"
}

# Ajouter les lignes si elles n'existent pas
for line in "${LINES[@]}"; do
  if ! line_exists "$line"; then
    echo "$line" >> "$BASHRC"
  fi
done

# Recharger le .bashrc
source "$BASHRC"