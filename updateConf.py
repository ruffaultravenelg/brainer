import yaml
from termcolor import colored
import pyfiglet

# Affichage du titre stylisé
def print_banner():
    banner = pyfiglet.figlet_format("CONFIGURATION")
    print(colored(banner, 'cyan'))

# Demande une entrée utilisateur avec une valeur par défaut
def ask_question(question, default):
    user_input = input(f"{question} (default: {default}): ").strip()
    return user_input if user_input else default

# Chargement de la configuration existante
def load_config(file_path='configuration.yml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Sauvegarde de la configuration mise à jour
def save_config(config, file_path='configuration.yml'):
    with open(file_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False, sort_keys=False)

# Programme principal
def main():
    print_banner()
    config = load_config()

    # Choix du rôle
    print(colored("Configuration du rôle:", 'yellow'))
    role = ask_question("Choisissez le rôle (asker, brainer, memory)", config.get('role', 'asker'))
    config['role'] = role

    # Configuration RabbitMQ
    print(colored("Configuration de RabbitMQ:", 'yellow'))
    config['rabbitmq']['host'] = ask_question("Adresse IP de RabbitMQ", config['rabbitmq'].get('host', 'localhost'))
    config['rabbitmq']['port'] = ask_question("Port de RabbitMQ", config['rabbitmq'].get('port', '5672'))
    config['rabbitmq']['credentials']['username'] = ask_question("Nom d'utilisateur RabbitMQ", config['rabbitmq']['credentials'].get('username', 'testuser'))
    config['rabbitmq']['credentials']['password'] = ask_question("Mot de passe RabbitMQ", config['rabbitmq']['credentials'].get('password', 'testpass'))

    # Configuration MongoDB
    print(colored("Configuration de MongoDB:", 'yellow'))
    config['mongodb']['host'] = ask_question("Adresse IP de MongoDB", config['mongodb'].get('host', 'localhost'))
    config['mongodb']['port'] = ask_question("Port de MongoDB", config['mongodb'].get('port', '27017'))
    config['mongodb']['credentials']['username'] = ask_question("Nom d'utilisateur MongoDB", config['mongodb']['credentials'].get('username', 'testmongouser'))
    config['mongodb']['credentials']['password'] = ask_question("Mot de passe MongoDB", config['mongodb']['credentials'].get('password', 'testmongopass'))

    # Sauvegarde finale
    save_config(config)
    print(colored("Configuration mise à jour avec succès!", 'green'))

if __name__ == '__main__':
    main()
