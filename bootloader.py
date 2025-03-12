import time
import re
import yaml
import subprocess
from pathlib import Path
from pyfiglet import figlet_format
from termcolor import colored

def is_valid_ip(ip):
    pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    if pattern.match(ip):
        return all(0 <= int(octet) <= 255 for octet in ip.split('.'))
    return False

def get_ip():
    while True:
        ip = input(colored("Veuillez entrer l'adresse IP du MOM : ", 'cyan'))
        if is_valid_ip(ip):
            return ip
        print(colored("Adresse IP invalide. Veuillez entrer une adresse IP valide.", 'red'))

def get_role():
    roles = {"1": "Asker", "2": "Brainer", "3": "Memory"}
    while True:
        print(colored("\nChoisissez votre rôle :", 'yellow'))
        print(colored("1 - Asker", 'blue'))
        print(colored("2 - Brainer", 'blue'))
        print(colored("3 - Memory", 'blue'))
        choix = input(colored("Entrez le numéro correspondant à votre rôle : ", 'cyan'))
        if choix in roles:
            return roles[choix]
        print(colored("Choix invalide. Veuillez sélectionner un rôle valide.", 'red'))

def update_config(role, ip):
    config_path = Path.home() / 'Brainer' / 'configuration.yml'
    if not config_path.exists():
        print(colored(f"Le fichier de configuration {config_path} est introuvable.", 'red'))
        return
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    config['role'] = role.lower()
    config['rabbitmq']['host'] = ip
    
    with open(config_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    
    print(colored("Configuration mise à jour avec succès !", 'green'))

def launch_brainer():
    brainer_path = Path.home() / 'Brainer'
    activate_venv = brainer_path / 'venv' / 'bin' / 'activate'
    main_script = brainer_path / 'main.py'
    config_file = brainer_path / 'configuration.yml'
    
    print(colored("Lancement de l'application Brainer...", 'cyan'))
    subprocess.run(f"cd {brainer_path} && source {activate_venv} && clear && python3 {main_script} -c {config_file}", shell=True, executable='/bin/bash')

# Affichage stylisé
time.sleep(0.5)
print(colored(figlet_format("Brainer app"), 'magenta'))

# Récupération des données
mom_ip = get_ip()
role = get_role()

# Mise à jour de la configuration
update_config(role, mom_ip)

# Lancement de l'application
launch_brainer()