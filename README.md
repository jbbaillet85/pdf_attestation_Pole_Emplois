[![wakatime](https://wakatime.com/badge/user/648b0556-0c0e-4e9d-b952-2bea950dabe6/project/45470d41-9b13-40de-b61a-c6c40ffe9b39.svg)](https://wakatime.com/badge/user/648b0556-0c0e-4e9d-b952-2bea950dabe6/project/45470d41-9b13-40de-b61a-c6c40ffe9b39)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a0aa7a87c160491c81f94692df4a1a40)](https://www.codacy.com/gh/jbbaillet85/pdf_attestation_Pole_Emplois/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jbbaillet85/pdf_attestation_Pole_Emplois&amp;utm_campaign=Badge_Grade)

# Les attestations Pôle Emplois et le pdf
## Exposition du besoin

Certains employeurs fournissent l'attestation Pole Emplois, le certificat de travail et le solde de tout compte sur le même document pdf. Or Pole Emplois refuse de mettre plusieurs documents dans le même fichier.
Que faire ? scanner pages par page ? imprimer les certaines pages au format pdf et renommer le fichier ?
Bref, il est plus que temps d'automatiser avec python un programme pour cette problématique.

## Pré-requis
- Python 3.10
- pypdf2

## Fonctionnalités
- gestion_dossier: créer un dossiers pour mettre les pdf à modifier et un pour les pdfs modifiés.