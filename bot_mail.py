import smtplib
import pandas as pd

# Charger votre fichier CSV ou Excel
df = pd.read_csv('input à régler')

# Paramètres SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'créer mail pour envoyer + git ignore'
smtp_password = 'mdp à définir'

# Fonction pour envoyer un e-mail
def envoyer_email(destinataire, sujet, corps):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        message = f'Subject: {sujet}\n\n{corps}'
        server.sendmail(smtp_username, destinataire, message)

        print(f'E-mail envoyé à {destinataire}')
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
    finally:
        server.quit()

# Parcourir chaque ligne du DataFrame
for index, row in df.iterrows():
    destinataire = row['Email']
    sujet = 'Sujet de l\'e-mail'
    corps1 = f"Madame Monsieur,\n\nCeci est un mail ayant pour but d'alerter sur un risque d'innondation."

    # Condition pour décider d'envoyer l'e-mail ou non
    if row['Colonne_condition'] == 'Condition_souhaitee':
        envoyer_email(destinataire, sujet, corps)
    else:
        print(f"Ne pas envoyer d'e-mail à {destinataire} en raison de la condition non remplie.")
