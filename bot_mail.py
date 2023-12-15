import smtplib
import pandas as pd
import time
import random

df = pd.read_csv('./files/test.csv', delimiter=';')
print(df.columns)

# Paramètres SMTP 587 parce qu'il permet un chiffrement STARTTLS,ca garantit une communication sécurisée entre votre programme Python et les serveurs mail.
# GMAIL PAS POSSIBLE ! depuis fin 2022 besoin compte admin etc ...
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = 'weatherwizardg7@outlook.fr'
smtp_password = 'Magical07/12'

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

# On applique l'envoie du mail à chacune des lignes de notre fichier
for index, row in df.iterrows():
    destinataire = row['Email']
    sujet = 'Risque d''innondation'
    corps = f"Madame Monsieur,\n\n L équipe Weather Wizard vous contact afin de signaler une possible d'innondation.\n\n Bonne journée à vous."

    # Condition pour décider d'envoyer l'e-mail ou non basé sur profondeur de l'eau
    if row['seuil'] == 'critique':
        envoyer_email(destinataire, sujet, corps)
    else:
        print(f"Pas d'email {destinataire} parce que pas innondation.")

    # ajout de délais random pour éviter ban !
    délais = random.uniform(1, 5)
    time.sleep(délais)
